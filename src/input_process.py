from icecream import ic
from icecream import install
import global_variable as glv
from tsjPython.tsjCommonFunc import *
import argparse

def inputParameters():
    parser = argparse.ArgumentParser()
    parser.description = "please enter some parameters"
    parser.add_argument(
        "-d",
        "--debug",
        help="是否打印Debug信息 is print debug informations",
        dest="debug",
        type=str,
        choices=["yes", "no"],
        default="no",
    )
    parser.add_argument(
        "-p",
        "--path",
        help="批量重命名文件的目录",
        dest="path",
        type=str,
        required=True
    )
    parser.add_argument(
        "-S",
        "--season",
        help="节目的季，默认第一季",
        dest="season",
        type=int,
        default=1
    )

    args = parser.parse_args()

    glv._set("debug",args.debug)
    glv._set("path",args.path)
    glv._set("season",args.season)
    passPrint("parameter debug is : %s " % args.debug)
    passPrint("parameter path is : %s " % args.path)
    passPrint("parameter season is : %s " % args.season)
    print("")
    return args

def isIceEnable(isYes):
    install()
    ic.configureOutput(prefix='Debug -> ', outputFunction=yellowPrint)
    if isYes=="yes" : 
        ic.enable()
    else:
        ic.disable()