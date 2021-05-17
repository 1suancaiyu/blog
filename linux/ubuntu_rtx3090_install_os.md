# 戴尔台式机3640，显卡RTX3060，安装Ubuntu20.04，驱动问题

## 1. 制作u盘启动盘，略
## 2. 系统安装
插入u盘，开机出现dell log按F12进入BIOS，选择u盘，进入grab，选择ubuntu回车，进入系统安装界面。选择最小安装，只需要选择这一个就可以，其他略。

## 3. 驱动问题，注意避坑
我遇到的问题：系统安装成功后，重启，但是黑屏，有一个白点在那里闪烁，网上很多教程说进入grab界面后按e，禁止什么驱动，我试了很多次，无果。

这是dell官方给出的回答，“将显示器连接到独立 GPU 卡后重新安装第三方显卡驱动程序可能会解决问题，但建议的解决方案是重新安装 OEM 映像。”

https://www.dell.com/support/kbdoc/zh-cn/000132211/ubuntu-18-04-%E6%97%A0%E6%B3%95%E5%90%AF%E5%8A%A8%E5%B9%B6%E5%87%BA%E7%8E%B0%E9%BB%91%E5%B1%8F

**最终我是尝试将视频线接口接到应该是cpu集显的视频输出口，就可以显示系统界面了，一般在主机的上面那一排视频输出接口。**


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

```
#安装依赖
sudo dpkg --add-architecture i386
sudo apt install build-essential libc6:i386
sudo chmod a+x NVIDIA-Linux-x86_64*
sudo ./NVIDIA-Linux-x86_64* -no-x-check -no-nouveau-check -no-opengl-files

 
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
