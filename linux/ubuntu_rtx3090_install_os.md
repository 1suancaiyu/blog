# 戴尔台式机3640，显卡RTX3060，安装Ubuntu20.04，驱动问题

## 1. 制作u盘启动盘，略
## 2. 系统安装
插入u盘，开机出现dell log按F12进入BIOS，选择u盘，进入grab，选择ubuntu回车，进入系统安装界面。选择最小安装，只需要选择这一个就可以，其他略。

## 3. 驱动问题，注意避坑

### 开机小白点

#### 方法1
我遇到的问题：系统安装成功后，重启，但是黑屏，有一个白点在那里闪烁，网上很多教程说进入grab界面后按e，禁止什么驱动，我试了很多次，无果。

这是dell官方给出的回答，“将显示器连接到独立 GPU 卡后重新安装第三方显卡驱动程序可能会解决问题，但建议的解决方案是重新安装 OEM 映像。”

https://www.dell.com/support/kbdoc/zh-cn/000132211/ubuntu-18-04-%E6%97%A0%E6%B3%95%E5%90%AF%E5%8A%A8%E5%B9%B6%E5%87%BA%E7%8E%B0%E9%BB%91%E5%B1%8F

**最终我是尝试将视频线接口接到应该是cpu集显的视频输出口，就可以显示系统界面了，一般在主机的上面那一排视频输出接口。**

#### 方法2

1. 在ubuntu处按下e键，进入编辑。 在倒数第二行的样子，会看到 ro quiet splash $vt_handoff

2. 在splash 后面加入`nomodeset`就变为了 ro quiet splash nomodeset $vt_handoff

3. 然后按下 **F10**，输入登录密码就能进入桌面了。

   

### 内核问题
安装好ubuntu 20.04 后不要upgrade ，这样系统内核会升级，导致无法安装驱动安装好ubuntu 20.04 后不要upgrade ，这样系统内核会升级，导致无法安装驱动NVIDIA-Linux-x86_64-455.23.04_11.1_.run



## 3. 屏蔽开源驱动 nouveau
```
sudo vim /etc/modprobe.d/blacklist.conf

blacklist nouveau
options nouveau modeset=0
reboot
lsmod | grep nouveau
若没有输出，则禁用生效
```

## 4. 安装RTX3090驱动
官网链接
https://www.nvidia.cn/Download/index.aspx?lang=cn

sudo telinit 3 进入命令行界面


安装依赖
```
sudo dpkg --add-architecture i386
sudo apt install build-essential libc6:i386

binutils，GNU make，gcc
sudo apt install binutils make gcc g++
```

关闭图形化界面
```
init 3
sudo service lightdm stop
```
添加权限
sudo chmod a+x NVIDIA-Linux-x86_64*

开始安装

sudo ./NVIDIA-Linux-x86 -no-x-check -no-nouveau-check -no-opengl-files

```
#选项：
The distribution-provided pre-install script failed! Are you sure you want to continue? -> CONTINUE INSTALLATION

Would you like to register the kernel module souces with DKMS? This will allow DKMS to automatically build a new module, if you install a different kernel later? -> No

Nvidia's 32-bit compatibility libraries? -> No

Would you like to run the nvidia-xconfig utility to automatically update your x configuration so that the NVIDIA x driver will be used when you restart x? Any pre-existing x confile will be backed up -> YES
```

## 5. 检查是否安装成功
安装成功后，重启系统
**这个时候要将视频连接线连接到机箱下端的独立显卡处的视频输出接口，因为这个时候已经启用了RTX3090的驱动**
nvidia-smi检查显卡状态，可显示，表明驱动安装成功 




```
在linux 中卸载另一个系统工具 OS-Uninstaller 参考https://help.ubuntu.com/community/OS-Uninstaller

gparted 磁盘管理工具
```



## 卸载驱动

sudo sh ./NVIDIA-Linux-x86_64-xxx.run  --uninstall

$ nvidia-uninstall



## 其他问题

### bios 设置问题











