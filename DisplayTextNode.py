class DisplayTextNode:
  
  @classmethod
  def INPUT_TYPES(cls): 
    return {
      "required": {        
        "text": ("STRING", {"forceInput": True}),     
        },
      "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
      }

  RETURN_TYPES = ('STRING',)
  RETURN_NAMES = ('text',)
  OUTPUT_NODE = True
  
  FUNCTION = "display_text"
  CATEGORY = "ecjojo_example"

  def display_text(self, text, prompt=None, extra_pnginfo=None):
      return {"ui": {"string": [text,]}, "result": (text,)}