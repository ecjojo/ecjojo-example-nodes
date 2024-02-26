import json

class FilenameNode:
    
    FORMAT = ["yyyy-MM-dd", "hhmmss"] 
  
    @classmethod
    def INPUT_TYPES(s): 
        return {
            "required": {
                "CustomPath": ("BOOL", {"default":False}),
                "FolderName": ("STRING", {"default":"%date:yyyy-MM-dd%"}),
                "ImageName": ("STRING", {"default":"Image"}),
                "Custom_FolderName": (FilenameNode.FORMAT, {"yyyy-MM-dd"}),
                "Custom_ImageName": (FilenameNode.FORMAT, {"default":"Image"}),
            },
       }

    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('Filename_Prefix',)
    OUTPUT_NODE = True
  
    FUNCTION = "Filename"
    CATEGORY = "ecjojo_example"

    def FileName(self, CustomPath, FolderName, ImageName, Custom_FolderName, Custom_ImageName):
        if CustomPath:
            return (f"{Custom_FolderName}/{Custom_ImageName}",)

        mapping = {
            "yyyy-MM-dd": "%date:yyyy-MM-dd%", 
            "hhmmss": "%hhmmss%"}
        
        out_FolderName = mapping.get(FolderName)
        out_ImageName = mapping.get(ImageName)

        return (f"{out_FolderName}/{out_ImageName}",)
    
#data_string="%NodeName.node_value%"

# "Image",
#                     "%Empty Latent Image.width%x%Empty Latent Image.height%",
#                     "%KSampler.seed%"
