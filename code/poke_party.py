from settings import *
from support import draw_bar
import player_data
from pokemon_data import POKEMON_DATA
from game_data import NATURE_DATA
from move_data import MOVE_DATA
import textwrap

class PokeParty:
    def __init__(self, fonts, pokemon_graphics, other_graphics):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts
        self.battle_sprites = pokemon_graphics['battle_sprites']
        self.box_sprites = pokemon_graphics['box_sprites']

        self.move_type_icon = {
            'physical': other_graphics['physical'],
            'special': other_graphics['special'],
            'status': other_graphics['status']
        }
        
        self.gender_icons = other_graphics['gender']

        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)

        self.column_n = 3
        self.row_n = 2

        self.order = [[],[]]

        self.pokemon = player_data.POKEMON

        self.selected_index = (0,0)
        self.index = (0,0)
        self.move_select_index = 0

        self.current_window = 'party'

    def display_party(self):
        for i in range(self.row_n):
            for j in range(self.column_n):
                self.order[i].append(player_data.POKEMON[i*3 + j].name if player_data.POKEMON[i*3 + j] else None)

        main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.6, WINDOW_HEIGHT*0.45).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        #pokedex title
        title_text_surf = self.fonts['bold'].render("POKEMON", True, COLOURS['white'], COLOURS['dark-grey'])
        title_text_rect = title_text_surf.get_frect(bottomleft = main_rect.topleft + vector(15, -5))
        border_add = 6
        title_box_rect = pygame.FRect(title_text_rect.topleft + vector(-border_add * 1.75, -border_add * 1.75), (title_text_rect.width + border_add * 3.5, (title_text_rect.height + border_add * 4.5)))
        pygame.draw.rect(self.display_surface, COLOURS['navy'], title_box_rect, 6, 6, 6, 6, 6)
        self.display_surface.blit(title_text_surf, title_text_rect)

        # background
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], main_rect, 0, 12, 12, 12, 12)

        # boxes (3x2 layout)
        top_gap = 30
        between_gap = 10
        box_width = main_rect.width*0.3
        box_height = main_rect.height/2 - top_gap - between_gap
        for i in range(self.row_n):
            for j in range(self.column_n):        
                pokemon_box_rect = pygame.FRect(
                    (
                        main_rect.midtop + \
                        vector(- between_gap - box_width*3/2, top_gap) + \
                        vector((box_width + between_gap)*j,(box_height + between_gap)*i)
                    ),
                    (box_width, box_height)
                )
                pygame.draw.rect(self.display_surface, COLOURS['grey'], pokemon_box_rect, 0, 8, 8, 8, 8)

        # selecting lighter shaded box (index)
        select_box_rect = pygame.FRect(
            (
                main_rect.midtop + \
                vector(- between_gap - box_width*3/2, top_gap) + \
                vector((box_width + between_gap)*self.index[0],(box_height + between_gap)*self.index[1])
            ),
            (box_width, box_height)
        )
        pygame.draw.rect(self.display_surface, COLOURS['light'], select_box_rect, 0, 8, 8, 8, 8)

        # pokemon data
        for i in range(self.row_n):
            for j in range(self.column_n):
                pos = main_rect.midtop + \
                    vector(- between_gap - box_width*3/2, top_gap) + \
                    vector((box_width + between_gap)*j,(box_height + between_gap)*i)
                if self.order[i][j] is None:
                    # empty box
                    empty_text_surf = self.fonts['regular'].render("[EMPTY]", False, COLOURS['white'])
                    empty_text_rect = pygame.FRect((pos + vector(box_width/2-empty_text_surf.get_width()/2,box_height/2-empty_text_surf.get_height()/2)), (empty_text_surf.get_width(), empty_text_surf.get_height()))
                    self.display_surface.blit(empty_text_surf, empty_text_rect)
                else:
                    pokemon = self.pokemon[3*i + j]
                    
                    # pokemon box sprite
                    icon_surf = self.box_sprites[pokemon.name]
                    icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*2, icon_surf.get_height()*2))
                    icon_rect = icon_surf.get_frect(topright = pos + vector(box_width + 25, -5))
                    self.display_surface.blit(icon_surf, icon_rect)

                    # pokemon name
                    name_surf = self.fonts['large'].render(pokemon.name.capitalize(), False, COLOURS['white'])
                    name_rect = name_surf.get_frect(topleft = pos + vector(12, 10))
                    self.display_surface.blit(name_surf, name_rect)

                    # pokemon level
                    level_surf = self.fonts['regular'].render(f'Lv.{pokemon.level}', False, COLOURS['white'])
                    level_rect = level_surf.get_frect(bottomleft = (icon_rect.right - level_surf.get_width(), name_rect.bottom) + vector(-32, -1))
                    self.display_surface.blit(level_surf, level_rect)

                    # health bar
                    health_bar_height = 15
                    health_bar_width = 130
                    health_bar_rect = pygame.FRect(((name_rect.left, icon_rect.bottom) + vector(0, - health_bar_height - 10)),(health_bar_width, health_bar_height))
                    health_bar_colour = None
                    ratio = pokemon.current_hp/pokemon.max_hp
                    if ratio < 0.2:
                        health_bar_colour = COLOURS['red']
                    elif ratio >= 0.2 and ratio < 0.5:
                        health_bar_colour = COLOURS['amber']
                    else:
                        health_bar_colour = COLOURS['green']
                    draw_bar(self.display_surface, health_bar_rect, pokemon.current_hp, pokemon.max_hp, health_bar_colour, COLOURS['light'])

                    # health text
                    health_text_surf = self.fonts['bold'].render(f'{pokemon.current_hp}/{pokemon.max_hp}', False, COLOURS['white'])
                    health_text_rect = health_text_surf.get_frect(bottomleft = health_bar_rect.topleft + vector(0, -5))
                    self.display_surface.blit(health_text_surf, health_text_rect)                    

                    # xp bar
                    xp_bar_height = 10
                    xp_bar_rect = pygame.FRect((health_bar_rect.bottomleft),(health_bar_width, xp_bar_height))
                    xp_bar_colour = COLOURS['blue']
                    draw_bar(self.display_surface, xp_bar_rect, pokemon.current_xp, pokemon.level_xp, xp_bar_colour, COLOURS['light-grey'])

                    # pokemon held item if held item
                    # any status effect

    def display_pokemon(self):
        pokemon = self.pokemon[3*self.selected_index[1] + self.selected_index[0]]
        
        main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.6, WINDOW_HEIGHT*0.6).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        divide_y = 527

        rect = pygame.FRect(
            main_rect.left, main_rect.top, main_rect.width, main_rect.height
        )
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], rect, 0, 12, 12, 12, 12)

        profile_rect = pygame.FRect(rect.topright + vector(-rect.height * 0.4, 0), (rect.height * 0.4, rect.height * 0.4))
        pygame.draw.rect(self.display_surface, COLOURS[pokemon.type[0]], profile_rect, 0, 0, 0, 12, 12)

        scale_factor = 2
        pokemon_surf = self.battle_sprites[f"{pokemon.name}_normal"]
        pokemon_surf = pygame.transform.scale(pokemon_surf, (pokemon_surf.get_width()*scale_factor, pokemon_surf.get_height()*scale_factor))
        pokemon_rect = pokemon_surf.get_frect(midbottom = profile_rect.midbottom + vector(0,-10))
        self.display_surface.blit(pokemon_surf, pokemon_rect)
        
        # name
        name_surf = self.fonts['bold'].render(pokemon.name.capitalize(), False, COLOURS['white'])
        name_rect = name_surf.get_frect(topleft = rect.topleft + vector(25, 25))
        self.display_surface.blit(name_surf, name_rect)

        # gender
        gender_surf = self.gender_icons[pokemon.gender if pokemon.gender is not None else 'genderless']
        gender_surf = pygame.transform.scale(gender_surf, (name_rect.height,name_rect.height))
        gender_rect = gender_surf.get_frect(bottomleft = name_rect.bottomright + vector(5, 0))
        self.display_surface.blit(gender_surf, gender_rect)

        # ID
        id_surf = self.fonts['small'].render(f"No. {pokemon.data['id']}", False, COLOURS['white'])
        id_rect = id_surf.get_frect(bottomleft = gender_rect.bottomright + vector(5, 0))
        self.display_surface.blit(id_surf, id_rect)

        # types
        last_type_length = 0
        text_box_height = 20
        border_add = 6
        bar_buffer = 12
        bar_width_mod = 70
        for _type in pokemon.type:
            type_surf = self.fonts['bold'].render(f"{_type}", False, COLOURS['white'])
            type_surf = pygame.transform.scale(type_surf, (type_surf.get_width()*0.85, type_surf.get_height()*0.85))
            type_rect = type_surf.get_frect(topleft = name_rect.bottomleft + vector((last_type_length + border_add * 3) * (int(pokemon.type.index(_type))), 20))
            type_box_rect = pygame.FRect(type_rect.topleft - vector(border_add, border_add), (type_rect.width + border_add * 2, (text_box_height + border_add * 2)))
            pygame.draw.rect(self.display_surface, COLOURS[_type.lower()], type_box_rect, 0, 6, 6, 6, 6)
            last_type_length = type_surf.get_width()
            self.display_surface.blit(type_surf, type_rect)

        # genus
        genus_surf = self.fonts['regular'].render(pokemon.data['genus'], False, COLOURS['white'])
        genus_rect = genus_surf.get_frect(topleft = vector(name_rect.left, type_rect.bottom + 20))
        self.display_surface.blit(genus_surf, genus_rect)

        # base stats
        for index, stat in enumerate(['HP', 'Atk', 'Def', 'SpAtk', 'SpDef', 'Speed']):
            text_surf = self.fonts['regular'].render(f"{stat}:", False, COLOURS['white'])
            text_rect = text_surf.get_frect(topleft = (divide_y + bar_buffer, profile_rect.bottom + (text_surf.get_height() + bar_buffer) * index + 33))
            self.display_surface.blit(text_surf, text_rect)

            bar_rect = pygame.FRect(vector(divide_y + bar_buffer + bar_width_mod, text_rect.top), (rect.width - bar_width_mod - bar_buffer * 3 - 40 - (divide_y - rect.left), text_rect.height))
            base_stat = int(pokemon.base_stats[stat])
            bar_colour = None
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

        health_bar_height = 15
        xp_bar_height = 10

        # health bar
        health_bar_rect = pygame.FRect((divide_y + bar_buffer, profile_rect.bottom - health_bar_height - xp_bar_height),(profile_rect.left - (divide_y + bar_buffer) - bar_buffer*2, health_bar_height))
        health_bar_colour = None
        ratio = pokemon.current_hp/pokemon.max_hp
        if ratio < 0.2:
            health_bar_colour = COLOURS['red']
        elif ratio >= 0.2 and ratio < 0.5:
            health_bar_colour = COLOURS['amber']
        else:
            health_bar_colour = COLOURS['green']
        draw_bar(self.display_surface, health_bar_rect, pokemon.current_hp, pokemon.max_hp, health_bar_colour, COLOURS['light'])

        # health text
        health_text_surf = self.fonts['regular'].render(f'{pokemon.current_hp}/{pokemon.max_hp}', False, COLOURS['white'])
        health_text_rect = health_text_surf.get_frect(bottomright = health_bar_rect.topright + vector(0, -5))
        self.display_surface.blit(health_text_surf, health_text_rect)                    

        # xp bar
        xp_bar_rect = pygame.FRect((health_bar_rect.bottomleft),(health_bar_rect.width, xp_bar_height))
        xp_bar_colour = COLOURS['blue']
        draw_bar(self.display_surface, xp_bar_rect, pokemon.current_level_xp, pokemon.level_xp, xp_bar_colour, COLOURS['light-grey'])

        # level
        level_surf = self.fonts['bold'].render(f'Lv.{pokemon.level}', False, COLOURS['white'])
        level_rect = level_surf.get_frect(bottomleft = health_bar_rect.topleft + vector(0,-10))
        self.display_surface.blit(level_surf, level_rect)

        # ability
        ability_surf = self.fonts['regular'].render(f'Ability: {pokemon.ability.replace('-', ' ').title()}', False, COLOURS['white'])
        ability_rect = ability_surf.get_frect(topright = (health_bar_rect.right, name_rect.top))
        self.display_surface.blit(ability_surf, ability_rect)

        # nature
        nature_right_bracket_surf = self.fonts['regular'].render(')', False, COLOURS['white'])
        nature_right_bracket_rect = nature_right_bracket_surf.get_frect(topright = (ability_rect.bottomright))
        self.display_surface.blit(nature_right_bracket_surf, nature_right_bracket_rect)
        
        if NATURE_DATA[pokemon.nature]['decreased'] and NATURE_DATA[pokemon.nature]['increased']:
            nature_right_bonus_surf = self.fonts['regular'].render(f'-{NATURE_DATA[pokemon.nature]['decreased']}', False, COLOURS['red'])
            nature_right_bonus_rect = nature_right_bonus_surf.get_frect(bottomright = nature_right_bracket_rect.bottomleft)
            self.display_surface.blit(nature_right_bonus_surf, nature_right_bonus_rect)

            nature_slash_surf = self.fonts['regular'].render('/', False, COLOURS['white'])
            nature_slash_rect = nature_slash_surf.get_frect(bottomright = nature_right_bonus_rect.bottomleft)
            self.display_surface.blit(nature_slash_surf, nature_slash_rect)

            nature_left_bonus_surf = self.fonts['regular'].render(f'+{NATURE_DATA[pokemon.nature]['increased']}', False, COLOURS['blue'])
            nature_left_bonus_rect = nature_left_bonus_surf.get_frect(bottomright = nature_slash_rect.bottomleft)
            self.display_surface.blit(nature_left_bonus_surf, nature_left_bonus_rect)

            nature_surf = self.fonts['regular'].render(f'Nature: {pokemon.nature.capitalize()} (', False, COLOURS['white'])
            nature_rect = nature_surf.get_frect(bottomright = nature_left_bonus_rect.bottomleft)
            self.display_surface.blit(nature_surf, nature_rect)
        else:
            nature_surf = self.fonts['regular'].render(f'Nature: {pokemon.nature.capitalize()} (no effect', False, COLOURS['white'])
            nature_rect = nature_surf.get_frect(bottomright = nature_right_bracket_rect.bottomleft)
            self.display_surface.blit(nature_surf, nature_rect)

        # moves
        move_gap = 5
        move_box_height = (main_rect.bottom - genus_rect.bottom - bar_buffer*2) / 4 - move_gap
        move_box_width = health_bar_rect.left - genus_rect.left - bar_buffer
        for i in range(4):
            move = pokemon.moves[i]
            box_topleft_pos = (genus_rect.left, genus_rect.bottom + bar_buffer + (move_box_height+move_gap)*i)
            move_box_rect = pygame.FRect(box_topleft_pos, (move_box_width, move_box_height))

            if i == self.move_select_index:
                box_wrap = 6
                pygame.draw.rect(self.display_surface, COLOURS['white'], pygame.FRect(box_topleft_pos + vector(-box_wrap/2, -box_wrap/2), (move_box_width + box_wrap, move_box_height + box_wrap)), 0, 8, 8, 8, 8)

            if move:
                move_data = MOVE_DATA[move['name']]

                # box
                pygame.draw.rect(self.display_surface, COLOURS[move_data['type']], move_box_rect, 0, 8, 8, 8, 8)

                # name
                move_name_surf = self.fonts['regular'].render(f'{move['name'].replace('-', ' ').title()}', False, COLOURS['white'])
                move_name_rect = move_name_surf.get_frect(topleft = box_topleft_pos + vector(10,10))
                self.display_surface.blit(move_name_surf, move_name_rect)

                # move_icon
                icon_surf = self.move_type_icon[move_data['damage_class']]
                icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*0.6, icon_surf.get_height()*0.6))
                icon_width = icon_surf.get_width()
                icon_height = icon_surf.get_height()
                icon_rect = icon_surf.get_frect(topleft = box_topleft_pos + vector(move_box_width - icon_width - 10, 10))
                self.display_surface.blit(icon_surf, icon_rect)
                
                # pp
                pp_surf = self.fonts['small'].render(f'PP:{move['current_pp']}/{move_data['max_pp']}', False, COLOURS['white'])
                pp_rect = pp_surf.get_frect(topleft = box_topleft_pos + vector(10, move_box_height - pp_surf.get_height() - 10))
                self.display_surface.blit(pp_surf, pp_rect)

                # power
                power_surf = self.fonts['small'].render(f'Power: {move_data['power']}' if move_data['power'] else 'Power: --', False, COLOURS['white'])
                power_rect = power_surf.get_frect(bottomleft = pp_rect.bottomright + vector(10,0))
                self.display_surface.blit(power_surf, power_rect)

                # accuracy
                acc_surf = self.fonts['small'].render(f'Acc: {move_data['accuracy']}' if move_data['accuracy'] else 'Acc: --', False, COLOURS['white'])
                acc_rect = acc_surf.get_frect(bottomleft = power_rect.bottomright + vector(10,0))
                self.display_surface.blit(acc_surf, acc_rect)

                # selected box
                if i == self.move_select_index:
                    text = '\n'.join(textwrap.wrap(f"{move_data['flavor_text_entry']} {move_data['effect_entries']}", width=76))
                    item_text_surf = self.fonts['regular'].render(text, False, COLOURS['white'])

                    text_bg_rect = pygame.FRect(vector(main_rect.bottomleft + vector(0, bar_buffer)), (main_rect.width, item_text_surf.get_height() + bar_buffer*2))
                    pygame.draw.rect(self.display_surface, COLOURS['grey'], text_bg_rect, 0, 12, 12, 12, 12)

                    item_text_rect = item_text_surf.get_frect(topleft = text_bg_rect.topleft + vector(bar_buffer, bar_buffer))
                    self.display_surface.blit(item_text_surf, item_text_rect)

            else:
                # box
                move_box_rect = pygame.FRect(box_topleft_pos, (move_box_width, move_box_height))
                pygame.draw.rect(self.display_surface, COLOURS['grey'], move_box_rect, 0, 8, 8, 8, 8)

                # name
                move_name_surf = self.fonts['bold'].render('--', False, COLOURS['white'])
                move_name_rect = move_name_surf.get_frect(center = move_box_rect.center)
                self.display_surface.blit(move_name_surf, move_name_rect)

    def input(self):
        keys = pygame.key.get_just_pressed()

        if self.current_window == 'party':
            if keys[pygame.K_UP]:
                self.index = (self.index[0], self.index[1] - 1)
            if keys[pygame.K_DOWN]:
                self.index = (self.index[0], self.index[1] + 1)
            if keys[pygame.K_LEFT]:
                self.index = (self.index[0] - 1, self.index[1])
            if keys[pygame.K_RIGHT]:
                self.index = (self.index[0] + 1, self.index[1])
            self.index = (self.index[0] % 3, self.index[1] % 2)
            if keys[pygame.K_SPACE]:
                if self.order[self.index[1]][self.index[0]] is not None:
                    if self.current_window == 'party':
                        self.selected_index = self.index
                        self.current_window = 'pokemon'

        if self.current_window == 'pokemon':
            if keys[pygame.K_UP]:
                self.move_select_index -= 1
            if keys[pygame.K_DOWN]:
                self.move_select_index += 1
            self.move_select_index = self.move_select_index % 4
            if keys[pygame.K_z]:
                self.move_select_index = 0
                self.current_window = 'party'

    def update(self, dt):
        self.input()
        self.display_surface.blit(self.tint_surf, (0,0))
        if self.current_window == 'party':
            self.display_party()
        if self.current_window == 'pokemon':
            self.display_pokemon()