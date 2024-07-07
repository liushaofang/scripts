import os
import subprocess

# 指定包含要拼接的 mp4 文件的目录路径
source_directory = '/Users/zyb/kidedu/笛子/张维良/笛子基础视频教程（CD1）'
# 指定输出文件路径
output_file = '/Users/zyb/kidedu/笛子/张维良/笛子基础视频教程（CD1）/01_Flute_Playing.mp4'

# 获取目录中的 mp4 文件列表并排序（确保按顺序拼接）
files = sorted([f for f in os.listdir(source_directory) if f.endswith('.mp4')])

# 创建包含要拼接的文件列表的文本文件
with open('files_to_concat.txt', 'w') as file_list:
    for file in files:
        file_path = os.path.join(source_directory, file)
        file_list.write(f"file '{file_path}'\n")

# 使用 ffmpeg 拼接文件
command = f'ffmpeg -f concat -safe 0 -i files_to_concat.txt -c copy "{output_file}"'
subprocess.run(command, shell=True)

# 删除临时的文件列表文本文件
# os.remove('files_to_concat.txt')

print(f'已拼接文件，输出文件为: {output_file}')
