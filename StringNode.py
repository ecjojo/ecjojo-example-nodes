class StringNode:
  
  @classmethod
  def INPUT_TYPES(s): 
    return {
      "required": {        
        "textA": ("STRING", {"multiline": True,"default": ""}),     
        "textB": ("STRING", {"multiline": True,"default": ""}),   
        "textC": ("STRING", {"multiline": True,"default": ""}),   
        },
      }
  
  FUNCTION = "output"

  def output(self, textA,textB,textC):
      ouput_text = textA +","+ textB +","+ textC
      return ouput_text,
    
  RETURN_TYPES = ('STRING',)
  RETURN_NAMES = ('combin_text',)
  OUTPUT_NODE = True
  
  CATEGORY = "ecjojo_example"