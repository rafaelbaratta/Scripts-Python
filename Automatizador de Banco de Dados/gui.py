import customtkinter as ctk


class Gui(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")

        self.COLORS = {
            "primary_bg": "#242424",
            "secondary_bg": "#2e2e2e",
            "button": "#bb4f02",
            "button_hover": "#ce5804",
            "button_text": "#ffffff",
            "text": "#ffffff",
        }

        self.FONTS = {
            "title": ("Arial", 28, "bold"),
            "text": ("Arial", 14),
            "message": ("Arial", 12),
            "button": ("Arial", 16, "bold"),
        }

        self.height = 40

        self.build()

    def build(self):
        self.title("Automatizador de Banco de Dados")
        self.geometry("500x500")
        self.resizable(False, False)

        title_container = ctk.CTkFrame(self, fg_color=self.COLORS["secondary_bg"])
        title_container.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            title_container,
            text="Automatizador Banco de Dados",
            font=self.FONTS["title"],
            text_color=self.COLORS["text"],
        ).pack(pady=15)

        content_container = ctk.CTkFrame(self, fg_color=self.COLORS["primary_bg"])
        content_container.pack(fill="both")

        entry_container = ctk.CTkFrame(content_container, fg_color=self.COLORS["secondary_bg"])
        entry_container.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            entry_container,
            text="Insira ou procure o caminho da pasta/diretório com os dados:\n\n"
            "* Tabelas em formato .sql e dados em .csv\n"
            "* Não organize em subpastas",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)

        self.directory_entry = ctk.CTkEntry(
            entry_container,
            width=340,
            height=self.height,
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        )
        self.directory_entry.pack(side="left", pady=(10, 20), padx=(20, 0))

        self.directory_button = ctk.CTkButton(
            entry_container,
            height=self.height,
            width=40,
            text="Procurar",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.directory_button.pack(side="right", pady=(10, 20), padx=(0, 20))

        database_container = ctk.CTkFrame(content_container, fg_color=self.COLORS["secondary_bg"])
        database_container.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            database_container,
            text="Digite o nome do banco de dados:",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)

        self.database_entry = ctk.CTkEntry(
            database_container,
            width=400,
            height=self.height,
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        )
        self.database_entry.pack(pady=(0, 10), padx=20)

        checkbox_container = ctk.CTkFrame(database_container, fg_color="transparent")
        checkbox_container.pack(fill="x", pady=10, padx=10)

        self.create_database_checkbox = ctk.CTkCheckBox(
            checkbox_container,
            checkbox_width=20,
            checkbox_height=20,
            border_width=2,
            text="Criar Banco de Dados",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.create_database_checkbox.grid(row=0, column=0, padx=10)
        self.create_database_checkbox.select()

        self.create_tables_checkbox = ctk.CTkCheckBox(
            checkbox_container,
            checkbox_width=20,
            checkbox_height=20,
            border_width=2,
            text="Criar Tabelas",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.create_tables_checkbox.grid(row=0, column=1, padx=10)
        self.create_tables_checkbox.select()

        self.insert_data_checkbox = ctk.CTkCheckBox(
            checkbox_container,
            checkbox_width=20,
            checkbox_height=20,
            border_width=2,
            text="Inserir Dados",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.insert_data_checkbox.grid(row=0, column=2, padx=10)
        self.insert_data_checkbox.select()

        self.run_button = ctk.CTkButton(
            content_container,
            height=self.height,
            text="Executar",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.run_button.pack(pady=10)
