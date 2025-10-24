import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from image_panel import ImagePanel
from vram import VRAM


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.image_panel = None
        self.vram = None
        self.initialize()

        # Setup initial VRAM
        self.vram = VRAM(10, 10)
        self.vram.set_pixel(2, 2, 255, 0, 0)
        self.vram.set_pixel(7, 7, 0, 255, 0)
        self.vram.set_pixel(2, 7, 0, 0, 255)
        self.vram.set_pixel(7, 2, 255, 255, 255)

        # wait until the window is drawn before updating image
        self.after(100, lambda: self.image_panel.set_image(self.vram.get_image()))

    def initialize(self):
        self.master.title("Raster Graphics")
        self.master.geometry("1004x705")
        self.master.resizable(False, False)

        # Image panel
        self.image_panel = ImagePanel(self, width=970, height=600)
        self.image_panel.place(x=10, y=60)

        # Buttons
        btn_save = tk.Button(self, text="Save as PNG", command=self.save_image_as_png)
        btn_save.place(x=10, y=10, width=120, height=30)

        btn_load = tk.Button(self, text="Load Image", command=self.open_image)
        btn_load.place(x=150, y=10, width=120, height=30)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Load Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if not file_path:
            return

        try:
            img = Image.open(file_path)
            self.image_panel.set_image(img)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image: {e}")

    def save_image_as_png(self):
        if not self.image_panel.get_image():
            messagebox.showwarning("Warning", "No image to save!")
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Image as PNG",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )
        if not file_path:
            return

        try:
            self.image_panel.get_image().save(file_path, "PNG")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to save image: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(master=root)
    app.mainloop()
