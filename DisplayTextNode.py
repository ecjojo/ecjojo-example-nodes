class DisplayTextNode:
  
  @classmethod
  def INPUT_TYPES(s): 
    return {
      "required": {        
        "text": ("STRING", {"forceInput": True}),     
        },
      "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
      }
  
  FUNCTION = "display_text"

  def display_text(self, text, prompt=None, extra_pnginfo=None):
      return {"ui": {"string": [text,]}, "result": (text,)}
    
  RETURN_TYPES = ('STRING',)
  RETURN_NAMES = ('text',)
  OUTPUT_NODE = True
  
  CATEGORY = "ecjojo_example"