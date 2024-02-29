class EmptyNode:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
        }

    FUNCTION = "output"
 
    def output(self):
        return ()
    
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    
    CATEGORY = "ecjojo_example"