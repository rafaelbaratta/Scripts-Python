import os

import qrcode
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkImage, filedialog


class Core:

    def __init__(self, gui):
        self.gui = gui
        self.img = None

        self.gui.file_button.configure(command=self.get_path)
        self.gui.generate_button.configure(command=self.generate_code)
        self.gui.save_button.configure(command=self.save_code)

    def get_path(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos texto", "*.txt")])
        self.gui.text_entry.delete(0, "end")
        self.gui.text_entry.insert(0, file_path)

    def generate_code(self):
        data = self.get_data()

        if not data:
            return

        try:
            self.img = qrcode.make(data)
        except ValueError:
            option = CTkMessagebox(
                title="Info!",
                message="Conteúdo extenso para QR code, uma parte poderá ser cortada!",
                icon="info",
                option_1="Aceitar mesmo assim",
                option_2="Cancelar",
            )
            if option.get() == "Cancelar":
                return
            self.img = qrcode.make(data[:2100])

        converted_img = self.img.convert("RGB")

        ctk_img = CTkImage(
            light_image=converted_img, dark_image=converted_img, size=(220, 220)
        )
        self.gui.code_label.configure(image=ctk_img)
        self.gui.code_label.configure(text="")

    def get_file_content(self, file_path):

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        except UnicodeDecodeError:
            CTkMessagebox(
                title="Atenção!",
                message="Não foi possível ler o conteúdo do arquivo (erro de codificação)!",
                icon="warning",
            )
            return None

        except FileNotFoundError:
            CTkMessagebox(
                title="Info!",
                message="Arquivo não encontrado!",
                icon="info",
            )
            return None

        except Exception:
            CTkMessagebox(
                title="Atenção!",
                message="Erro ao ler o conteúdo do arquivo!",
                icon="warning",
            )
            return None

    def get_data(self):
        data = self.gui.text_entry.get()

        if not data:
            CTkMessagebox(
                title="Info!",
                message="Não deixe o campo em branco!",
                icon="info",
            )
            return None

        elif os.path.isfile(data):
            file_content = self.get_file_content(data)

            data = file_content

        return data

    def save_code(self):
        if not self.img:
            CTkMessagebox(
                title="Info!",
                message="Nenhum QR code para salvar!",
                icon="info",
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Imagens PNG", "*.png"), ("Todos os arquivos", "*.*")],
        )

        if file_path:
            self.img.save(file_path)
