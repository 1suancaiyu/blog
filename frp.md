## 远程连接BCI工作站
实验室工作站通过 frp 和具有公网ip的远程服务器做了内网穿透，现可以在任意网络环境下通过域名  ``` bci.shuxi.wang``` 访问工作站，例如宿舍wifi和手机热点等，而不必须连接实验室局域网访问，当然局域网访问也是一直可行的，而且传输超过100M左右的大文件的时候，最好连接实验室的局域网，不然就是跑远程服务器流量（当然如果远程服务器没有流量限制的话，可以放开用）。

### 连接方法：
#### 1. ssh 工具
选用自己喜欢的ssh工具即可，例如mobaxterm，xshell等。
**mobaxterm** （推荐使用，连上ssh后也可以上传和下载文件）
软件下载和视频教程 http://note.youdao.com/s/PXxoiQNu  mobax那一项

<img src="mobaxterm_ssh.png" alt="mobaxterm_ssh" style="zoom:67%;" />

**xshell** 连接

<img src="xshell_ssh.png" alt="cmd_ssh" style="zoom: 67%;" />


#### 2. ssh 命令  
```shell
 ssh -oPort=3023 [usr_name]@bci.shuxi.wang
```
这里只需要把```usr_name```替换成自己的用户名就可以, 

例如：```ssh -oPort=3023 li_yun_long@bci.shuxi.wang```
例如Windows cmd 连接如图：
<img src="cmd_ssh.png" alt="cmd_ssh" style="zoom:67%;" />









## frp内网穿透实现方法

需要的东西：frp文件 + 带公网iP的服务器  + 域名（非必须）



### 1.  github网址和文件下载

github地址 https://github.com/fatedier/frp
安装包下载 https://github.com/fatedier/frp/releases
根据自己的系统下载对应的版本，一般下载```frp linux amd64``` 这个版本
解压到自己想放置的文件目录下
```tar -vxzf [文件名]```  解压

### 2. 编辑配置文件
（用我自己的配置文件举例，没有#注释的部分不用改）：
在远程服务器中只需修改 frps.ini 配置如下：（如果只想要实现ssh内网穿透的话）
```
[common]
bind_port = 7000
```
最后为了使这个frp进程持续运行，我采用**screen**命令的方法，使其保持进程运行，当然还有其他方法，目前先这样用。
服务器端输入命令
```screen  -S  frps```   名字可以自定义
```./frps -c frps.ini```

然后得到如下log表示运行成功

![frps_log](frps_log.png)

使用快捷键 ctrl + a + d（一直按着ctrl 先按a 再按 d）推出这个frps的screen 但是保持它的运行状态。
以后想查看这个frps的screen 可以用命令 sreen -ls 查看，screen -r frps 进入

本地服务器只需修改 frpc.ini 文件配置如下：
```
[common]
server_addr =  bci.shuxi.wang 
#这里可以写上远程服务器的公网ip，或者为了好记，可以用自己的域名用dns指向这个公网IP然
#后写上域名，以后就可以用域名访问了
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 3023  #端口号
```
同样建立一个名为 frpc  的 screen 方法如上



详细说明见frp中文说明文档 https://gofrp.org/docs/
screen 命令见 https://www.runoob.com/linux/linux-comm-screen.html