screen -S

Ctrl+a d

screen -r

screen -ls

exit 


screen -D -r ＜session-id>


Attached

Detached


用 screen -ls, 显式当前状态为Attached， 但当前没有用户登陆些会话。screen此时正常状态应该为(Detached)，此时用screen -r ，怎么也登不上。最后找到解决方法：-D -r 先踢掉前一用户，再登陆。

screen -X -S [screen id] quit
kill one stuck session


3、常用快捷键
Ctrl+a c ：在当前screen会话中创建窗口
Ctrl+a w ：窗口列表
Ctrl+a n ：下一个窗口
Ctrl+a p ：上一个窗口
Ctrl+a 0-9 ：在第0个窗口和第9个窗口之间切换

