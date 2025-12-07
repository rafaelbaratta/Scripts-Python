from core import Core
from gui import Gui


def main():
    app = Gui()
    core = Core(app)

    try:
        app.mainloop()
    except KeyboardInterrupt:
        print("Programa 'Auto Clicker' Encerrado")


if __name__ == "__main__":
    main()
