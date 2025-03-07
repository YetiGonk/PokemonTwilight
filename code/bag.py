from settings import *
import textwrap
import player_data
from game_data import *
from move_data import MOVE_DATA
from item_data import ITEM_DATA
import pokemon_data
import ability_data
from support import *
from dialog import DialogTree, DialogSprite

class Bag:
    def __init__(self, fonts, pokemon_graphics, item_graphics, other_graphics):
        self.display_surface = pygame.display.get_surface()
        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.5, WINDOW_HEIGHT*0.6).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        self.fonts = fonts
        self.pokemon_graphics = pokemon_graphics
        self.item_graphics = item_graphics
        
        self.player_pokemon = player_data.POKEMON

        # other graphics
        self.move_type_icon = {
            'physical': other_graphics['physical'],
            'special': other_graphics['special'],
            'status': other_graphics['status']
        }

        self.bag_icons = other_graphics['bag_icons']
        self.bag_sprites = other_graphics['bag_sprites']
        self.gender_icons = other_graphics['gender']

        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.tint_surf.set_alpha(200)   

        self.visible_items = 7
        self.list_width = self.main_rect.width * 0.4
        self.item_height = self.main_rect.height / self.visible_items

        self.current_bag = player_data.BAG
        self.bag_open = True

        self.dialog_tree = None
        self.dialog_input_overlap = False

        self.bag_index = 0
        self.bag_category_index = 0
        self.bag_option = 0
        self.bag_pokemon_option = 0
        
        self.bag_option_select = False
        self.bag_option_pokemon_select = False
        self.bag_open = False

    def draw_bag(self):
        self.main_rect = pygame.FRect(0, 0, WINDOW_WIDTH*0.5, WINDOW_HEIGHT*0.6).move_to(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

        self.visible_items = 7
        self.list_width = self.main_rect.width * 0.4
        self.item_height = self.main_rect.height / self.visible_items

        self.current_bag = player_data.BAG
        self.bag_open = True
        
        list_bg_rect = pygame.FRect(self.main_rect.topleft, (self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], list_bg_rect, 0, 0, 12, 0, 12, 0)

        # bag title
        title_text_surf = self.fonts['bold'].render("BAG", True, COLOURS['white'], COLOURS['dark-grey'])
        title_text_rect = title_text_surf.get_frect(bottomleft = self.main_rect.topleft + vector(15, -5))
        border_add = 6
        title_box_rect = pygame.FRect(title_text_rect.topleft + vector(-border_add * 1.75, -border_add * 1.75), (title_text_rect.width + border_add * 3.5, (title_text_rect.height + border_add * 4.5)))
        pygame.draw.rect(self.display_surface, COLOURS['water'], title_box_rect, 6, 6, 6, 6, 6)
        self.display_surface.blit(title_text_surf, title_text_rect)

        # bag category icons
        bag_icon_botright_pos = self.main_rect.topright + vector(-20, -5)
        icon_gap = 6
        padding = 4
        for i, category in enumerate(list(player_data.BAG.keys())):
            bag_icon_surf = self.bag_icons[category]
            bag_icon_surf = pygame.transform.scale(bag_icon_surf, (bag_icon_surf.get_width()*1.5, bag_icon_surf.get_width()*1.5))

            bag_icon_bg_rect = pygame.FRect(
                bag_icon_botright_pos - vector(padding*2, padding*2) - vector(bag_icon_surf.get_width(), bag_icon_surf.get_height()) - vector((bag_icon_surf.get_width()+padding*2+icon_gap)*i, 0),
                (bag_icon_surf.get_width() + padding*2, bag_icon_surf.get_height() + padding*2)
            )
            pygame.draw.rect(self.display_surface, COLOURS['white' if i == self.bag_category_index else 'grey'], bag_icon_bg_rect, 6, 6, 6, 6, 6)

            bag_icon_rect = bag_icon_surf.get_frect(center = bag_icon_bg_rect.center)
            self.display_surface.blit(bag_icon_surf, bag_icon_rect)

        data_bg_rect = pygame.FRect(self.main_rect.topleft + vector(self.list_width, 0), (self.main_rect.width - self.list_width, self.main_rect.height))
        pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], data_bg_rect, 0, 12, 0, 12, 0, 0)

        category = list(player_data.BAG.keys())[self.bag_category_index]
        bag_sprite_surf = self.bag_sprites[category]
        bag_sprite_surf = pygame.transform.scale(bag_sprite_surf, (bag_sprite_surf.get_width()*3, bag_sprite_surf.get_height()*3))
        bag_sprite_rect = bag_sprite_surf.get_frect(center = data_bg_rect.midtop + vector(0,data_bg_rect.height*0.333))
        self.display_surface.blit(bag_sprite_surf, bag_sprite_rect)

        category_text = None
        if category == 'balls':
            category_text = 'Poke Balls'
        if category == 'berries':
            category_text = 'Berries'
        if category == 'tms':
            category_text = 'TMs'
        if category == 'key-items':
            category_text = 'Key Items'
        if category == 'medicine':
            category_text = 'Medicine'
        if category == 'battle-items':
            category_text = 'Battle Items'
        if category == 'items':
            category_text = 'Items'
        category_surf = self.fonts['large'].render(category_text, False, COLOURS['white'])
        category_rect = category_surf.get_frect(midtop = data_bg_rect.midtop + vector(0, 15))
        self.display_surface.blit(category_surf, category_rect)

        # list entries
        v_offset = 0 if self.bag_index < self.visible_items else -(self.bag_index - self.visible_items + 1) * self.item_height
        category = list(player_data.BAG.keys())[self.bag_category_index]
        for index, data in enumerate(player_data.BAG[category]):
            name, count = data['name'], data['count']
            bg_colour = COLOURS['grey'] if self.bag_index != index else COLOURS['light']
            top = self.main_rect.top + index * self.item_height + v_offset
            item_rect = pygame.FRect(self.main_rect.left, top, self.list_width, self.item_height)

            list_name = name.replace('-', ' ').title()
            if category == 'balls':
                list_name += ' Ball'
            if category == 'berries':
                list_name += ' Berry'
            text_surf = self.fonts['regular'].render(list_name, False, COLOURS['white'])
            text_rect = text_surf.get_frect(midleft = item_rect.midleft + vector(90, 0))

            # list item sprites
            if category == 'tms':
                icon_surf = self.item_graphics[category][MOVE_DATA[name]['type']]
            else:
                icon_surf = self.item_graphics[category][name]
            icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*2, icon_surf.get_height()*2))
            icon_rect = icon_surf.get_frect(center = item_rect.midleft + vector(45, 0))

            quantity_surf = self.fonts['small'].render(str(count), False, COLOURS['white'])
            quantity_rect = quantity_surf.get_frect(midbottom = icon_rect.bottomright + vector(-5, -5))

            if item_rect.colliderect(self.main_rect):
                if item_rect.collidepoint(self.main_rect.topleft):
                    pygame.draw.rect(self.display_surface, bg_colour, item_rect, 0, 0, 12)
                elif item_rect.collidepoint(self.main_rect.bottomleft + vector(1,-1)):
                    pygame.draw.rect(self.display_surface, bg_colour, item_rect, 0, 0, 0, 0, 12, 0)
                else:
                    pygame.draw.rect(self.display_surface, bg_colour, item_rect)
                self.display_surface.blit(text_surf, text_rect)
                self.display_surface.blit(icon_surf, icon_rect)
                if category != 'tms':
                    if 'countable' in ITEM_DATA[name]['attributes']:
                        self.display_surface.blit(quantity_surf, quantity_rect)

        text_buffer = 10
        top_gap = 30
        text_bg_rect = pygame.FRect(
            vector(data_bg_rect.left + text_buffer, bag_sprite_rect.bottom + top_gap),
            (
                self.main_rect.width - self.list_width - text_buffer*2,
                data_bg_rect.bottom - (bag_sprite_rect.bottom + top_gap) - text_buffer
            )
        )
        pygame.draw.rect(self.display_surface, COLOURS['grey'], text_bg_rect, 0, 12, 12, 12, 12)

        text = None
        if category == 'tms':
            text = '\n'.join(textwrap.wrap(f"{MOVE_DATA[player_data.BAG[category][self.bag_index]['name']]['flavor_text_entry']}", width=32))
        else:
            text = '\n'.join(textwrap.wrap(f"{ITEM_DATA[player_data.BAG[category][self.bag_index]['name']]['flavor_text']} {ITEM_DATA[player_data.BAG[category][self.bag_index]['name']]['short_effect']}", width=38))
        item_text_surf = self.fonts['bag'].render(text, False, COLOURS['white'])
        item_text_rect = item_text_surf.get_frect(topleft = text_bg_rect.topleft + vector(text_buffer, text_buffer))
        self.display_surface.blit(item_text_surf, item_text_rect)
        
        if category == 'tms':
            move_data = MOVE_DATA[player_data.BAG[category][self.bag_index]['name']]

            # power
            power_surf = self.fonts['regular'].render(f'Power: {move_data['power']}' if move_data['power'] else 'Power: --', False, COLOURS['white'])
            power_rect = power_surf.get_frect(bottomleft = text_bg_rect.topleft + vector(0, -text_buffer))
            self.display_surface.blit(power_surf, power_rect)
            
            # move_icon
            icon_surf = self.move_type_icon[move_data['damage_class']]
            icon_surf = pygame.transform.scale(icon_surf, (icon_surf.get_width()*0.6, icon_surf.get_height()*0.6))
            icon_width = icon_surf.get_width()
            icon_height = icon_surf.get_height()
            icon_rect = icon_surf.get_frect(bottomleft = power_rect.topleft + vector(0, -text_buffer))
            self.display_surface.blit(icon_surf, icon_rect)
            
            # pp
            pp_surf = self.fonts['regular'].render(f'PP:{move_data['max_pp']}', False, COLOURS['white'])
            pp_rect = pp_surf.get_frect(bottomright = text_bg_rect.topright + vector(0, -text_buffer))
            self.display_surface.blit(pp_surf, pp_rect)

            # accuracy
            acc_surf = self.fonts['regular'].render(f'Acc: {move_data['accuracy']}' if move_data['accuracy'] else 'Acc: --', False, COLOURS['white'])
            acc_rect = acc_surf.get_frect(bottomright = pp_rect.topright + vector(0, -text_buffer))
            self.display_surface.blit(acc_surf, acc_rect)

        #lines
        for i in range(min(self.visible_items, len(player_data.BAG[category]))):
            y = self.main_rect.top + self.item_height * i
            left = self.main_rect.left
            right = self.main_rect.left + self.list_width
            pygame.draw.line(self.display_surface, COLOURS['light-grey'], (left, y), (right, y))
        
        #shadow
        shadow_surf = pygame.Surface((4, self.main_rect.height))
        shadow_surf.set_alpha(100)
        self.display_surface.blit(shadow_surf, (self.main_rect.left + self.list_width - 4, self.main_rect.top))

    def draw_bag_option_select(self):
        options = ['use', 'give', 'trash']
        option_gap = 8
        bar_buffer = 12
        option_box_height = 40
        option_box_width = 150

        for i, option in enumerate(options):
            box_topleft_pos = self.main_rect.bottomright + vector(-option_box_width/2, -option_box_height*5/2 + (option_box_height+option_gap)*i)

            # outline box  
            padding = 8
            option_outline_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
            pygame.draw.rect(self.display_surface, COLOURS['grey'], option_outline_box_rect, 8, 8, 8, 8, 8)

            # box
            option_box_rect = pygame.FRect(box_topleft_pos, (option_box_width, option_box_height))
            pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], option_box_rect, 0, 8, 8, 8, 8)

            # name
            option_name_surf = self.fonts['regular'].render(f'{option.upper()}', False, COLOURS['white'])
            option_name_rect = option_name_surf.get_frect(center = option_box_rect.center)
            self.display_surface.blit(option_name_surf, option_name_rect)

            if i == self.bag_option:
                option_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
                pygame.draw.rect(self.display_surface, COLOURS['white'], option_box_rect, 8, 8, 8, 8, 8)

    def draw_bag_option_pokemon_select(self):
        option_gap = 8
        bar_buffer = 12
        option_box_height = 40
        option_box_width = 150

        for i, option in list(self.player_pokemon.items()):
            if option is not None:
                box_topleft_pos = self.main_rect.bottomright + vector(option_box_width/2 + bar_buffer, -option_box_height*5/2 + (option_box_height+option_gap)*i)

                # outline box  
                padding = 8
                option_outline_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
                pygame.draw.rect(self.display_surface, COLOURS['grey'], option_outline_box_rect, 8, 8, 8, 8, 8)

                # box
                option_box_rect = pygame.FRect(box_topleft_pos, (option_box_width, option_box_height))
                pygame.draw.rect(self.display_surface, COLOURS['dark-grey'], option_box_rect, 0, 8, 8, 8, 8)

                # name
                option_name_surf = self.fonts['regular'].render(f'{option.name.upper()}', False, COLOURS['white'])
                option_name_rect = option_name_surf.get_frect(center = option_box_rect.center)
                self.display_surface.blit(option_name_surf, option_name_rect)

                if i == self.bag_pokemon_option:
                    option_box_rect = pygame.FRect(box_topleft_pos - vector(padding/2, padding/2), (option_box_width + padding, option_box_height + padding))
                    pygame.draw.rect(self.display_surface, COLOURS['white'], option_box_rect, 8, 8, 8, 8, 8)

    def input(self):
        if not self.dialog_tree:
            keys = pygame.key.get_just_pressed()
            
            if self.bag_option_select:
                if self.bag_option_pokemon_select:
                    if keys[pygame.K_UP]:
                        self.bag_pokemon_option -= 1
                    if keys[pygame.K_DOWN]:
                        self.bag_pokemon_option += 1
                    self.bag_pokemon_option = self.bag_pokemon_option % len([i for i in list(self.player_pokemon.values()) if i is not None])
                    if keys[pygame.K_SPACE]:
                        pass
                    if keys[pygame.K_z]:
                        self.bag_option_pokemon_select = False
                else:
                    if keys[pygame.K_UP]:
                        self.bag_option -= 1
                    if keys[pygame.K_DOWN]:
                        self.bag_option += 1
                    self.bag_option = self.bag_option % 3
                    if keys[pygame.K_SPACE]:
                        if self.bag_option == 0: # use
                            item_name = player_data.BAG[list(player_data.BAG.keys())[self.bag_category_index]][self.bag_index]['name']
                            if 'usable-in-battle' not in ITEM_DATA[item_name]['attributes']:
                                if not self.dialog_input_overlap:
                                    self.dialog_tree = DialogTree(self.all_sprites, self.fonts['dialog'], self.display_surface, self.end_dialog, narration=[f"{item_name.replace('-', ' ').title()} cannot be used during a battle!"])
                                if self.dialog_input_overlap:
                                    self.dialog_input_overlap = False 
                            else:
                                self.bag_option_pokemon_select = True
                        if self.bag_option == 1: # give
                            self.bag_option_pokemon_select = True
                        if self.bag_option == 2: # trash
                            self.bag_open = False
                            self.bag_option_select = False
                    if keys[pygame.K_z]:
                        self.bag_open = False
                        self.bag_option_select = False
            else:
                if keys[pygame.K_UP]:
                    self.bag_index -= 1
                if keys[pygame.K_DOWN]:
                    self.bag_index += 1
                if keys[pygame.K_RIGHT]:
                    self.bag_category_index -= 1
                    self.bag_index = 0
                if keys[pygame.K_LEFT]:
                    self.bag_category_index += 1
                    self.bag_index = 0
                self.bag_category_index = self.bag_category_index % len(list(player_data.BAG.keys()))
                self.bag_index = self.bag_index % len(player_data.BAG[list(player_data.BAG.keys())[self.bag_category_index]])
                if keys[pygame.K_SPACE]:
                    if self.bag_open:
                        self.selected_bag_index = (self.bag_category_index, self.bag_index)
                        self.bag_option_select = True


    def update(self, dt):
        self.display_surface.blit(self.tint_surf, (0,0))

        if self.dialog_tree:
            self.dialog_tree.update()
        if not self.dialog_tree:
            self.input()

        self.draw_bag()
        if self.bag_option_select:
            self.draw_bag_option_select()
            if self.bag_option_pokemon_select:
                self.draw_bag_option_pokemon_select()
