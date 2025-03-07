import os
from PIL import Image

def get_max_dimensions(folder_path):
    """
    Get the maximum width and height of the images in the folder.
    """
    max_width = 0
    max_height = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            with Image.open(file_path) as img:
                width, height = img.size
                if width > max_width:
                    max_width = width
                if height > max_height:
                    max_height = height
    return max_width, max_height

def center_sprite_in_rectangle(image, max_width, max_height):
    """
    Center the sprite in a transparent rectangle of given max width and max height.
    Align the middle bottom of the sprite with the middle bottom of the rectangle.
    """
    width, height = image.size
    new_image = Image.new("RGBA", (max_width, max_height), (0, 0, 0, 0))
    offset_x = (max_width - width) // 2
    offset_y = max_height - height
    new_image.paste(image, (offset_x, offset_y))
    return new_image

def process_sprites(folder_path):
    """
    Process all cropped PNG images in the folder, and place them into a transparent rectangle.
    """
    max_width, max_height = get_max_dimensions(folder_path)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            with Image.open(file_path) as img:
                centered_img = center_sprite_in_rectangle(img, max_width, max_height)
                centered_img.save(file_path)

if __name__ == "__main__":
    folder_path = '../graphics/pokemon/battle_sprites'  # Replace with the path to your folder
    process_sprites(folder_path)
    print("Cropping completed.")    