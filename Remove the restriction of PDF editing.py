import tkinter
from tkinter import filedialog
import pikepdf
import os

def select_input_files():
    root = tkinter.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        title="请选择一个或多个合法拥有且你知道密码的 PDF 文件",
        filetypes=[("PDF 文件","*.pdf"),("所有文件","*.*")]
    )
    return list(files)

def select_output_directory():
    root = tkinter.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(
        title="请选择输出目录（解密后的文件将保存在这里）"
    )
    return directory

def process_file(input_path, output_dir, password):
    # 获取原文件名
    _, base_name = os.path.split(input_path)
    # 输出路径：用相同的文件名，但在输出目录中
    output_path = os.path.join(output_dir, base_name)
    try:
        with pikepdf.open(input_path, password=password) as pdf:
            pdf.save(output_path)
        print(f"成功：\"{input_path}\" → \"{output_path}\"")
    except pikepdf._qpdf.PasswordError:
        print(f"失败（密码错误）：\"{input_path}\"")
    except Exception as e:
        print(f"失败（其它错误）：\"{input_path}\" —— {e}")

def main():
    print("请选择你想解密的 PDF 文件（可多选）。\n")
    input_files = select_input_files()
    if not input_files:
        print("未选择任何文件，程序结束。")
        return

    print("\n请选择解密后文件保存的输出目录：")
    output_dir = select_output_directory()
    if not output_dir:
        print("未选择输出目录，程序结束。")
        return

    password = input("请输入这些 PDF 的打开密码（注意：此脚本假设所有选中文件使用相同密码）：").strip()

    print("\n开始批量处理 …\n")
    for path in input_files:
        process_file(path, output_dir, password)

    print("\n全部处理完成。")
    input("按回车键退出。")

if __name__ == "__main__":
    main()