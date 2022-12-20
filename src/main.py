
import config
from input_process import inputParameters, isIceEnable
from Candidate import findCandidateList
from preview import preview
from tsjPython.tsjCommonFunc import *
from rename import apply_rename

if __name__ == '__main__':
    args = inputParameters()
    isIceEnable(args.debug)
    # 正则寻找候选列表
    [prefix_dict, suffix_dict] = findCandidateList(args.path)
    # 预览修改效果
    rename_dict = preview(prefix_dict, suffix_dict)

    # 预览判断
    colorPrint("If you want to use the above replace strategy:(y to continue)","cyan")
    user_option = input()
    if user_option == 'y':
        apply_rename(rename_dict)
        passPrint("重命名完毕")
    else:
        errorPrint("QUIT!!!")