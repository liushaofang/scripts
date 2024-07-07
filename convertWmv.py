import os
import subprocess

# 指定目录路径
directory_path = os.getcwd()

# 获取目录中的文件列表
files = os.listdir(directory_path)

# 遍历文件列表并转换 rmvb 文件为 mp4
for file in files:
    if file.endswith('.wmv'):
        file_path = os.path.join(directory_path, file)
        output_file = os.path.splitext(file_path)[0] + '.mp4'

        # 使用 ffmpeg 命令转换文件格式
        # 使用 ffmpeg 命令转换文件格式，给文件路径加上引号
        command = f'ffmpeg -i "{file_path}" -c:v h264 -c:a aac "{output_file}"'
        subprocess.run(command, shell=True)
        print(f'已转换: {file} 为 {output_file}')
