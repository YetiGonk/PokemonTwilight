from PIL import Image

def replace_color_with_transparency(image_path):
    # Open the image
    image = Image.open(image_path).convert("RGBA")
    
    # Get the color of the top-left pixel
    top_left_pixel = image.getpixel((0, 0))
    
    # Create a new image with an alpha channel (transparency)
    new_image = Image.new("RGBA", image.size)
    
    # Load pixel data
    pixels = image.load()
    new_pixels = new_image.load()
    
    # Iterate over each pixel in the image
    for y in range(image.height):
        for x in range(image.width):
            current_pixel = pixels[x, y]
            # Replace the pixel with transparency if it matches the top-left pixel color
            if current_pixel == top_left_pixel:
                new_pixels[x, y] = (0, 0, 0, 0)  # Fully transparent
            else:
                new_pixels[x, y] = current_pixel
    
    # Save the modified image
    new_image.save(image_path, "PNG")

# Example usage
replace_color_with_transparency("graphics/characters/overworld/collector.png")