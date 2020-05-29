
from pygame.sprite import Sprite, collide_rect
from pygame import Surface
#import pyganim

MOVE_SPEED = 7
JUMP_POWER = 10

GRAVITY = 0.4

animCount = 0

class Player(Sprite):
    def __init__(self, x, y, img):
        Sprite.__init__(self)
        self.image = img
        self.xvel = 0
        self.yvel = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onGround = False

        self.image.set_colorkey((0, 0, 0))

        #self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        #self.boltAnimStay.play()

    def update(self, left, right, up, objects):
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if not (left or right):
            self.xvel = 0
            # if not up:
            #     self.image.fill((0, 0, 0))
            #     self.boltAnimStay.blit(self.image, (0, 0))

        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, objects)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, objects)

    def collide(self, xvel, yvel, objects):
        for obj in objects:
            if collide_rect(self, obj):
                if xvel > 0:
                    self.rect.right = obj.rect.left
                if xvel < 0:
                    self.rect.left = obj.rect.right
                if yvel > 0:
                    self.rect.bottom = obj.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = obj.rect.bottom
                    self.yvel = 0

