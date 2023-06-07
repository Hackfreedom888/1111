import subprocess

# 提示用户输入要提交的文件/目录
path = input("请输入要提交的文件/目录路径: ")

# 初始化 Git 仓库
subprocess.run(['git', 'init'])

# 配置用户名和邮箱
username = input("请输入用户名: ")
email = input("请输入邮箱: ")
subprocess.run(['git', 'config', 'user.name', username])
subprocess.run(['git', 'config', 'user.email', email])

# 添加文件/目录到暂存区
subprocess.run(['git', 'add', path])

# 提示用户输入 commit message
message = input("请输入 commit message: ")

# 提交更改
subprocess.run(['git', 'commit', '-m', message])

# 提示用户输入 GitHub 仓库的 URL
url = input("请输入 GitHub 仓库的 URL: ")

# 添加远程仓库
subprocess.run(['git', 'remote', 'add', 'origin', url])

# 拉取最新的更改
subprocess.run(['git', 'pull', 'origin', 'master'])

# 推送更改到 GitHub
subprocess.run(['git', 'push', '-u', 'origin', 'master'])
