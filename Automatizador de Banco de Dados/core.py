import csv
import os
import re
import sqlite3 as sql

from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog


class Core:

    def __init__(self, gui):
        self.gui = gui

        self.connection = None
        self.cursor = None

        self.database = ""
        self.directory_path = ""

        self.sql_files = []
        self.csv_files = []

        self.gui.directory_button.configure(command=self.get_path)
        self.gui.run_button.configure(command=self.execute)

    def get_path(self):
        path = filedialog.askdirectory()
        self.gui.directory_entry.delete(0, "end")
        self.gui.directory_entry.insert(0, path)

    def verify_directory(self):
        path = self.gui.directory_entry.get()
        if not path or not os.path.exists(path) or not os.path.isdir(path):
            CTkMessagebox(
                title="Erro!",
                message="Caminho de diretório inválido. Por favor, insira um caminho válido.",
                icon="cancel",
            )
            return False
        self.directory_path = path
        return True

    def get_files(self):
        files = os.listdir(self.directory_path)

        self.sql_files = [f for f in files if f.endswith(".sql")]
        self.csv_files = [f for f in files if f.endswith(".csv")]

        if not self.sql_files and not self.csv_files:
            CTkMessagebox(
                title="Info!",
                message="Nenhum arquivo .sql ou .csv encontrado no diretório especificado.",
                icon="info",
            )
            return

    def create_database(self):
        if not self.database:
            CTkMessagebox(
                title="Info!",
                message="Por favor, crie ou insira um nome de banco de dados válido.",
                icon="info",
            )
            return

        try:
            self.connection = sql.connect(f"{self.directory_path}/{self.database}.db")
            self.cursor = self.connection.cursor()
            self.cursor.execute("PRAGMA foreign_keys = ON")
        except sql.Error as e:
            CTkMessagebox(
                title="Erro!",
                message=f"Erro! ao conectar ao banco de dados:\n{e}",
                icon="cancel",
            )
            return

    def create_tables(self):
        if not self.sql_files:
            CTkMessagebox(
                title="Info!",
                message="Nenhum arquivo .sql encontrado no diretório especificado.",
                icon="info",
            )
            return

        if not self.connection:
            self.create_database()
            if not self.connection:
                return

        for sql_file in self.sql_files:
            with open(os.path.join(self.directory_path, sql_file), "r", encoding="utf-8") as file:
                context = file.read()

            commands = context.split(";")
            commands = [" ".join(command.split()) + ";" for command in commands if command.strip()]

            for command in commands:
                try:
                    self.cursor.execute(command)
                except sql.Error as e:
                    self.connection.rollback()
                    CTkMessagebox(
                        title="Erro!",
                        message=f"Erro! ao criar tabela a partir do arquivo {sql_file}:\n{e}",
                        icon="cancel",
                    )
                    return

        self.connection.commit()
        CTkMessagebox(
            title="Sucesso",
            message="Tabelas criadas com sucesso no banco de dados.",
            icon="check",
        )

    def get_tables(self):
        if not self.connection:
            self.create_database()
            if not self.connection:
                return

        query = "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        all_tables = [row[0] for row in self.cursor.execute(query).fetchall()]

        tables_with_fks = []
        tables_without_fks = []

        for table in all_tables:
            query = f"PRAGMA foreign_key_list({table});"
            foreign_keys = self.cursor.execute(query).fetchall()

            if foreign_keys:
                tables_with_fks.append(table.lower())
            else:
                tables_without_fks.append(table.lower())

        return tables_with_fks, tables_without_fks

    def get_foreign_keys(self, table_name):
        query = f"PRAGMA foreign_key_list({table_name});"
        foreign_keys = self.cursor.execute(query).fetchall()
        return foreign_keys

    def resolve_foreign_keys(self, headers, values, foreign_keys):
        for fk in foreign_keys:
            fk_column = fk[3]
            ref_table = fk[2]
            ref_column = fk[4]

            if fk_column in headers:
                fk_index = headers.index(fk_column)
                self.cursor.execute(f"PRAGMA table_info({ref_table});")

                ref_columns = self.cursor.fetchall()
                ref_columns = [col for col in ref_columns if col[1] != ref_column]

                for value in values:
                    ref_value = value[fk_index]
                    conditions = " OR ".join([f"{col[1]} = ?" for col in ref_columns])
                    query = f"SELECT {ref_column} FROM {ref_table} WHERE {conditions};"
                    result = self.cursor.execute(query, [ref_value] * len(ref_columns)).fetchone()

                    if not result:
                        CTkMessagebox(
                            title="Info!",
                            message=f"Chave estrangeira {ref_value} inválida ou não encontrada na tabela {ref_table}.",
                            icon="info",
                        )
                        return

                    value[fk_index] = str(result[0])

        return values

    def insert_data(self, tables):
        if not self.csv_files:
            CTkMessagebox(
                title="Info!",
                message="Nenhum arquivo .csv encontrado no diretório especificado.",
                icon="info",
            )
            return

        if not self.connection:
            self.create_database()
            if not self.connection:
                return

        for csv_file in self.csv_files:
            table_name = os.path.splitext(csv_file)[0].lower()
            file_path = os.path.join(self.directory_path, csv_file)
            foreign_keys = self.get_foreign_keys(table_name)

            if table_name not in tables:
                continue

            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                headers = next(reader)
                values = [line for line in reader if line]

                if not values:
                    continue

                if foreign_keys:
                    values = self.resolve_foreign_keys(headers, values, foreign_keys)

                if values is None:
                    CTkMessagebox(
                        title="Erro!",
                        message=f"Erro ao resolver chaves estrangeiras no arquivo {csv_file}.",
                        icon="cancel",
                    )
                    return

                placeholders = ", ".join(["?"] * len(headers))
                insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"

                try:
                    self.cursor.executemany(insert_query, values)
                except sql.Error as e:
                    self.connection.rollback()
                    CTkMessagebox(
                        title="Erro!",
                        message=f"Erro ao inserir dados do arquivo {csv_file}:\n{e}",
                        icon="cancel",
                    )
                    return

        self.connection.commit()
        CTkMessagebox(
            title="Sucesso",
            message="Dados inseridos com sucesso no banco de dados.",
            icon="check",
        )

    def execute(self):
        if not self.verify_directory():
            return

        self.database = self.gui.database_entry.get().strip()

        if not self.database or not re.match(r"^[A-Za-z0-9_-]+$", self.database):
            CTkMessagebox(
                title="Info!",
                message="Por favor, insira um nome válido para o banco de dados.",
                icon="info",
            )
            return

        create_db = self.gui.create_database_checkbox.get()
        create_tables = self.gui.create_tables_checkbox.get()
        insert_data = self.gui.insert_data_checkbox.get()

        if not create_db and not create_tables and not insert_data:
            CTkMessagebox(
                title="Info!",
                message="Por favor, selecione ao menos uma opção para executar.",
                icon="info",
            )
            return

        self.get_files()
        if create_db:
            self.create_database()
        if create_tables:
            self.create_tables()
        if insert_data:
            tables_with_fks, tables_without_fks = self.get_tables()
            if tables_without_fks:
                self.insert_data(tables_without_fks)
            if tables_with_fks:
                self.insert_data(tables_with_fks)

        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
