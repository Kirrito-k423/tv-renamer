# tv-renamer


推荐：http://www.den4b.com/products/renamer

![](https://shaojiemike.oss-cn-hangzhou.aliyuncs.com/img/20230109200339.png)

（网上冲浪完之后才发现，已经有功能更全面的图形化界面的软件了。白写了，虽然也没写几个小时）
## Usage

```
python -m venv myVenv
.\myVenv\Scripts\activate # PowerShell active command
python ./src/main.py -d yes -p 'X:\Videos\anime\清恋[VCB-Studio] Seiren [Ma10p_1080p]' -pre yes -S 1
```
字幕文件批量重命名推荐SubRenamer

## Example

自动匹配集号的前缀
![](./fig/test3.gif)

手动输入集号的前缀
![](./fig/test4.gif)
## motivation

一开始玩jellyfin，用tinymediamanager刮削。发现会有如下的问题。

![](https://shaojiemike.oss-cn-hangzhou.aliyuncs.com/img/20221220160532.png)

其实github有些类似的 https://github.com/dbr/tvnamer。但还是不和我胃口

## To do
- [x] 文件夹下的识别出Episodes的编号，并重命名
- [ ] 支持查找theTVDB来重命名SP
- [ ] 不是脚本，变成python的可执行文件
