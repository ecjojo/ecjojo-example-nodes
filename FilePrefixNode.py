class FilePrefixNode:
  
    @classmethod
    def INPUT_TYPES(s): 
        return {
            "required": {
                "CustomFolderBool":("BOOLEAN",{"default":False}),
                "CustomFolderName":("STRING",{"default":"CustomName"}),
                "FolderFormat": (["%date:yyyy-MM-dd%", 
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

    def PrefixFormat(self, FolderFormat,ImageName,CustomFolderBool,CustomFolderName):
        if CustomFolderBool ==True:
            custom_output = CustomFolderName+"/"+ImageName,
            return (custom_output,)
            
        else:
            if FolderFormat == "%date:yyyy-MM-dd%":
                output = "%date:yyyy-MM-dd%/"+ImageName,
                
            elif FolderFormat == "%date:dd-MM-yyyy%":
                output = "%date:dd-MM-yyyy%/"+ImageName,
                
            elif FolderFormat == "%date:dd/MM/yyyy%":
                output = "%date:dd/MM/yyyy%/"+ImageName,
                
            elif FolderFormat == "%date:yyyy-MM-dd hh:mm:ss%":
                output = "%date:yyyy-MM-dd hh:mm:ss%/"+ImageName,
                
            elif FolderFormat == "%date:yyyyMMddhhmmss%": 
                output = "%date:yyyyMMddhhmmss%/"+ImageName,
            
            return output,
    
#data_string="%NodeName.node_value%"
#"%Empty Latent Image.width%x%Empty Latent Image.height%",
#"%KSampler.seed%"
#"%date:yyyy-MM-dd hh:mm:ss%",
#"%date:yyyyMMddhhmmss%",