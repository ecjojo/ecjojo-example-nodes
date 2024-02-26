
import numpy as np

class RandomSizeNode:

    @classmethod
    def INPUT_TYPES(s): 
        return {
            "required": {
                "min_width": ("INT", {"default": 512}),
                "max_width": ("INT", {"default": 1024}),
                "min_height": ("INT", {"default": 512}),
                "max_height": ("INT", {"default": 1024}),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "random_value"

    CATEGORY = "ecjojo_example"

    def random_value(self, min_width, max_width,min_height,max_height):
        
        width = np.random.randint(min_width, max_width)
        height = np.random.randint(min_height, max_height)

        return (width, height,)

