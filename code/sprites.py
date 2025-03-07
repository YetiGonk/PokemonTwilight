from settings import *
from support import *
import game_data

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = WORLD_LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.z = z
        self.y_sort = self.rect.centery
        self.hitbox = self.rect.copy()

class PokemonPatchSprite(Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups, z = WORLD_LAYERS['main'])
        self.y_sort -= 40

class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups, z = WORLD_LAYERS['main']):
        self.frame_index, self.frames = 0, frames
        super().__init__(pos, frames[self.frame_index], groups, z)

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        self.image = self.frames[int(self.frame_index % len(self.frames))]

    def update(self, dt):
        self.animate(dt)

class BorderSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()

class CollidableSprite(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy().inflate(0,-self.rect.height/2)
        self.hitbox.centery -= self.rect.height/4

class TransitionSprite(Sprite):
    def __init__(self, pos, size, target, groups):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.target = target

class PokemonSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups, pokemon, entity):
        self.entity = entity
        self.pokemon = pokemon

        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(midbottom = pos)

class PokemonStatsSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, pokemon, entity, groups, fonts, status_icons):
        super().__init__(groups)
        self.size = size
        self.padding = 30
        self.fonts = fonts
        self.pokemon = pokemon
        self.entity = entity
        self.pokeball_surf = import_image(join('..', 'graphics', 'other', 'pokeball'))
        self.status_icons = status_icons

        self.base_image = pygame.Surface(self.size + vector(0, 100))
        self.image = pygame.Surface(self.size + vector(self.padding, self.padding))
        self.rect = self.image.get_frect(topleft = pos - vector(-self.padding/2, -self.padding/2))
        
    def update(self, _):
        self.image.fill(COLOURS['grey'])

        box = pygame.Surface(self.size)
        box.fill(COLOURS['dark-grey'])
        self.image.blit(box, vector(self.padding/2, self.padding/2))

        # pokemon name
        name_surf = self.fonts['bold'].render(self.pokemon.name.capitalize(), False, COLOURS['white'])
        self.image.blit(name_surf, vector(self.padding, self.padding))

        # pokemon level
        level_surf = self.fonts['bold'].render(f'Lv.{self.pokemon.level}', False, COLOURS['white'])
        self.image.blit(level_surf, vector(self.rect.width - level_surf.get_width() - self.padding, self.padding))

        health_bar_height = 20
        xp_bar_height = 12
        health_xp_gap = 8

        # health text
        health_text_surf = self.fonts['bold'].render(f'HP', False, COLOURS['white'])
        self.image.blit(health_text_surf, vector(self.padding, name_surf.get_height() + self.padding*3/2))   

        # health bar
        health_bar_surf_bg = pygame.Surface(((self.rect.width - self.padding*3 - health_text_surf.get_width())*0.8, health_text_surf.get_height()))
        health_bar_surf_bg.fill(COLOURS['grey'])
        ratio = self.pokemon.current_hp/self.pokemon.max_hp
        health_bar_surf = pygame.Surface(((self.rect.width - self.padding*3 - health_text_surf.get_width())*ratio*0.8, health_bar_height))
        if ratio < 0.2:
            health_bar_surf.fill(COLOURS['red'])
        elif ratio >= 0.2 and ratio < 0.5:
            health_bar_surf.fill(COLOURS['amber'])
        else:
            health_bar_surf.fill(COLOURS['green'])
        self.image.blit(health_bar_surf_bg, vector(health_text_surf.get_width() + self.padding*3/2, name_surf.get_height() + self.padding*3/2))
        self.image.blit(health_bar_surf, vector(health_text_surf.get_width() + self.padding*3/2, name_surf.get_height() + self.padding*3/2))

        # status condition
        if self.pokemon.status_effect:
            status_surf = self.status_icons[self.pokemon.status_effect]
            status_surf = pygame.transform.scale(status_surf, ((name_surf.get_height()/status_surf.get_height() * status_surf.get_width())*1.5, name_surf.get_height()*1.5))
            self.image.blit(status_surf, vector(self.padding, self.padding) + vector(name_surf.get_width(), 0) + vector(self.padding*1/2, -self.padding*0.15))

        mods_topright_pos = vector(0, self.image.get_height()) + vector(self.padding/2, -self.padding*3/2)

        for stat in list(self.pokemon.stat_mods.items()):
            stat_name = stat[0]
            stat_value = stat[1]
            if stat_value != 0:
                text_surf = self.fonts['small'].render(f"{stat_name}" + (" +" if stat_value > 0 else " ") + f"{stat_value}", False, COLOURS['white'])
                text_box_surf = pygame.Surface((text_surf.get_width()+self.padding/2, text_surf.get_height()+self.padding/2))
                text_box_surf.fill(COLOURS['light-grey'])
                self.image.blit(text_box_surf, mods_topright_pos + vector(self.padding/2, 0))
                self.image.blit(text_surf, mods_topright_pos + vector(self.padding*3/4, self.padding*1/4))
                mods_topright_pos += vector(self.padding/2, 0) + vector(text_box_surf.get_width(), 0)

        if self.entity == 'player':
            # health number
            health_number_surf = self.fonts['large'].render(f'{self.pokemon.current_hp}/{self.pokemon.max_hp}', False, COLOURS['white'])
            self.image.blit(health_number_surf, vector(health_text_surf.get_width() + self.padding*2 + health_bar_surf_bg.get_width(), name_surf.get_height() + self.padding*1.35))
            
            # xp text
            xp_text_surf = self.fonts['bold'].render(f'XP', False, COLOURS['white'])
            self.image.blit(xp_text_surf, vector(self.padding, name_surf.get_height() + self.padding*3/2 + health_text_surf.get_height() + health_xp_gap))

            # xp bar
            xp_bar_surf_bg = pygame.Surface(((self.rect.width - self.padding*3 - health_text_surf.get_width())*0.8, health_text_surf.get_height()))
            xp_bar_surf_bg.fill(COLOURS['grey'])
            ratio = self.pokemon.current_xp/self.pokemon.level_xp
            xp_bar_surf = pygame.Surface(((self.rect.width - self.padding*3 - health_text_surf.get_width())*ratio*0.8, health_bar_height))
            xp_bar_surf.fill(COLOURS['blue'])
            self.image.blit(xp_bar_surf_bg, vector(health_text_surf.get_width() + self.padding*3/2, name_surf.get_height() + self.padding*3/2 + health_text_surf.get_height() + health_xp_gap))
            self.image.blit(xp_bar_surf, vector(health_text_surf.get_width() + self.padding*3/2, name_surf.get_height() + self.padding*3/2 + health_text_surf.get_height() + health_xp_gap))

        if self.entity == 'opponent':
            for index in range(6):
                if self.pokemon.status_effect or self.pokemon.fainted:
                    if self.pokemon.status_effect == 'paralysed':
                        self.pokeball_surf.copy().fill(COLOURS['amber'])
                    if self.pokemon.status_effect == 'frozen':
                        self.pokeball_surf.copy().fill(COLOURS['blue'])
                    if self.pokemon.status_effect == 'asleep':
                        self.pokeball_surf.copy()