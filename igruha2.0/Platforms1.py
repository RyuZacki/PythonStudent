
from pygame.sprite import Sprite
from pygame.image import load

class GameObject(Sprite):
    def __init__(self, x, y, img):
        Sprite.__init__(self)
        self.image = load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
