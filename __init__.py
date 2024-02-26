"""
Author: ecjojo
Title: ComfyUI Custom Nodes Example
File: __init__.py
Copyright (c) 2024 ecjojo
"""
__VERSION__ = "0.1.0"

import os, sys, filecmp, shutil, __main__
python = sys.executable
extentions_folder = os.path.join(os.path.dirname(os.path.realpath(__main__.__file__)),
                                 "web" + os.sep + "extensions" + os.sep + "ecjojo_example_nodes")
javascript_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
# --------- WEB ---------- #
if not os.path.exists(extentions_folder):
    print('Making the "web\extensions\ecjojo_example_nodes" folder')
    os.mkdir(extentions_folder)
    
result = filecmp.dircmp(javascript_folder, extentions_folder)

if result.left_only or result.diff_files:
    print('Update to javascript files detected')
    file_list = list(result.left_only)
    file_list.extend(x for x in result.diff_files if x not in file_list)
    
    for file in file_list:
        print(f'Copying {file} to extensions folder')
        src_file = os.path.join(javascript_folder, file)
        dst_file = os.path.join(extentions_folder, file)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_file)



#INPORT NODES
from .EmptyNode import EmptyNode
from .DisplayTextNode import DisplayTextNode
from .HelloWorldNode import HelloWorldNode
#from .FilenameNode import FilenameNode
#from .RandomResolutionNode import RandomResolutionNode

# ------- MAPPING ------- #
NODE_CLASS_MAPPINGS = { 
    "EmptyNode_Example": EmptyNode,
    "HelloWorldNode_Example": HelloWorldNode,
    "DisplayTextNode_Example": DisplayTextNode,
   # "FilenameNode_Example": FilenameNode,
   #"RandomResolutionNode_Example": RandomResolutionNode,
}

NODE_DISPLAY_NAME_MAPPINGS = { 
    "EmptyNode_Example": "A Empty Node (ecjojo)",
    "HelloWorldNode_Example": "Hello World Node (ecjojo)",
    "DisplayTextNode_Example": "Display Text Node (ecjojo)",
    #"FilenameNode_Example": "Filename Node (ecjojo)",
    #"RandomResolutionNode_Example": "Random Resolution Node (ecjojo)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
