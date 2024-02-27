class DateFormatNode:
  
    @classmethod
    def INPUT_TYPES(cls): 
        return {
            "required": {
                "Format": (["yyyy-MM-dd", 
                            "dd-MM-yyyy",  
                            "dd/MM/yyyy",
                            "yyyy-MM-dd hh:mm:ss",
                            "yyyyMMddhhmmss",
                            ],),  
            },
       }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('DateFormat',)
    OUTPUT_NODE = True
  
    FUNCTION = "DateFormat"
    CATEGORY = "ecjojo_example"

    def DateFormat(self, Format):
        if Format == "yyyy-MM-dd":
            output = "%yyyy-MM-dd%"
            
        elif Format == "dd-MM-yyyy":
            output = "%dd-MM-yyyy%"
            
        elif Format == "dd/MM/yyyy":
            output = "%dd/MM/yyyy%"
            
        elif Format == "yyyy-MM-dd hh:mm:ss":
            output = "%yyyy-MM-dd hh:mm:ss%"
            
        elif Format == "yyyyMMddhhmmss": 
            output = "%yyyyMMddhhmmss%"
            
        return (output,)
    
#data_string="%NodeName.node_value%"
#"%Empty Latent Image.width%x%Empty Latent Image.height%",
#"%KSampler.seed%"
