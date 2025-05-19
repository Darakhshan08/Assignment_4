import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.cells = []
        self.create_grid()

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")
        self.canvas.bind("<Motion>", self.on_mouse_move)

    def create_grid(self):
        for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for x in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="blue")
                self.cells.append(rect)

    def on_mouse_move(self, event):
        # Move eraser with the mouse
        self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)

        # Erase overlapping blue cells
        eraser_coords = self.canvas.bbox(self.eraser)
        overlapping = self.canvas.find_overlapping(*eraser_coords)

        for item in overlapping:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill="white")

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    app = EraserApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
