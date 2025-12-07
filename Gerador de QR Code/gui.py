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

        self.build()

    def build(self):
        self.title("Gerador de QR Code")
        self.geometry("500x580")
        self.resizable(False, False)

        title_container = ctk.CTkFrame(self, fg_color=self.COLORS["secondary_bg"])
        title_container.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            title_container,
            text="Gerador de QR Code",
            font=self.FONTS["title"],
            text_color=self.COLORS["text"],
        ).pack(pady=15)

        content_container = ctk.CTkFrame(self, fg_color=self.COLORS["primary_bg"])
        content_container.pack(fill="both")

        entry_container = ctk.CTkFrame(content_container, fg_color=self.COLORS["secondary_bg"])
        entry_container.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            entry_container,
            text="Insira um texto, link ou arquivo para gerar um QR Code:",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)

        self.text_entry = ctk.CTkEntry(
            entry_container,
            height=self.height,
            width=340,
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            placeholder_text="Digite ou insira o conteúdo...",
        )
        self.text_entry.pack(side="left", pady=(10, 20), padx=(20, 0))

        self.file_button = ctk.CTkButton(
            entry_container,
            height=self.height,
            width=40,
            text="Procurar",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.file_button.pack(side="right", pady=(10, 20), padx=(0, 20))

        code_container = ctk.CTkFrame(content_container, fg_color=self.COLORS["secondary_bg"])
        code_container.pack(fill="x", pady=10, padx=10)

        self.code_label = ctk.CTkLabel(
            code_container,
            image=None,
            text="Código a ser gerado...",
            height=220,
            width=220,
            fg_color=self.COLORS["primary_bg"],
        )
        self.code_label.pack(pady=20, padx=30)

        self.generate_button = ctk.CTkButton(
            content_container,
            height=self.height,
            text="Gerar Código",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.generate_button.pack(side="left", pady=10, padx=(70, 0))

        self.save_button = ctk.CTkButton(
            content_container,
            height=self.height,
            text="Salvar Código",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["secondary_bg"],
            state="disabled",
        )
        self.save_button.pack(side="right", pady=10, padx=(0, 70))
