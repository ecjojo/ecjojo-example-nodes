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
  
    FUNCTION = "output"

    def output(self, FolderFormat,ImageName,CustomFolderBool,CustomFolderName):
        if CustomFolderBool ==True:
            custom_output = CustomFolderName+"/"+ImageName,
            return (custom_output,)
            
        else:
            if FolderFormat == "%date:yyyy-MM-dd%":
                fotmat_output = "%date:yyyy-MM-dd%/"+ImageName,
                
            elif FolderFormat == "%date:dd-MM-yyyy%":
                fotmat_output = "%date:dd-MM-yyyy%/"+ImageName,
                
            elif FolderFormat == "%date:dd/MM/yyyy%":
                fotmat_output = "%date:dd/MM/yyyy%/"+ImageName,
            
            return fotmat_output,
        
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('filename_prefix(FolderName/ImageName)',)
    OUTPUT_NODE = True
    
    CATEGORY = "ecjojo_example"
    
#data_string="%NodeName.node_value%"
#"%Empty Latent Image.width%x%Empty Latent Image.height%",
#"%KSampler.seed%"
#"%date:yyyy-MM-dd hh:mm:ss%",
#"%date:yyyyMMddhhmmss%",

            # elif FolderFormat == "%date:yyyy-MM-dd hh:mm:ss%":
            #     fotmat_output = "%date:yyyy-MM-dd hh:mm:ss%/"+ImageName,
                
            # elif FolderFormat == "%date:yyyyMMddhhmmss%": 
            #     fotmat_output = "%date:yyyyMMddhhmmss%/"+ImageName,