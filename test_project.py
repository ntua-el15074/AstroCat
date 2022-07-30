from project import draw_window, aura, rainbow_dash
import pygame
import random



WIDTH = 2400
HEIGHT = 1400
FPS = 60
SPEED = 5

POSX = 1000
POSY = 550

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("space.png")
pygame.display.set_caption("Pixie the AstroCat")
pygame.mixer.init()
meow = pygame.mixer.Sound("Cute-cat-meow-sound.mp3")


PARTICLE_EVENT = pygame.USEREVENT + 1
PARTICLE_EVENT2 = pygame.USEREVENT + 2
pygame.time.set_timer(PARTICLE_EVENT, 100)
pygame.time.set_timer(PARTICLE_EVENT2, 30)
PART_RADIUS = 10
PART_WIDTH = 25


class Cat:

    def __init__(self, POSX, POSY):
        self.CAT_WIDTH = 300
        self.CAT_HEIGHT = 300
        self.POSX = POSX
        self.POSY = POSY
        self.CAT_IMAGE = pygame.image.load("84774-square-art-pixel-rectangle-cat-hd-image-free-png.png")
        self.CAT = pygame.transform.scale(self.CAT_IMAGE, (self.CAT_WIDTH, self.CAT_HEIGHT))


    def rect_cat(self):
        return pygame.Rect(self.POSX, self.POSY, self.CAT_WIDTH, self.CAT_HEIGHT)


    def draw_cat(self):
        return WIN.blit(self.CAT, (self.POSX, self.POSY))


    def cat_position(self):
        return self.POSX + self.CAT_WIDTH/2 - 10, self.POSY + self.CAT_HEIGHT/2


    def cat_movement(self, command):
        if command[pygame.K_UP] and self.POSY >= 0:
            self.POSY -= SPEED
        if command[pygame.K_DOWN] and self.POSY <= 1100:
            self.POSY += SPEED
        if command[pygame.K_LEFT] and self.POSX >= 0:
            self.POSX -= SPEED
        if command[pygame.K_RIGHT] and self.POSX <= 2100:
            self.POSX += SPEED


    def cat_meow(self, command):
        if command[pygame.K_m]:
            meow.play()


class Particle1:

    def __init__(self):
        self.particles = []


    def emit(self):
        if self.particles:
            self.delete_particle()
            for particle in self.particles:
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(WIN, WHITE, particle[0], int(particle[1]))


    def add_particle(self, cat1):
        pPOSX, pPOSY = cat1.cat_position()
        radius = PART_RADIUS
        direction_x = random.randint(-5, 5)
        direction_y = random.randint(-5, 5)
        particle_circle = [[pPOSX, pPOSY], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)


    def delete_particle(self):
        particle_copy = [ particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy


class ParticleNyan:

    def __init__(self, PART_WIDTH):
        self.particles = []
        self.size = PART_WIDTH


    def emit(self, speed):
        if self.particles:
            self.delete_particle()
            for particle in self.particles:
                particle[0][1] += speed
                pygame.draw.rect(WIN, particle[1], particle[0])


    def add_particle(self, offset1, offset2, color, cat1):
        pPOSX, pPOSY = cat1.cat_position()
        pPOSX += offset1
        pPOSY += offset2
        particle_rect = [pPOSX, pPOSY, self.size, self.size]
        self.particles.append((particle_rect, color))


    def delete_particle(self):
        particle_copy = [ particle for particle in self.particles if particle[0][0] > 0]
        self.particles = particle_copy



def test_draw_window():
    cat1 = Cat(POSX, POSY)
    particle1 = Particle1()
    particle2 = ParticleNyan(PART_WIDTH)
    draw_window(cat1, particle1, particle2)

def test_aura():
    cat1 = Cat(POSX, POSY)
    particle1 = Particle1()
    aura(cat1, particle1)

def test_rainbow_dash():
    cat1 = Cat(POSX, POSY)
    particle2 = ParticleNyan(PART_WIDTH)
    command = pygame.key.get_pressed()
    rainbow_dash(cat1, particle2, command)

