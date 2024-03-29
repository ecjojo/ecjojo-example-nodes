
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
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
        }

    FUNCTION = "random_value"

    def random_value(self, min_width, max_width,min_height,max_height, seed):
        
        np.random.seed(seed)
        
        width = np.random.randint(min_width, max_width)
        height = np.random.randint(min_height, max_height)

        return (width, height,)


    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    OUTPUT_NODE = True
    
    CATEGORY = "ecjojo_example"