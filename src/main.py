
import config
from input_process import inputParameters, isIceEnable
from Candidate import findCandidateList
from preview import preview

if __name__ == '__main__':
    args = inputParameters()
    isIceEnable(args.debug)
    # 正则寻找候选列表
    [candidate_prefix, candidate_suffix, episodes_list] = findCandidateList(args.path)
    # 预览修改效果
    preview(candidate_prefix, candidate_suffix, episodes_list)