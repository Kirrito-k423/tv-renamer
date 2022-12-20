# tv-renamer

## To do
- [ ] 文件夹下的识别出Episodes的编号，并重命名
- [ ] 支持查找theTVDB来重命名SP
- [ ] 不是脚本，变成python的可执行文件

## Usage

```
python -m venv myVenv
.\myVenv\Scripts\activate # PowerShell active command
python ./src/main.py -d yes -p 'X:\Videos\anime\清恋[VCB-Studio] Seiren [Ma10p_1080p]' -pre yes -S 1
```
字幕文件批量重命名推荐SubRenamer

## motivation

一开始玩jellyfin，用tinymediamanager刮削。发现会有![](https://shaojiemike.oss-cn-hangzhou.aliyuncs.com/img/20221220160532.png)的问题。

其实github有些类似的 https://github.com/dbr/tvnamer

。但还是不和我胃口