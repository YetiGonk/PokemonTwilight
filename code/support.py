from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame

# imports 
def import_image(*path, alpha = True, format = 'png'):
	full_path = join(*path) + f'.{format}'
	surf = pygame.image.load(full_path).convert_alpha()
	return surf

def import_folder(*path):
	frames = []
	for folder_path, sub_folders, image_names in walk(join(*path)):
		for image_name in sorted(image_names, key = lambda name: int(name.split('.')[0])):
			full_path = join(folder_path, image_name)
			surf = pygame.image.load(full_path).convert_alpha()
			frames.append(surf)
	return frames

def import_folder_dict(*path):
    frames = {}
    folder_path = join(*path)
    for root, _, files in walk(folder_path):
        for file in files:
            file_path = join(root, file)
            try:
                surf = pygame.image.load(file_path).convert_alpha()
                frames[file.rsplit('.', 1)[0].lower()] = surf
            except pygame.error as e:
                print(f"Error loading image {file_path}: {e}")
    return frames

def import_sub_folders(*path):
	frames = {}
	for _, sub_folders, __ in walk(join(*path)):
		if sub_folders:
			for sub_folder in sub_folders:
				frames[sub_folder] = import_folder(*path, sub_folder)
	return frames

def import_tilemap(cols, rows, *path):
	frames = {}
	surf = import_image(*path)
	cell_width, cell_height = surf.get_width() // cols, surf.get_height() // rows
	for col in range(cols):
		for row in range(rows):
			cutout_rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
			cutout_surf = pygame.Surface((cell_width, cell_height), pygame.SRCALPHA)
			cutout_surf.blit(surf, (0, 0), cutout_rect)
			frames[(col, row)] = cutout_surf
	return frames

def character_importer(cols, rows, *path):
    frame_dict = import_tilemap(cols, rows, *path)
    new_dict = {}
    for row, direction in enumerate(('up', 'down', 'left', 'right')):
        new_dict[direction] = [pygame.transform.scale(frame_dict[(col, row)], (64, 64)) for col in range(cols)]
        new_dict[f"{direction}_idle"] = [pygame.transform.scale(frame_dict[(0, row)], (64, 64))]
    return new_dict

def all_character_import(*path):
    new_dict = {}
    for _, __, image_names in walk(join(*path)):
        for image in image_names:
            image_name = image.split('.')[0]
            new_dict[image_name] = character_importer(4, 4, *path, image_name)
    return new_dict

# game functions

def check_connection(radius, entity, target, tolerance = 30):
    relation = vector(target.rect.center) - vector(entity.rect.center)
    if relation.length() < radius:
        if entity.facing_direction == 'left' and relation.x < 0 and abs(relation.y) < tolerance or \
            entity.facing_direction == 'right' and relation.x > 0 and abs(relation.y) < tolerance or \
            entity.facing_direction == 'up' and relation.y < 0 and abs(relation.x) < tolerance or \
            entity.facing_direction == 'down' and relation.y > 0 and abs(relation.x) < tolerance:
        	return True
    return False

def draw_bar(surface, rect, value, max_value, colour, bg_colour, radius=1):
    ratio = rect.width / max_value
    bg_rect = rect.copy()
    progress = max(0, min(rect.width, value * ratio))
    progress_rect = pygame.FRect(rect.topleft, (progress, rect.height))
    if bg_colour:
        pygame.draw.rect(surface, bg_colour, bg_rect, 0, radius)
    pygame.draw.rect(surface, colour, progress_rect, 0, radius)