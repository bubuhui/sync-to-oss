rem 先删除任务
schtasks  /Delete /F /tn  synctooss
rem 添加任务
schtasks  /create  /tn  synctooss /tr  C:\Users\evan\PycharmProjects\sync-to-oss\start.cmd  /sc  DAILY /st  12:00:00