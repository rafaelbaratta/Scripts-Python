import threading
from time import sleep

from CTkMessagebox import CTkMessagebox
from pyautogui import click
from pynput import keyboard, mouse


class Core:

    def __init__(self, gui):
        self.gui = gui

        self.listener = None

        self.clicking = False
        self.fixed_clicking = False
        self.recording = False

        self.positions = []
        self.clicks_counter = 0

        self.position_key = keyboard.Key.f1
        self.clicker_key = keyboard.Key.f2
        self.fixed_clicker_key = keyboard.Key.f3

        self.gui.positions_start.configure(command=self.record_positions)
        self.gui.positions_end.configure(command=lambda: self.end_record_positions("click"))
        self.gui.reset_positions.configure(command=self.reset_positions)

        self.gui.start_button.configure(command=self.start_clicker)
        self.gui.finish_button.configure(command=self.finish_clicker)
        self.gui.reset_clicks.configure(command=self.reset_clicks)

        self.gui.fixed_clicker_start_button.configure(command=self.start_fixed_clicker)
        self.gui.fixed_clicker_finish_button.configure(command=self.finish_fixed_clicker)

        self.gui.speed_slider.configure(command=self.print_speed_value)

        self.gui.protocol("WM_DELETE_WINDOW", self.cleanup)

        self.key_listener_thread()

    def key_listener_thread(self):
        key_listener_thread = threading.Thread(target=lambda: keyboard.Listener(on_press=self.on_press).start())
        key_listener_thread.daemon = True
        key_listener_thread.start()

    def on_press(self, key):
        if key == self.position_key:
            if self.recording:
                self.end_record_positions("keyboard")
            else:
                self.record_positions()
        elif key == self.clicker_key:
            if self.clicking:
                self.finish_clicker()
            else:
                self.start_clicker()
        elif key == self.fixed_clicker_key:
            if self.fixed_clicking:
                self.finish_fixed_clicker()
            else:
                self.start_fixed_clicker()

    def record_positions(self):
        if self.clicking or self.fixed_clicking:
            return

        self.recording = True

        self.gui.positions_start.pack_forget()
        self.gui.positions_end.pack(side="left", padx=(70, 0))

        self.positions = []
        self.print_positions()

        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def end_record_positions(self, event):
        if self.clicking or self.fixed_clicking:
            return

        self.recording = False

        self.gui.positions_start.pack(side="left", padx=(70, 0))
        self.gui.positions_end.pack_forget()

        self.listener.stop()

        if event == "click" and self.positions:
            self.positions.pop()
            self.print_positions()

    def reset_positions(self):
        self.positions = []
        self.print_positions()

    def on_click(self, x, y, button, pressed):

        button_side = "left" if "left" in str(button) else "right"

        if pressed:
            self.positions.append((button_side, x, y))
            self.print_positions()

    def print_positions(self):
        self.gui.positions_counter.configure(text=f"Total de posições: {len(self.positions)}")

    def start_clicker(self):
        if self.recording or self.fixed_clicking:
            return

        if not self.positions:
            CTkMessagebox(
                title="Info!",
                message="Não há posições definidas para o Clicker funcionar!",
                icon="info",
            )
            return

        self.clicking = True

        self.gui.start_button.pack_forget()
        self.gui.finish_button.pack(side="left", padx=(70, 0))

        clicker_thread = threading.Thread(target=self.clicker)
        clicker_thread.daemon = True
        clicker_thread.start()

    def finish_clicker(self):
        if self.recording or self.fixed_clicking:
            return

        self.clicking = False

        self.gui.start_button.pack(side="left", padx=(70, 0))
        self.gui.finish_button.pack_forget()

    def clicker(self):
        delay = self.gui.speed_slider.get()

        while self.clicking:
            for button, x, y in self.positions:
                if not self.clicking:
                    break

                click(x, y, button=button)
                self.increase_clicks()
                sleep(delay)

    def increase_clicks(self):
        self.clicks_counter += 1
        self.gui.clicks_counter.configure(text=f"Total de cliques: {self.clicks_counter}")

    def reset_clicks(self):
        self.clicks_counter = 0
        self.gui.clicks_counter.configure(text=f"Total de cliques: {self.clicks_counter}")

    def print_speed_value(self, value):
        self.gui.speed_value.configure(text=f"Velocidade dos cliques: ({value:.3f})")

    def cleanup(self):
        self.clicking = False
        self.fixed_clicking = False
        self.recording = False

        if self.listener:
            self.listener.stop()

        self.gui.destroy()

    def start_fixed_clicker(self):
        if self.recording or self.clicking:
            return

        self.fixed_clicking = True

        self.gui.fixed_clicker_start_button.pack_forget()
        self.gui.fixed_clicker_finish_button.pack(pady=5)

        clicker_thread = threading.Thread(target=self.fixed_clicker)
        clicker_thread.daemon = True
        clicker_thread.start()

    def finish_fixed_clicker(self):
        if self.recording or self.clicking:
            return

        self.fixed_clicking = False

        self.gui.fixed_clicker_finish_button.pack_forget()
        self.gui.fixed_clicker_start_button.pack(pady=5)

    def fixed_clicker(self):
        with mouse.Controller() as mouse_controller:
            delay = self.gui.speed_slider.get()

            while self.fixed_clicking:
                if not self.fixed_clicking:
                    break

                mouse_controller.click(mouse.Button.left, 1)
                self.increase_clicks()
                sleep(delay)
