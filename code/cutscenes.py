from settings import *
from os.path import join
from sprites import Sprite
from dialog import DialogTree

CAR_POSITIONS = {"start": (1440, WINDOW_HEIGHT/2), "end": (1440, 6400-(3*WINDOW_HEIGHT/2))}
LOGO_POSITION = (200, 100)
PROFESSOR_PATHING = {}

class TitleIntro:
    def __init__(self, all_sprites, display_surf, font):
        self.all_sprites = all_sprites
        self.display_surf = display_surf
        self.car = Car(CAR_POSITIONS["start"], self.all_sprites)
        self.logo = Logo(LOGO_POSITION, self.display_surf, self.all_sprites)  # Note: not part of all_sprites
        self.font = font
        self.start_text = self.font.render("Press any button to START", True, COLOURS["white"])
        self.start_text_rect = self.start_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/1.3))
        self.text_alpha = 255
        self.logo_alpha = 255
        self.fading = False

    def update(self, dt):
        self.all_sprites.update(dt)
        self.handle_event()
        if self.fading:
            self.fade_out()

    def draw(self):
        self.all_sprites.draw(self.car.rect.center)
        self.logo.draw(self.display_surf, self.logo_alpha)
        start_text_surface = self.start_text.copy()
        start_text_surface.set_alpha(self.text_alpha)
        self.display_surf.blit(start_text_surface, self.start_text_rect)

    def fade_out(self):
        fade_speed = 5
        self.text_alpha -= fade_speed
        self.logo_alpha -= fade_speed
        if self.text_alpha <= 0:
            self.text_alpha = 0
        if self.logo_alpha <= 0:
            self.logo_alpha = 0
            self.fading = False
        self.fade_surface.set_alpha(self.text_alpha)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.fading = True
                self.fade_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
                self.fade_surface.fill(COLOURS["black"])
                self.fade_surface.set_alpha(self.text_alpha)

class Car(pygame.sprite.Sprite):
    def __init__(self, pos, all_sprites):
        super().__init__(all_sprites)
        self.image = pygame.image.load(join('..', 'graphics', 'objects', 'orange_car.png'))
        self.rect = self.image.get_frect(topleft = (pos[0]-self.image.get_width()/2, pos[1]))
        self.speed = 400
        self.y_sort = self.rect.centery

    def update(self, dt):
        self.y_sort = self.rect.centery
        self.rect.y += self.speed * dt
        if self.rect.y > CAR_POSITIONS["end"][1]:
            self.rect.y = CAR_POSITIONS["start"][1]

class Logo(pygame.sprite.Sprite):
    def __init__(self, pos, display_surf, all_sprites):
        self.image = pygame.transform.scale(pygame.image.load(join('..', 'graphics', 'other', 'logo.png')), (WINDOW_WIDTH*0.7, WINDOW_HEIGHT*0.6))
        self.rect = self.image.get_frect(topleft = pos)
        self.display_surface = display_surf

    def update(self, dt):
        pass

    def draw(self, display_surface, alpha):
        temp_image = self.image.copy()
        temp_image.set_alpha(alpha)
        display_surface.blit(temp_image, self.rect)

class Classroom:
    def __init__(self, all_sprites, display_surf):
        self.all_sprites = all_sprites
        self.display_surf = display_surf
        Professor()

class Professor(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 30