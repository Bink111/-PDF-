# PDF 批量解密编辑加密工具
基于 Python+Tkinter+pikepdf 开发的 PDF 批量解密加密编辑工具，无需命令行操作。

## 功能特点
- 支持多文件批量处理
- 兼容中文路径
- 适用于办公/个人 PDF 整理
- 高效解除 PDF 密码保护（仅支持编辑密码）

## 依赖环境
- Python
- 依赖库：pikepdf
- 图形库：Tkinter（Python 预装）

## 安装步骤
1. 先安装并配置好 Python 环境
2. 安装依赖库 pikepdf：
   	打开终端/命令提示符，执行以下命令：
   	```bash
   pip install pikepdf
	
3. 若电脑有多个 Python 版本，改用以下命令：
   ```bash
   pip3 install pikepdf
   
4. Tkinter 安装说明（默认已预装，未安装时按以下步骤操作）：

   Windows 系统：重新安装 Python，勾选「Tcl/Tk」组件即可

   Linux 系统（以 Ubuntu 为例）：打开终端执行：
  	 ```bash
   	sudo apt-get install python3-tk
  	 ```
   macOS 系统：若需修复 / 更新，通过 Homebrew 执行：
    ```bash
    brew install python-tk
    ```
   
## 注意事项
仅支持破解「编辑密码」（解除 PDF 的修改、复制、打印限制）
无法破解「打开密码」（无密码无法查看的 PDF 不支持）
