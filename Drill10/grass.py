from pico2d import load_image


class Grass:
    def __init__(self, height):
        self.image = load_image('grass.png')
        self.height = height

    def draw(self):
        self.image.draw(400, self.height)

    def update(self):
        pass
