from settings import *
from pokemon_data import POKEMON_DATA
import player_data

class StarterSelect:
    def __init__(self, display_surface, pokemon_graphics, fonts):
        self.display_surface = display_surface
        self.starter_surfs = {
            'grass': pokemon_graphics['rowlet_normal'],
            'fire': pokemon_graphics['vulpix_normal'],
            'water': pokemon_graphics['totodile_normal']
        }
        self.fonts = fonts

        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)

        self.confirm_menu = False

        self.index = None
        self.selected_index = 0

    def display_starter_menu(self):
        pass

    def display_confirm_menu(self):
        pass

    def input(self):
        pass

    def update(self, dt):
        self.input()
        self.display_surface.blit(self.tint_surf, (0,0))
        self.display_starter_menu()
        if self.confirm_menu:
            self.display_confirm_menu()
            