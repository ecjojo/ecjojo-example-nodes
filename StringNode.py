class StringNode:
  
  @classmethod
  def INPUT_TYPES(cls): 
    return {
      "required": {        
        "textA": ("STRING", {"multiline": True}),     
        "textB": ("STRING", {"multiline": True}),   
        "textC": ("STRING", {"multiline": True}),   
        },

      }

  RETURN_TYPES = ('STRING',)
  RETURN_NAMES = ('text',)
  OUTPUT_NODE = True
  
  FUNCTION = "output"
  CATEGORY = "ecjojo_example"

  def output(self, textA,textB,textC):
      text = textA +","+ textB +","+ textC
      return {"text": text}

