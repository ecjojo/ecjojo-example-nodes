class HelloWorldNode:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            },
        }
 
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Hello_World_Text",)
    OUTPUT_NODE = True
 
    FUNCTION = "output_HelloWorld"
    CATEGORY = "ecjojo_example"
 
    def output_HelloWorld(self):
        HelloWorldText="Hello World!"
        print (HelloWorldText)
        return (HelloWorldText,)