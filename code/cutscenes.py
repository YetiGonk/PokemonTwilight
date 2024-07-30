from settings import *
from support import import_image
from os.path import join
from sprites import Sprite
from dialog import DialogTree
from game_data import NARRATOR_DATA, TRAINER_DATA
from timer import Timer
from entities import Character

CAR_POSITIONS = {"start": (1440, WINDOW_HEIGHT/2), "end": (1440, 6400-(3*WINDOW_HEIGHT/2))}
LOGO_POSITION = (200, 100)
PROFESSOR_PATHING = {'start':(176, 288), 'end': (176, 384)}
CLASSROOM_POSITION = (320, 320)

class TitleIntro:
    def __init__(self, all_sprites, display_surf, font, end_cutscene):
        self.all_sprites = all_sprites
        self.display_surf = display_surf
        self.car = Car(CAR_POSITIONS["start"], self.all_sprites)
        self.logo = Logo(LOGO_POSITION, self.display_surf, self.all_sprites)
        self.font = font
        self.start_text = self.font.render("Press any button to START", True, COLOURS["white"])
        self.start_text_rect = self.start_text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.3))
        self.text_alpha = 255
        self.logo_alpha = 255
        self.fading = False
        self.title_gone = False
        self.end_cutscene = end_cutscene

    def update(self, dt):
        self.all_sprites.update(dt)
        self.input()
        if self.fading:
            self.fade_out()
        if self.title_gone:
            self.end_cutscene()
            self.title_gone = False

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
        if self.text_alpha == 0 and self.logo_alpha == 0:
            self.title_gone = True

    def input(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE]:
            self.fading = True

class DadIntro:
    def __init__(self, all_sprites, display_surf, font, end_cutscene, end_dialog):
        self.all_sprites = all_sprites
        self.display_surf = display_surf
        self.font = font
        self.end_cutscene = end_cutscene
        self.end_dialog = end_dialog
        self.car = Car(CAR_POSITIONS["start"], self.all_sprites)
        self.dad_dialog = TRAINER_DATA['dad intro']['dialog']['default']
        self.narrator_dialog = NARRATOR_DATA['forest_road']
        self.dialog_active = False
        self.dialog_started = False
        self.dad_portrait = import_image(join('..', 'graphics', 'characters', 'portrait', 'Dad'))
        self.dad_obj = {'portrait': self.dad_portrait, 'dialog': self.dad_dialog}
        self.predialog_timer = Timer(1500, autostart=True)
        self.dialog_tree = None
        self.dad_dialog_active = False

    def dialog_end_callback(self):
        if self.dad_dialog_active:
            self.dad_dialog_active = False
            self.dialog_tree = DialogTree(self.all_sprites, self.font, self.display_surf, self.dialog_end_callback, narration=self.narrator_dialog)
        else:
            self.end_cutscene()

    def update(self, dt):
        self.all_sprites.update(dt)
        if self.predialog_timer.active:
            self.predialog_timer.update()
        if not self.predialog_timer.active and not self.dialog_tree:
            self.dialog_tree = DialogTree(self.all_sprites, self.font, self.display_surf, self.dialog_end_callback, non_character=self.dad_obj)
            self.dad_dialog_active = True
        if self.dialog_tree:
            self.dialog_tree.update()

    def draw(self):
        self.all_sprites.draw(self.car.rect.center)
        if self.dialog_tree:
            self.dialog_tree.current_dialog.draw()

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

class ClassroomIntro:
    def __init__(self, all_sprites, display_surf, font, end_cutscene, end_dialog, prof_frames):
        self.all_sprites = all_sprites
        self.display_surf = display_surf
        self.font = font
        self.end_cutscene = end_cutscene
        self.end_dialog = end_dialog
        self.prof_frames = prof_frames
        self.dialog_tree = None
        self.entry_timer = Timer(1500, autostart=True)
        self.prof_dialog_active = False
        self.prof_portrait = import_image(join('..', 'graphics', 'characters', 'portrait', 'Drayden'))
        self.prof_dialog_1 = TRAINER_DATA['professor intro']['dialog']['default']
        self.prof_obj_1 = {'portrait': self.prof_portrait, 'dialog': self.prof_dialog_1}
        self.prof_dialog_2 = TRAINER_DATA['professor intro']['dialog']['default 1']
        self.prof_obj_2 = {'portrait': self.prof_portrait, 'dialog': self.prof_dialog_2}
        self.prof_dialog_3 = TRAINER_DATA['professor intro']['dialog']['default 2']
        self.prof_obj_3 = {'portrait': self.prof_portrait, 'dialog': self.prof_dialog_3}
        self.narrator_dialog = NARRATOR_DATA['classroom']
        self.moving = False
        self.has_moved = False
        self.has_spoken_after_move = False
        self.has_spoken_after_narration = False
        self.narrator_has_spoken = False
        self.professor = Character(PROFESSOR_PATHING['start'], self.prof_frames, self.all_sprites, 'down', None, None, None, None, None, None)

    def dialog_end_callback(self, result = None):
        if self.prof_dialog_active and not self.has_spoken_after_narration:
            self.prof_dialog_active = False
            if not self.moving:
                self.moving = True
            self.dialog_tree = None
        if self.has_spoken_after_narration:
            self.dialog_tree = None
            self.end_cutscene()
        else:
            self.dialog_tree = None

    def update(self, dt):
        self.all_sprites.update(dt)
        if self.entry_timer.active:
            self.entry_timer.update()
        if self.dialog_tree:
            self.dialog_tree.update()

        # Initial dialog
        if not self.entry_timer.active and not self.dialog_tree and not self.moving and not self.has_moved:
            self.dialog_tree = DialogTree(self.all_sprites, self.font, self.display_surf, self.dialog_end_callback, non_character=self.prof_obj_1)
            self.prof_dialog_active = True

        # Moving the professor
        if self.moving:
            if self.professor.rect.bottom < PROFESSOR_PATHING['end'][1]:
                self.professor.direction = vector(0, 0.6)
                self.professor.rect.center += self.professor.direction * self.professor.speed * dt
                self.professor.animate(dt)
            else:
                self.moving = False
                self.has_moved = True
                self.professor.direction = vector()
                self.professor.has_moved = True
                self.professor.facing_direction = 'right'

        # Second dialog
        if self.has_moved and not self.prof_dialog_active and not self.moving and not self.has_spoken_after_move:
            self.dialog_tree = DialogTree(self.all_sprites, self.font, self.display_surf, self.dialog_end_callback, non_character=self.prof_obj_2)
            self.prof_dialog_active = True
            self.has_spoken_after_move = True

        # Narrator dialog
        if self.has_spoken_after_move and not self.prof_dialog_active and not self.narrator_has_spoken:
            self.dialog_tree = DialogTree(self.all_sprites, self.font, self.display_surf, self.dialog_end_callback, narration=self.narrator_dialog)
            self.narrator_has_spoken = True
            self.prof_dialog_active = True

        # Final professor dialog
        if self.narrator_has_spoken and not self.prof_dialog_active and not self.dialog_tree:
            self.dialog_tree = DialogTree(self.all_sprites, self.font, self.display_surf, self.dialog_end_callback, non_character=self.prof_obj_3)
            self.prof_dialog_active = True
            self.has_spoken_after_narration = True

    def draw(self):
        self.all_sprites.draw(CLASSROOM_POSITION)
        if self.dialog_tree:
            self.dialog_tree.current_dialog.draw()