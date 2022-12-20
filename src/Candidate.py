
import os
import re
import global_variable as glv
from tsjPython.tsjCommonFunc import *

def findCandidateList(path):
    file_name_list=os.listdir(path)
    ic(file_name_list)
    return regexCandidateList(file_name_list)

def regexCandidateList(file_name_list):
    [tmp_prefix, tmp_suffix] = findCandidatePrefixsuffix(file_name_list)
    episodes_list = findEpisodesList(file_name_list,tmp_prefix, tmp_suffix)
    return [tmp_prefix, tmp_suffix, episodes_list]

def findCandidatePrefixsuffix(file_name_list):
    count = 1
    prefix = ''
    suffix = ''
    media_type = ''
    for file_name in file_name_list:
        matchObj = re.match(glv._get("regex_format"), file_name)
        if matchObj:
            ic(matchObj.group())
            ic(matchObj.group(1))
            ic(matchObj.group(3))
            ic(matchObj.group(4))
            if prefix == matchObj.group(1) and suffix == matchObj.group(3) and \
                media_type == matchObj.group(4):
                count += 1
                ic(count)
            else:
                count = 1
                prefix = matchObj.group(1)
                suffix = matchObj.group(3)
                media_type = matchObj.group(4)
        if count > 3:
            passPrint("find a Candidate Prefix & suffix")
            # errorPrint(, end = "")
            print(colored("{}".format(prefix), 'red'), end = "")
            print(colored("XX", 'yellow'), end = "")
            errorPrint("{}{}".format(suffix,media_type))
            break
    return [prefix, suffix+media_type]


def findEpisodesList(file_name_list,tmp_prefix, tmp_suffix):
    episodes_list = []
    regex_prefix = toRegex(tmp_prefix)
    regex_suffix = toRegex(tmp_suffix)
    regex_for_episodes = "{}([0-9]*){}".format(regex_prefix,regex_suffix)
    ic(regex_for_episodes)
    for file_name in file_name_list:
        matchObj = re.match(regex_for_episodes, file_name)
        if matchObj:
            episodes_num = int(matchObj.group(1))
            print(colored("{}".format(episodes_num), 'yellow'), end = " ")
            episodes_list.append(episodes_num)
    print("")
    return episodes_list

def toRegex(String):
    regex_string = ''
    for character in String:
        if character == '[' or character == ']':
            regex_string += '\\'
        regex_string += character
    ic(regex_string)
    return regex_string
