
import config
from input_process import inputParameters, isIceEnable
from Candidate import findCandidateList
from preview import preview, previewWithOffset
from tsjPython.tsjCommonFunc import *
from rename import apply_rename
import global_variable as glv

if __name__ == '__main__':
    args = inputParameters()
    isIceEnable(args.debug)
    # 正则寻找候选列表
    [prefix_dict, suffix_dict, media_type_list] = findCandidateList(args.path)
    # 预览修改效果
    rename_dict = preview(prefix_dict, suffix_dict, media_type_list)

    # 预览判断
    if glv._get("number") == 'yes':
        # 询问用户是否需要编号便宜
        colorPrint("[You Choose offset num option]If you want to use the above replace strategy:(y to continue)\
                    or \n (o to input offset num)","cyan")
        user_option = input()
        if user_option == 'y':
            apply_rename(rename_dict)
            passPrint("重命名完毕")
        elif user_option == 'o':
            colorPrint("Pleas input your offset num: ( -2 means S01E01 -> S01E03)","cyan")
            offset_num = int(input())
            rename_dict = previewWithOffset(prefix_dict, suffix_dict, media_type_list, offset_num)
            colorPrint("If you want to use the above replace strategy:(y to continue)","cyan")
            user_option = input()
            if user_option == 'y':
                apply_rename(rename_dict)
                passPrint("重命名完毕")
            else:
                errorPrint("QUIT!!!")
        else:
            errorPrint("QUIT!!!")
    
    