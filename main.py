import tkinter as tk
from tkinter import ttk
from tkinter import Menu

from utils import create_section

class Main_app:
    def __init__(self, root):
        self.root = root
        self.main_menu = Menu(self.root)

        self.first_section_label = ttk.Frame(root)
        self.second_section_label = ttk.Frame(root)
        self.third_section_label = ttk.Frame(root)

        self.set_inicial_state()

    def render_first(self):
        self.first_section_label.pack()
        self.second_section_label.pack_forget()
        self.third_section_label.pack_forget()

    def render_second(self):
        self.first_section_label.pack_forget()
        self.second_section_label.pack()
        self.third_section_label.pack_forget()

    def render_third(self):
        self.first_section_label.pack_forget()
        self.second_section_label.pack_forget()
        self.third_section_label.pack()

    def set_inicial_state(self):
        self.root.title("Formulas Daniel")
        self.root.config(menu = self.main_menu)

        self.main_menu.add_command(label='Primeira Parte', command=self.render_first)
        self.main_menu.add_command(label='Segunda Parte', command=self.render_second)
        self.main_menu.add_command(label='Terceira Parte', command=self.render_third)

        create_section(self.first_section_label, "section_1")
        create_section(self.second_section_label, "section_2")
        create_section(self.third_section_label, "section_3")


if __name__ == "__main__":
    root = tk.Tk()
    app = Main_app(root)
    root.mainloop()
