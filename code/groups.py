from settings import *
from support import import_image
from entities import Entity
from dialog import DialogSprite

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()
        self.shadow_surf = import_image('..', 'graphics', 'other', 'shadow')
    
    def draw(self, pos):
        self.offset.x = -(pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(pos[1] - WINDOW_HEIGHT / 2)
        
        for sprite in self:
            if not hasattr(sprite, 'z'):
                setattr(sprite, 'z', WORLD_LAYERS['main'])
        
        bg_sprites = [sprite for sprite in self if sprite.z < WORLD_LAYERS['main']]
        main_sprites = sorted(
            [sprite for sprite in self if sprite.z == WORLD_LAYERS['main']], key = lambda sprite: sprite.y_sort
        )
        fg_sprites = [sprite for sprite in self if sprite.z > WORLD_LAYERS['main']]
        
        for layer in (bg_sprites, main_sprites, fg_sprites):
            for sprite in layer:
                if isinstance(sprite, DialogSprite):
                    continue
                if isinstance(sprite, Entity):
                    self.display_surface.blit(self.shadow_surf, sprite.rect.bottomleft + self.offset + (19, -8))
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)