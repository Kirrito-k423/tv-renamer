import global_variable as glv
import os
from tsjPython.tsjCommonFunc import *

def previewWithOffset(prefix_dict, suffix_dict, media_type_list, offset_num):
    rename_dict = dict()
    for episode_id, candidate_prefix in prefix_dict.items():
    # for episode_id in episodes_list:
        for media_type in media_type_list:
            suffix_name = suffix_dict[episode_id] + media_type
            # [FreeSub&VCB-S&ANK-Raws] Noragami Aragoto [OAD
            ic(suffix_name)
            id2str = '%02d' % episode_id
            check_file_name = candidate_prefix + id2str + suffix_name
            if checkFile(check_file_name):
                print(colored('\u2714', 'green'), end = " ")
                print(colored("{}".format(check_file_name), 'magenta'), end = "")
                print(colored(' -> ', 'white'), end = "")
                dest_file_name = destFileName(candidate_prefix, suffix_name, '%02d' % (episode_id-offset_num))
                print(colored("{}".format(dest_file_name), 'green'))
                rename_dict[check_file_name]=dest_file_name
            else:
                id2str = str(episode_id)
                if checkFile(check_file_name):
                    print(colored('\u2714', 'green'), end = " ")
                    print(colored("{}".format(check_file_name), 'magenta'), end = "")
                    print(colored(' -> ', 'white'), end = "")
                    dest_file_name = destFileName(candidate_prefix, suffix_name, '%02d' % (episode_id-offset_num))
                    print(colored("{}".format(dest_file_name), 'green'))
                    rename_dict[check_file_name]=dest_file_name
                else:
                    print(colored('\u2718', 'red'), end = " ")
                    print(colored("{}".format(check_file_name), 'red'))   
    return rename_dict

def preview(prefix_dict, suffix_dict, media_type_list):
    rename_dict = dict()
    for episode_id, candidate_prefix in prefix_dict.items():
    # for episode_id in episodes_list:
        for media_type in media_type_list:
            suffix_name = suffix_dict[episode_id] + media_type
            id2str = '%02d' % episode_id
            check_file_name = candidate_prefix + id2str + suffix_name
            if checkFile(check_file_name):
                print(colored('\u2714', 'green'), end = " ")
                print(colored("{}".format(check_file_name), 'magenta'), end = "")
                print(colored(' -> ', 'white'), end = "")
                dest_file_name = destFileName(candidate_prefix, suffix_name, id2str)
                print(colored("{}".format(dest_file_name), 'green'))
                rename_dict[check_file_name]=dest_file_name
            else:
                id2str = str(episode_id)
                if checkFile(check_file_name):
                    print(colored('\u2714', 'green'), end = " ")
                    print(colored("{}".format(check_file_name), 'magenta'), end = "")
                    print(colored(' -> ', 'white'), end = "")
                    dest_file_name = destFileName(candidate_prefix, suffix_name, '%02d' % episode_id)
                    print(colored("{}".format(dest_file_name), 'green'))
                    rename_dict[check_file_name]=dest_file_name
                else:
                    print(colored('\u2718', 'red'), end = " ")
                    print(colored("{}".format(check_file_name), 'red'))   
    return rename_dict

def checkFile(filename):
    return os.path.exists(glv._get("path")+'\\'+filename)

def destFileName(candidate_prefix, candidate_suffix, id2str):
    return "S{}E{} {}{}".format('%02d' % glv._get("season"),id2str,candidate_prefix,candidate_suffix)