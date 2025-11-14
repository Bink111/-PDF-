
基于 Python+Tkinter+pikepdf 开发的PDF 批量解密工具，无需命令行操作，需知晓文件合法密码。支持多文件批量处理，兼容中文路径，适用于办公/个人 PDF 整理，高效解除密码保护编辑，依赖：pikepdf
本项目使用Python编写，需要事先安装并配置好Python环境。
使用源代码前请使用以下 pip 命令安装 pikepdf 。

pip install pikepdf

Python 3.1 及以上版本通常已预装 Tkinter，若未安装，可通过重新安装 Python 时勾选 “Tcl/Tk” 组件来添加。
Linux 系统（以Ubuntu为例）：打开终端，执行命令 

sudo apt-get install python3-tk 

macOS 系统：一般已预装，若需更新或修复，可通过 Homebrew 执行 

brew install python-tk 。

注意
只能破解只有编辑密码的PDF文件，无法破解查看PDF的打开密码。
