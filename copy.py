import os
import shutil

# 指定源目录路径
source_directory = '/Users/zyb/kidedu/笛子/张维良'
# 指定目标目录路径
destination_directory = '/Users/zyb/kidedu/笛子/zhangweiliang_mp4'

# 创建目标目录（如果不存在）
os.makedirs(destination_directory, exist_ok=True)

# 遍历源目录及其子目录
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith('.mp4'):
            # 获取文件的完整路径
            file_path = os.path.join(root, file)
            # 生成目标路径
            destination_path = os.path.join(destination_directory, file)
            # 拷贝文件
            shutil.copy(file_path, destination_path)
            print(f'已拷贝: {file_path} 到 {destination_path}')
