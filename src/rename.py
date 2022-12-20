import os
import global_variable as glv

def apply_rename(rename_dict):
    for key, value in rename_dict.items():
        src_name = glv._get("path")+'\\'+ key
        dest_name = glv._get("path")+'\\'+ value
        os.rename(src_name, dest_name)