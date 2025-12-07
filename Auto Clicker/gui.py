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
        self.title("Auto Clicker")
        self.geometry("500x560")
        self.resizable(False, False)

        title_container = ctk.CTkFrame(self, fg_color=self.COLORS["secondary_bg"])
        title_container.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(
            title_container,
            text="Auto Clicker",
            font=self.FONTS["title"],
            text_color=self.COLORS["text"],
        ).pack(pady=15)

        content_container = ctk.CTkFrame(self, fg_color=self.COLORS["primary_bg"])
        content_container.pack(fill="both")

        positions_container = ctk.CTkFrame(content_container, fg_color=self.COLORS["secondary_bg"])
        positions_container.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            positions_container,
            text="Pressione o botão para gravar as posições dos cliques",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)

        self.positions_counter = ctk.CTkLabel(
            positions_container,
            width=400,
            text="Total de posições: 0",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["primary_bg"],
        )
        self.positions_counter.pack(pady=10, padx=30)

        positions_buttons_frame = ctk.CTkFrame(positions_container, fg_color="transparent")
        positions_buttons_frame.pack(fill="x", pady=10, padx=10)

        self.positions_start = ctk.CTkButton(
            positions_buttons_frame,
            height=self.height,
            text="Gravar Posições",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.positions_start.pack(side="left", padx=(70, 0))

        self.positions_end = ctk.CTkButton(
            positions_buttons_frame,
            height=self.height,
            text="Parar de Gravar",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )

        self.reset_positions = ctk.CTkButton(
            positions_buttons_frame,
            height=self.height,
            text="Resetar Posições",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.reset_positions.pack(side="right", padx=(0, 70))

        ctk.CTkLabel(
            positions_container,
            text="(As posições podem ser controladas pela tecla 'F1')",
            font=self.FONTS["message"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)

        clicker_container = ctk.CTkFrame(content_container, fg_color=self.COLORS["secondary_bg"])
        clicker_container.pack(fill="x", pady=10, padx=10)

        ctk.CTkLabel(
            clicker_container,
            text="Clique nos botões para controlar o 'Auto Clicker'",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)

        self.clicks_counter = ctk.CTkLabel(
            clicker_container,
            width=400,
            text="Total de cliques: 0",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
            fg_color=self.COLORS["primary_bg"],
        )
        self.clicks_counter.pack(pady=10, padx=30)

        clicker_speed_frame = ctk.CTkFrame(clicker_container, fg_color="transparent")
        clicker_speed_frame.pack(fill="x", pady=5, padx=10)

        self.speed_value = ctk.CTkLabel(
            clicker_speed_frame,
            text="Velocidade dos cliques: (2.50)",
            font=self.FONTS["text"],
            text_color=self.COLORS["text"],
        )
        self.speed_value.pack(side="left", padx=(30, 0))

        self.speed_slider = ctk.CTkSlider(clicker_speed_frame, from_=0.01, to=5.0)
        self.speed_slider.pack(fill="x", side="right", padx=(0, 30))
        self.speed_slider.set(2.5)

        clicker_buttons_frame = ctk.CTkFrame(clicker_container, fg_color="transparent")
        clicker_buttons_frame.pack(fill="x", pady=10, padx=10)

        self.start_button = ctk.CTkButton(
            clicker_buttons_frame,
            height=self.height,
            text="Iniciar Clicker",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.start_button.pack(side="left", padx=(70, 0))

        self.finish_button = ctk.CTkButton(
            clicker_buttons_frame,
            height=self.height,
            text="Encerrar Clicker",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )

        self.reset_clicks = ctk.CTkButton(
            clicker_buttons_frame,
            height=self.height,
            text="Resetar Clicks",
            font=self.FONTS["button"],
            text_color=self.COLORS["button_text"],
            fg_color=self.COLORS["button"],
            hover_color=self.COLORS["button_hover"],
        )
        self.reset_clicks.pack(side="right", padx=(0, 70))

        ctk.CTkLabel(
            clicker_container,
            text="(O Clicker pode ser controlado pela tecla 'F2')",
            font=self.FONTS["message"],
            text_color=self.COLORS["text"],
        ).pack(pady=10, padx=30)
