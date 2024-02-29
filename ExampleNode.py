class ExampleNode:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {

                "int": ("INT", {
                    "default": 0,
                    "display": "number" }),
                
                "int_slider": ("INT", {
                    "default": 0, 
                    "min": 0, 
                    "max": 4096, 
                    "step": 64,
                    "display": "slider" }),
                
                "floa": ("FLOAT", {
                    "default": 1.0,
                    "round": False, 
                    "display": "number"}),
                
                "float_round": ("FLOAT", {
                    "default": 1.00,
                    "min": 0.00,
                    "max": 10.00,
                    "step": 0.001,
                    "round": 0.001, 
                    "display": "number"}),
                
                "string": ("STRING", {
                    "default": "Hello World!"}),
                
                "string_multiline_field": ("STRING", {
                    "multiline": True, 
                    "default": "Hello World!"}),
            },
        }
 
    RETURN_TYPES = ("INT","INT","FLOAT","FLOAT","STRING","STRING",)
    RETURN_NAMES = ("INT","INT_SLIDER","FLOAT","FLOAT_ROUND","STRING","STRING_MULTILINE",)
    OUTPUT_NODE = True
 
    FUNCTION = "example"
    CATEGORY = "ecjojo_example"
 
    def example(self,int,int_slider,float,float_round,string,string_multiline_field):
        
               
        return (int,int_slider,float,float_round,string,string_multiline_field)

