@echo off

REM 提示用户输入要提交的文件/目录
set /p path="请输入要提交的文件/目录路径: "

REM 提示用户输入 commit message
set /p message="请输入 commit message: "

REM 提示用户输入 GitHub 仓库的 URL
set /p url="请输入 GitHub 仓库的 URL: "

REM 设置 Git 可执行文件路径
set "GIT_PATH=D:\Git\bin"

REM 初始化 Git 仓库
"%GIT_PATH%\git.exe" init

REM 添加文件/目录到暂存区
"%GIT_PATH%\git.exe" add %path%

REM 提交更改
"%GIT_PATH%\git.exe" commit -m "%message%"

REM 添加远程仓库
"%GIT_PATH%\git.exe" remote add origin %url%

REM 拉取最新的更改
"%GIT_PATH%\git.exe" pull origin master

REM 推送更改到 GitHub
"%GIT_PATH%\git.exe" push -u origin master

echo Done!
pause

