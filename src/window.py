from tkinter import *
from tkinter import ttk
from typing import Type

from src.line import Line


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = 'Maze Solver'
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False


    def draw_line(self, line: Type[Line], fill_color: str) -> None:
        line.draw(self.canvas, fill_color)
        

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        

    def close(self):
        self.running = False