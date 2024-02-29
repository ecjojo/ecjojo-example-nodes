import numpy as np
import torch
import os
from PIL import Image, ImageDraw,  ImageFont

color_mapping = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}

COLORS = ["white", "black"]

FONTS_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fonts")

class TextOverlayNode:
    
    @classmethod
    def INPUT_TYPES(cls):

     
        ALIGN_OPTIONS = ["center", "top left", "top center", "top right", "bottom left", "bottom center", "bottom right"]  
    
        return {
            "image": ("IMAGE", {"display": "image"}),
            "text": ("STRING", {"default": 'Your Name'}),
            "font": ([f for f in os.listdir(FONTS_DIR) if f.endswith('.ttf') or f.endswith('.otf')], ),
            "font_size": ("INT", {"default": 50, "min": 1, "max": 1024}),                
            "font_color": (COLORS,), 
        }

    RETURN_TYPE = "IMAGE"
    FUNCTION ="overlay_text"
    OUTPUT_NODE = True
    
    CATEGORY = "ecjojo_example"
    
    def overlay_text(self, image, text, font, font_size, font_color):
        # Load the image
        img = Image.open(image)
        draw = ImageDraw.Draw(img)

        # Load the font
        font_path = os.path.join(FONTS_DIR, font)
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text width and height
        text_width, text_height = draw.textsize(text, font=font)

        # Calculate position (example: center of the image)
        width, height = img.size
        position = ((width - text_width) / 2, (height - text_height) / 2)

        # Draw the text on the image
        draw.text(position, text, fill=color_mapping[font_color], font=font)

        # Save or return the image
        # img.save('output_image_path.png') # Example to save the image
        return img  # Assuming you want to return the PIL Image object