rem 先删除任务
schtasks  /Delete /F /tn  synctooss
rem 添加任务
set BASE_DIR=%~dp0
schtasks  /create  /tn  synctooss   /sc  minute  /mo  15 /tr  %BASE_DIR%\start.cmd