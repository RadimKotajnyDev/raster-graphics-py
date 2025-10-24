import tkinter as tk
from PIL import ImageTk, Image


class ImagePanel(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg="#B3BBCB", **kwargs)
        self.image = None
        self.tk_image = None

    def set_image(self, image: Image.Image):
        self.image = image
        self.repaint()

    def get_image(self):
        return self.image

    def repaint(self):
        self.delete("all")

        if self.image:
            panel_width = self.winfo_width()
            panel_height = self.winfo_height()

            img_w, img_h = self.image.size
            ratio = min(panel_width / img_w, panel_height / img_h)
            new_w, new_h = int(img_w * ratio), int(img_h * ratio)

            resized_img = self.image.resize((new_w, new_h), Image.NEAREST)
            self.tk_image = ImageTk.PhotoImage(resized_img)
            self.create_image(
                (panel_width - new_w) // 2,
                (panel_height - new_h) // 2,
                anchor="nw",
                image=self.tk_image
            )
