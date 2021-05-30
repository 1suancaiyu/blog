# install ssh
```
apt-get install openssh-server

#allow root login

"passwd root" setup a root passwd

sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

or edit the file
vim /etc/ssh/sshd_config
PermitRootLogin yes
PermitEmptyPasswords yes

service ssh enable
service ssh restart

安装netstat，查看sshd是否监听22端口
apt-get install net-tools
netstat -apn | grep ssh
```

## frp setup
git clone https://github.com/1suancaiyu/frp


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
