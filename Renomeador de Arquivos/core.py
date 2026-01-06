import os
from pathlib import Path

from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog


class Core:

    def __init__(self, gui):
        self.gui = gui

        self.gui.directory_button.configure(command=self.get_path)
        self.gui.rename_button.configure(command=self.rename_files)
        self.gui.clear_fields_button.configure(command=self.clear_fields)

        self.entries = [
            self.gui.insert_entry,
            self.gui.position_insert_entry,
            self.gui.remove_entry,
            self.gui.text_to_be_replaced_entry,
            self.gui.text_to_replace_entry,
            self.gui.prefix_entry,
            self.gui.suffix_entry,
        ]

    def get_path(self):
        directory_path = filedialog.askdirectory()
        self.gui.path_entry.delete(0, "end")
        self.gui.path_entry.insert(0, directory_path)

    def clear_fields(self):
        for entry in self.entries:
            entry.delete(0, "end")

    def rename_files(self):
        directory = self.get_directory()

        if not directory:
            return

        os.chdir(directory)

        if self.empty_fields():
            CTkMessagebox(
                title="Info!",
                message="Todas as opções de modificação estão em branco!",
                icon="info",
            )
            return

        files = os.listdir(directory)

        if not files:
            CTkMessagebox(
                title="Info!",
                message="Não há nada no diretório fornecido!",
                icon="info",
            )
            return

        counter = 0
        for file in files:
            file = Path(file)
            new_filename = self.add_modifications(file.stem)

            try:
                os.rename(file, new_filename + file.suffix)

            except FileExistsError:
                CTkMessagebox(
                    title="Info!",
                    message=f"Já existe um arquivo com o nome {new_filename}!",
                    icon="info",
                )
                break

            except PermissionError:
                CTkMessagebox(
                    title="Info!",
                    message=f"Você não tem permissão para mover renomear o arquivo {file}!",
                    icon="info",
                )
                break

            except Exception:
                CTkMessagebox(
                    title="Info!",
                    message=f"Falha ao renomear o arquivo {file}!",
                    icon="info",
                )
                break

            else:
                counter += 1

        CTkMessagebox(
            title="Info!",
            message=f"{counter} arquivos renomeados com sucesso!",
            icon="info",
        )
        return None

    def get_directory(self):
        data = self.gui.path_entry.get()

        if not data:
            CTkMessagebox(
                title="Info!",
                message="Não deixe o caminho em branco!",
                icon="info",
            )
            return None

        elif not os.path.isdir(data):
            CTkMessagebox(
                title="Info!",
                message="Caminho inserido não é um diretório!",
                icon="info",
            )
            return None

        return data

    def empty_fields(self):
        for entry in self.entries:
            if entry.get():
                return False
        return True

    def add_modifications(self, filename):
        filename = self.remove_text(filename)
        filename = self.replace_text(filename)
        filename = self.insert_text(filename)

        return filename

    def remove_text(self, filename):
        text_to_remove = self.entries[2].get()

        if text_to_remove:
            filename = filename.replace(text_to_remove, "")

        return filename

    def replace_text(self, filename):
        text_to_be_replaced = self.entries[3].get()
        text_to_replace = self.entries[4].get()

        if text_to_be_replaced and text_to_replace:
            filename = filename.replace(text_to_be_replaced, text_to_replace)

        return filename

    def insert_text(self, filename):
        text_to_insert = self.entries[0].get()
        position_to_insert = self.entries[1].get()

        try:
            if position_to_insert:
                position_to_insert = int(position_to_insert)

                if position_to_insert > len(filename):
                    CTkMessagebox(
                        title="Info!",
                        message="Insira uma posição menor que o tamanho do nome do arquivo!",
                        icon="info",
                    )
                    return filename

                if text_to_insert:
                    filename = filename[:position_to_insert] + text_to_insert + filename[position_to_insert:]

        except ValueError:
            CTkMessagebox(
                title="Info!",
                message="Insira um número inteiro para a posição do texto que será inserido!",
                icon="info",
            )
            return filename

        prefix_to_insert = self.entries[5].get()
        suffix_to_insert = self.entries[6].get()

        if prefix_to_insert:
            filename = prefix_to_insert + filename

        if suffix_to_insert:
            filename = filename + suffix_to_insert

        return filename
