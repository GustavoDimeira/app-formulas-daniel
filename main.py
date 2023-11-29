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
        self.fourth_section_label = ttk.Frame(root)
        self.tifth_section_label = ttk.Frame(root)
        self.sixth_section_label = ttk.Frame(root)

        self.set_inicial_state()

    def render_first(self):
        self.first_section_label.pack()
        self.second_section_label.pack_forget()
        self.third_section_label.pack_forget()
        self.fourth_section_label.pack_forget()
        self.tifth_section_label.pack_forget()
        self.tifth_section_label.pack_forget()
        self.sixth_section_label.pack_forget()

    def render_second(self):
        self.first_section_label.pack_forget()
        self.second_section_label.pack()
        self.third_section_label.pack_forget()
        self.fourth_section_label.pack_forget()
        self.tifth_section_label.pack_forget()
        self.sixth_section_label.pack_forget()

    def render_third(self):
        self.first_section_label.pack_forget()
        self.second_section_label.pack_forget()
        self.third_section_label.pack()
        self.fourth_section_label.pack_forget()
        self.tifth_section_label.pack_forget()
        self.sixth_section_label.pack_forget()

    def render_fourth(self):
        self.first_section_label.pack_forget()
        self.second_section_label.pack_forget()
        self.third_section_label.pack_forget()
        self.fourth_section_label.pack()
        self.tifth_section_label.pack_forget()
        self.sixth_section_label.pack_forget()

    def render_fifth(self):
        self.first_section_label.pack_forget()
        self.second_section_label.pack_forget()
        self.third_section_label.pack_forget()
        self.fourth_section_label.pack_forget()
        self.tifth_section_label.pack()
        self.sixth_section_label.pack_forget()

    def render_sixth(self):
        self.first_section_label.pack_forget()
        self.second_section_label.pack_forget()
        self.third_section_label.pack_forget()
        self.fourth_section_label.pack_forget()
        self.tifth_section_label.pack_forget()
        self.sixth_section_label.pack()

    def set_inicial_state(self):
        self.root.title("Formulas Daniel")
        self.root.config(menu = self.main_menu)

        self.main_menu.add_command(label='Primeira Parte', command=self.render_first)
        self.main_menu.add_command(label='Segunda Parte', command=self.render_second)
        self.main_menu.add_command(label='Terceira Parte', command=self.render_third)
        self.main_menu.add_command(label='Correias', command=self.render_fourth)
        self.main_menu.add_command(label='Correias Planas', command=self.render_fifth)
        self.main_menu.add_command(label='Correntes', command=self.render_sixth)

        create_section(self.first_section_label, "section_1")
        create_section(self.second_section_label, "section_2")
        create_section(self.third_section_label, "section_3")
        create_section(self.fourth_section_label, "section_4")
        create_section(self.tifth_section_label, "section_5")
        create_section(self.sixth_section_label, "section_6")


if __name__ == "__main__":
    root = tk.Tk()
    app = Main_app(root)
    root.mainloop()
