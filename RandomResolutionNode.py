class RandomResolutionNode:
    """
    A class to get the width and height based on the resolution and aspect.
    """
    RESOLUTIONS = {
        "Cinematic": (1536, 640),
        "Widescreen": (1344, 768),
        "Photo": (1216, 832),
        "Portrait": (1152, 896),
        "Square": (1024, 1024)
    }
    
    ASPECT = ["Horizontal", "Vertical"]

    @classmethod
    def INPUT_TYPES(cls): 
        """
        Returns the input types required for this node.
        """
        return {
            "required": {
                "resolution": (list(cls.RESOLUTIONS.keys()), {"default": "Square"}),
                "aspect": (cls.ASPECT, {"default": "Horizontal"})
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_value"

    CATEGORY = "ecjojo_example"

    def get_value(self, resolution, aspect):
        """
        Returns the width and height based on the resolution and aspect.
        """
        if resolution not in self.RESOLUTIONS:
            raise ValueError(f"Resolution '{resolution}' is not supported.")
        if aspect not in self.ASPECT:
            raise ValueError(f"Aspect '{aspect}' is not supported.")
        
        width, height = self.RESOLUTIONS[resolution]
        if aspect == "Vertical":
            return (height, width)
        return (width, height)