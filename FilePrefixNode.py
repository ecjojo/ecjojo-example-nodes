class FilePrefixNode:
  
    @classmethod
    def INPUT_TYPES(cls): 
        return {
            "required": {
                "CustomFolderBool":("BOOLEAN",{"default":False}),
                "CustomFolderName":("STRING",{"default":"CustomName"}),
                "FolderName": (["%date:yyyy-MM-dd%", 
                            "%date:dd-MM-yyyy%",  
                            "%date:dd/MM/yyyy%",
                            ],),
                "ImageName": ("STRING", {"default": "Image"}),
            },
       }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('filename_prefix(FolderName/ImageName)',)
    OUTPUT_NODE = True
  
    FUNCTION = "PrefixFormat"
    CATEGORY = "ecjojo_example"

    def PrefixFormat(self, Format,ImageName,CustomFolderBool,CustomFolderName):
        if CustomFolderBool ==True:
            custom_output = CustomFolderName+"/"+ImageName,
            return (custom_output,)
            
        else:
            if Format == "%date:yyyy-MM-dd%":
                output = "%date:yyyy-MM-dd%/"+ImageName,
                
            elif Format == "%date:dd-MM-yyyy%":
                output = "%date:dd-MM-yyyy%/"+ImageName,
                
            elif Format == "%date:dd/MM/yyyy%":
                output = "%date:dd/MM/yyyy%/"+ImageName,
                
            elif Format == "%date:yyyy-MM-dd hh:mm:ss%":
                output = "%date:yyyy-MM-dd hh:mm:ss%/"+ImageName,
                
            elif Format == "%date:yyyyMMddhhmmss%": 
                output = "%date:yyyyMMddhhmmss%/"+ImageName,
            
            return (output,)
    
#data_string="%NodeName.node_value%"
#"%Empty Latent Image.width%x%Empty Latent Image.height%",
#"%KSampler.seed%"
#"%date:yyyy-MM-dd hh:mm:ss%",
#"%date:yyyyMMddhhmmss%",