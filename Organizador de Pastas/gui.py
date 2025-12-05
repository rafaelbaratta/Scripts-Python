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
            "button": ("Arial", 16, "bold"),
        }

        self.height = 40
        self.checkbox_size = 20
        self.checkbox_border = 2

        self.build()

    def build(self):
        self.title("Organizador de Pastas")
        self.geometry("500x560")
        self.resizable(False, False)

        title_container = ctk.CTkFrame(self, fg_color=self.COLORS["secondary_bg"])
        title_container.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            title_container,
            text="Organizador de Pastas",
            font=self.FONTS["title"],
            text_color=self.COLORS["text"],
        ).pack(pady=15)

        content_container = ctk.CTkFrame(self, fg_color=self.COLORS["primary_bg"])
        content_container.pack(fill="both")

        entry_container = ctk.CTkFrame(
            content_container, fg_color=self.COLORS["secondary_bg"]
        )
        entry_container.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            entry_container,
            text="Insira ou procure o caminho da pasta/diretório:",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)

        self.text_entry = ctk.CTkEntry(
            entry_container,
            width=340,
            height=self.height,
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        )
        self.text_entry.pack(side="left", pady=(10, 20), padx=(20, 0))

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

        options_container = ctk.CTkFrame(
            content_container, fg_color=self.COLORS["secondary_bg"]
        )
        options_container.pack(fill="both", pady=10, padx=10)

        options_container.grid_columnconfigure(0, weight=1)
        options_container.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            options_container,
            text="Escolha a configuração de pastas:",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).grid(row=0, column=0, columnspan=2, pady=10, padx=30)

        self.documents_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Documentos",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.documents_checkbox.grid(
            row=1, column=0, pady=5, padx=(20, 0), sticky="nsew"
        )
        self.documents_checkbox.select()

        self.images_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Imagens",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.images_checkbox.grid(row=1, column=1, pady=5, padx=(0, 20), sticky="nsew")
        self.images_checkbox.select()

        self.audios_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Áudios",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.audios_checkbox.grid(row=2, column=0, pady=5, padx=(20, 0), sticky="nsew")
        self.audios_checkbox.select()

        self.videos_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Vídeos",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.videos_checkbox.grid(row=2, column=1, pady=5, padx=(0, 20), sticky="nsew")
        self.videos_checkbox.select()

        self.binary_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Binários/Executáveis",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.binary_checkbox.grid(row=3, column=0, pady=5, padx=(20, 0), sticky="nsew")

        self.compacted_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Compactados",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.compacted_checkbox.grid(
            row=3, column=1, pady=5, padx=(0, 20), sticky="nsew"
        )

        self.data_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Dados/Banco de Dados",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.data_checkbox.grid(row=4, column=0, pady=5, padx=(20, 0), sticky="nsew")

        self.programming_checkbox = ctk.CTkCheckBox(
            options_container,
            checkbox_width=self.checkbox_size,
            checkbox_height=self.checkbox_size,
            border_width=self.checkbox_border,
            text="Códigos Fonte",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.programming_checkbox.grid(
            row=4, column=1, pady=5, padx=(0, 20), sticky="nsew"
        )

        ctk.CTkLabel(
            options_container,
            text="(Outros tipos de arquivos estarão na pasta 'Outros')",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).grid(row=5, column=0, columnspan=2, pady=10, padx=30)

        self.generate_button = ctk.CTkButton(
            content_container,
            height=self.height,
            text="Organizar Pasta",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.generate_button.pack(pady=10)
