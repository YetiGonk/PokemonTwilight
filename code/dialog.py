from settings import *
from os.path import join
from timer import Timer

class DialogTree:
    def __init__(self, all_sprites, font, display_surf, end_dialog, character=None, narration=None, non_character=None):
        if character:
            self.character = character
        self.all_sprites = all_sprites
        self.end_dialog = end_dialog

        self.font = font
        self.display_surf = display_surf
        if character:
            self.dialog = character.get_dialog()
            self.portrait = character.portrait
        elif narration:
            self.dialog = narration
            self.portrait = None
        elif non_character:
            self.portrait = non_character['portrait']
            self.dialog = non_character['dialog']
        else:
            raise ValueError("Character, narration or non_character have been specified.")
        self.dialog_num = len(self.dialog)
        self.dialog_index = 0

        self.current_dialog = DialogSprite(self.dialog[self.dialog_index], self.all_sprites, self.font, self.display_surf, portrait=self.portrait)
        self.dialog_timer = Timer(100, autostart = True)

    def input(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE] and not self.dialog_timer.active:
            self.current_dialog.kill()
            self.dialog_index += 1
            if self.dialog_index < self.dialog_num:
                self.current_dialog = DialogSprite(self.dialog[self.dialog_index], self.all_sprites, self.font, self.display_surf, portrait=self.portrait)
                self.dialog_timer.activate()
            else:
                if self.dialog[self.dialog_index-1] == "So don't rush it.":
                    self.end_dialog(result = 'starter')
                else:
                    self.end_dialog()

    def update(self):
        self.dialog_timer.update()
        self.input()

class DialogSprite(pygame.sprite.Sprite):
    def __init__(self, message, all_sprites, font, display_surf, portrait = None):
        super().__init__(all_sprites)
        self.z = WORLD_LAYERS['top']
        self.display_surf = display_surf

        self.portrait = portrait

        self.text_box_surf = pygame.image.load(join('..', 'graphics', 'other', 'text box.png'))

        # Scale portrait
        if self.portrait:
            scale_factor = 8
            portrait_width = int(self.portrait.get_width() * scale_factor)
            portrait_height = int(self.portrait.get_height() * scale_factor)
            self.portrait_image = pygame.transform.scale(self.portrait, (portrait_width, portrait_height))

        # Scale text box
        scale_factor = 0.95
        text_box_width = int(display_surf.get_width() * scale_factor)
        text_box_height = int(self.text_box_surf.get_height() * (text_box_width / self.text_box_surf.get_width()))
        self.text_image = pygame.transform.scale(self.text_box_surf, (text_box_width, text_box_height))

        # Render text
        text_surf = font.render(message, True, COLOURS['black'])

        # Render text box
        text_rect = text_surf.get_rect(topleft = (65, 20))

        # Blit the text onto the text box
        self.text_image.blit(text_surf, text_rect)

        # Position the portrait on the right side of the screen
        if portrait:
            self.portrait_rect = self.portrait_image.get_frect(bottomright = (display_surf.get_width()+64, display_surf.get_height()))

        # Position the text box at the bottom of the screen
        self.text_rect = self.text_image.get_frect(midbottom = (display_surf.get_width() // 2, display_surf.get_height()-20))

    def draw(self):
        # Display portrait and text on screen
        self.display_surf.blit(self.text_image, self.text_rect)
        if self.portrait:
            self.display_surf.blit(self.portrait_image, self.portrait_rect)
