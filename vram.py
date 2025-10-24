from PIL import Image


class VRAM:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.raw_data = [[(0, 0, 0, 255) for _ in range(width)] for _ in range(height)]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_pixel(self, x: int, y: int):
        return self.raw_data[y][x]

    def set_pixel(self, x: int, y: int, r: int, g: int, b: int):
        self.raw_data[y][x] = (r, g, b, 255)

    def get_image(self):
        img = Image.new("RGBA", (self.width, self.height))
        pixels = [self.raw_data[y][x] for y in range(self.height) for x in range(self.width)]
        img.putdata(pixels)
        return img
