import os
import shutil

from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog


class Core:

    def __init__(self, gui):
        self.gui = gui

        self.EXTENSIONS = {
            "Documents": [
                "txt",
                "docx",
                "doc",
                "pdf",
                "ppt",
                "pptx",
                "odt",
                "ods",
                "odp",
                "html",
                "htm",
            ],
            "Images": [
                "png",
                "jpg",
                "jpeg",
                "svg",
                "gif",
                "bmp",
                "ico",
                "icns",
                "webp",
                "tiff",
                "psd",
            ],
            "Audios": [
                "mp3",
                "ogg",
                "wma",
                "wav",
                "aac",
                "flac",
                "aif",
                "m3u",
                "pls",
                "mid",
            ],
            "Videos": ["mp4", "avi", "mkv", "mov", "wmv", "m4v", "webm", "flv"],
            "Executables": [
                "exe",
                "bat",
                "cmd",
                "msi",
                "sh",
                "bin",
                "run",
                "app",
                "dll",
            ],
            "Compacted": [
                "jar",
                "rar",
                "zip",
                "7z",
                "tar",
                "gz",
                "iso",
                "ova",
                "dmg",
                "pkg",
            ],
            "Data": [
                "csv",
                "json",
                "xml",
                "tsv",
                "yaml",
                "yml",
                "sql",
                "db",
                "sqlite",
                "mdb",
                "dta",
                "sav",
                "xls",
                "xlsx",
            ],
            "Programming": [
                "js",
                "java",
                "c",
                "h",
                "cpp",
                "cs",
                "php",
                "py",
                "r",
                "go",
                "ru",
                "css",
                "kt",
                "cc",
                "cxx",
                "hpp",
                "pas",
            ],
        }

        self.gui.directory_button.configure(command=self.get_path)
        self.gui.generate_button.configure(command=self.organize)

    def get_path(self):
        directory_path = filedialog.askdirectory()
        self.gui.text_entry.delete(0, "end")
        self.gui.text_entry.insert(0, directory_path)

    def organize(self):
        directory = self.get_directory()

        if not directory:
            return

        os.chdir(directory)

        selected_extensions = self.get_selected_checkboxes()

        if not selected_extensions:
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
            if not os.path.isfile(file):
                continue

            for key, values in selected_extensions.items():
                file_ext = os.path.splitext(file)[1][1:].lower()

                if file_ext and file_ext in values:
                    try:
                        os.mkdir(key)
                    except FileExistsError:
                        pass
                    if self.move_file(directory, file, f"{directory}/{key}"):
                        counter += 1
                    break

            else:
                try:
                    os.mkdir("Outros")
                except FileExistsError:
                    pass
                if self.move_file(directory, file, f"{directory}/Outros"):
                    counter += 1

        CTkMessagebox(
            title="Info!",
            message=f"{counter} dados organizados com sucesso!",
            icon="info",
        )
        return None

    def move_file(self, directory, file, destiny):
        file_destination = f"{destiny}/{file}"

        if os.path.exists(file_destination):
            file_name, file_ext = os.path.splitext(file)
            counter = 1

            while os.path.exists(f"{destiny}/{file_name}_{counter}{file_ext}"):
                counter += 1
            file_destination = f"{destiny}/{file_name}_{counter}{file_ext}"

        try:
            shutil.move(f"{directory}/{file}", file_destination)
            return True

        except PermissionError:
            CTkMessagebox(
                title="Info!",
                message=f"Você não tem permissão para mover o arquivo {file}!",
                icon="info",
            )
            return False

        except Exception:
            CTkMessagebox(
                title="Info!",
                message=f"Falha ao mover o arquivo {file}!",
                icon="info",
            )
            return False

    def get_directory(self):
        data = self.gui.text_entry.get()

        if not data:
            CTkMessagebox(
                title="Info!",
                message="Não deixe o campo em branco!",
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

    def get_selected_checkboxes(self):
        selected_extensions = dict()

        if self.gui.documents_checkbox.get():
            selected_extensions["Documentos"] = self.EXTENSIONS["Documents"]

        if self.gui.images_checkbox.get():
            selected_extensions["Imagens"] = self.EXTENSIONS["Images"]

        if self.gui.audios_checkbox.get():
            selected_extensions["Áudios"] = self.EXTENSIONS["Audios"]

        if self.gui.videos_checkbox.get():
            selected_extensions["Vídeos"] = self.EXTENSIONS["Videos"]

        if self.gui.binary_checkbox.get():
            selected_extensions["Executáveis"] = self.EXTENSIONS["Executables"]

        if self.gui.compacted_checkbox.get():
            selected_extensions["Compactados"] = self.EXTENSIONS["Compacted"]

        if self.gui.data_checkbox.get():
            selected_extensions["Dados"] = self.EXTENSIONS["Data"]

        if self.gui.programming_checkbox.get():
            selected_extensions["Códigos Fonte"] = self.EXTENSIONS["Programming"]

        if not selected_extensions:
            CTkMessagebox(
                title="Info!",
                message="Você deve selecionar, no mínimo, uma categoria!",
                icon="info",
            )
            return None

        return selected_extensions
