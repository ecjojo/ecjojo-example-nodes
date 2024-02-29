class HelloWorldNode:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
        }
 
    FUNCTION = "output"
 
    def output(self):
        HelloWorldText="Hello World!"
        return HelloWorldText,
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Hello_World_Text",)
    OUTPUT_NODE = True
    
    CATEGORY = "ecjojo_example"