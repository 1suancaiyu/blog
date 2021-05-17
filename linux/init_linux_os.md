# install ssh
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
edit "sshd-config" allow root login

"passwd root" setup a root passwd

sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

or edit the file
vim /etc/ssh/sshd_config
PermitRootLogin yes
PermitEmptyPasswords yes

# restart ssh
ps -aux | grep ssh
kill
/usr/sbin/sshd -D &
```

## frp setup



## xrdp setup
```
sudo apt update
sudo apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils
apt install xrdp
systemctl status xrdp

# error: failed to execute default terminal emulator
apt-get install xfce4-terminal
update-alternatives --config x-terminal-emulator
Select xfce4-terminal.



sudo update-alternatives --config x-session-manager
echo gnome-session > ~/.xsession
echo xfce4-session > ~/.xsession
sudo dpkg-reconfigure gdm3
```
