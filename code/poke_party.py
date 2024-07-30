from settings import *
from support import draw_bar
from player_data import 
from pokemon_data import POKEMON_DATA

class PokeParty:
    def __init__(self, fonts, pokemon_graphics, player_pokemon):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts
        self.battle_sprites = pokemon_graphics['battle_sprites']
        self.box_sprites = pokemon_graphics['box_sprites']

        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)

        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.6, WINDOW_HEIGHT*0.6).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        self.pokemon = player_pokemon

        self.selected_index = (0,0)
        self.index = (0,0)

    def display_party(self):
        #pokedex title
        title_text_surf = self.fonts['bold'].render("YOUR POKEMON", True, COLOURS['white'], COLOURS['dark-grey'])
        title_text_rect = title_text_surf.get_frect(bottomleft = self.main_rect.topleft + vector(15, -5))
        border_add = 6
        title_box_rect = pygame.FRect(title_text_rect.topleft + vector(-border_add * 1.75, -border_add * 1.75), (title_text_rect.width + border_add * 3.5, (title_text_rect.height + border_add * 4.5)))
        pygame.draw.rect(self.display_surface, COLOURS['navy'], title_box_rect, 6, 6, 6, 6, 6)
        self.display_surface.blit(title_text_surf, title_text_rect)

        # boxes (3x2 layout)
        # selecting lighter shaded box (index)
        # pokemon box sprite
        # pokemon name
        # pokemon level
        # pokemon health
        # pokemon held item if held item

    def display_pokemon(self):
        pokemon = list(POKEMON_DATA.items())[self.index][1]

        rect = pygame.FRect(
            self.main_rect.left + self.list_width, self.main_rect.top, self.main_rect.width - self.list_width, self.main_rect.height
        )
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], rect, 0, 12, 0, 12, 0)

        profile_rect = pygame.FRect(rect.topright + vector(-rect.height * 0.4, 0), (rect.height * 0.4, rect.height * 0.4))
        pygame.draw.rect(self.display_surface, COLOURS[pokemon['types'][0]['type']], profile_rect, 0, 0, 0, 12, 12)

        scale_factor = 2
        pokemon_surf = self.battle_sprites[f"{pokemon['name']}_normal"]
        pokemon_surf = pygame.transform.scale(pokemon_surf, (pokemon_surf.get_width()*scale_factor, pokemon_surf.get_height()*scale_factor))
        pokemon_rect = pokemon_surf.get_frect(center = profile_rect.center)
        self.display_surface.blit(pokemon_surf, pokemon_rect)

        if pokemon['name'] in DISCOVERED_POKEMON:
            # discovered display
            self.display_surface.blit(pokemon_surf, pokemon_rect)
            
            # name
            name_surf = self.fonts['bold'].render(pokemon['name'].capitalize(), False, COLOURS['white'])
            name_rect = name_surf.get_frect(topleft = rect.topleft + vector(25, 25))
            self.display_surface.blit(name_surf, name_rect)

            # ID
            id_surf = self.fonts['small'].render(f"No. {pokemon['id']}", False, COLOURS['white'])
            id_rect = id_surf.get_frect(bottomleft = name_rect.bottomright + vector(10, 0))
            self.display_surface.blit(id_surf, id_rect)

            # types
            last_type_length = 0
            text_box_height = 20
            border_add = 6
            bar_buffer = 12
            bar_width_mod = 70
            for _type in pokemon['types']:
                type_surf = self.fonts['bold'].render(f"{_type['type']}", False, COLOURS['white'])
                type_rect = type_surf.get_frect(topleft = name_rect.bottomleft + vector((last_type_length + border_add * 3) * (int(_type['slot'])-1), 20))
                type_box_rect = pygame.FRect(type_rect.topleft - vector(border_add, border_add), (type_rect.width + border_add * 2, (text_box_height + border_add * 2)))
                pygame.draw.rect(self.display_surface, COLOURS[_type['type'].lower()], type_box_rect, 0, 6, 6, 6, 6)
                last_type_length = type_surf.get_width()
                self.display_surface.blit(type_surf, type_rect)

            # genus
            genus_surf = self.fonts['regular'].render(pokemon['genus'], False, COLOURS['white'])
            genus_rect = genus_surf.get_frect(topleft = vector(name_rect.left, type_rect.bottom + 20))
            self.display_surface.blit(genus_surf, genus_rect)

            # caught ball
            ball_surf = self.ball_graphic
            ball_rect = ball_surf.get_frect(bottomleft = profile_rect.bottomleft + vector(10,-10))
            if pokemon['name'] not in CAUGHT_POKEMON:
                ball_surf = fill_non_transparent(ball_surf, (0, 0, 0, 255))
            self.display_surface.blit(ball_surf, ball_rect)

            # base stats
            for index, stat in enumerate(['HP', 'Atk', 'Def', 'SpAtk', 'SpDef', 'Speed']):
                text_surf = self.fonts['regular'].render(f"{stat}:", False, COLOURS['white'])
                text_rect = text_surf.get_frect(topleft = (rect.left + bar_buffer, profile_rect.bottom + (text_surf.get_height() + bar_buffer) * index + 33))
                self.display_surface.blit(text_surf, text_rect)

                bar_rect = pygame.FRect(vector(rect.left + bar_buffer + bar_width_mod, text_rect.top), (rect.width - bar_width_mod - bar_buffer * 3 - 40, text_rect.height))
                base_stat = int(pokemon['stats'][index]['base_stat'])
                bar_colour = ''
                if base_stat <= 85:
                    bar_colour = COLOURS['red']
                elif base_stat > 85 and base_stat <= 170:
                    bar_colour = COLOURS['amber']
                else:
                    bar_colour = COLOURS['green']
                draw_bar(self.display_surface, bar_rect, base_stat, 255, bar_colour, COLOURS['light'])
                
                value_text_surf = self.fonts['regular'].render(f"{base_stat}", False, COLOURS['white'])
                value_text_rect = value_text_surf.get_frect(topleft = bar_rect.topright + vector(bar_buffer, 0))
                self.display_surface.blit(value_text_surf, value_text_rect)
        else:
            # undiscovered display
            self.fill_non_transparent(pokemon_surf, (0, 0, 0, 255))
            self.display_surface.blit(pokemon_surf, pokemon_rect)
            
            unknown_surf = self.fonts['large'].render('[UNDISCOVERED]', False, COLOURS['white'])
            unknown_rect = unknown_surf.get_frect(center = (self.main_rect.center + vector(self.list_width/2, 0)))
            self.display_surface.blit(unknown_surf, unknown_rect)

    def input(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_UP]:
            self.index -= 1
        if keys[pygame.K_DOWN]:
            self.index += 1
        self.index = self.index % len(POKEMON_DATA.keys())

    def update(self, dt):
        self.input()
        self.display_surface.blit(self.tint_surf, (0,0))
        if self.current_window = 'party':
            self.display_party()
        if self.current_window = 'pokemon':
            self.display_pokemon()