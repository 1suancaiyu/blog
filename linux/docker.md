# build docker
```
nvidia-docker run -it -p [local port]:[docker port] --ipc=host -v [dokcer save dir]:/[share floder name] --name [docker name] [docker images id]
```

```
deepo
nvidia-docker run -it -p 1920:22 --ipc=host -v /home/sci/private/wang_shu_xi:/wsx --name qln_deepo_matlab cf60a305ba7b
```



在容器中执行bash命令

```
docker exec -it [docker id] /bin/bash
```



# 创建docker镜像，并内网穿透，通过ssh登录

## install ssh
```
apt-get install openssh-server
启动之前需手动创建/var/run/sshd，不然启动sshd的时候会报错
mkdir -p /var/run/sshd
sshd以守护进程运行
/usr/sbin/sshd -D &
安装netstat，查看sshd是否监听22端口
apt-get install net-tools
netstat -apn | grep ssh
```

## allow root login
```
修改sshd-config允许root登陆
sed -i 's+PermitRootLogin prohibit-password+PermitRootLogin yes' /etc/ssh/sshd-config

vim /etc/ssh/sshd_config
PermitEmptyPasswords yes

restart ssh
找到pid
ps -aux | grep ssh
kill -9 pid
/usr/sbin/sshd -D &
```

## frp setup



## xrdp setup
```
sudo apt update
sudo apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils
apt install xrdp

systemctl status xrdp

if hit like this
System has not been booted with systemd as init system (PID 1). Can't operate.

change commadn "systemctl" to "service"
systemctl start xrdp -> service xrdp start
```

