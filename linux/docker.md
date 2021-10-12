# 安装Docker

此处安装还参考了：[官网指引](https://docs.docker.com/engine/install/ubuntu/)

1. Update the apt package index and install packages to allow apt to use a repository over HTTPS:

   ```shell
   sudo apt-get update
   
   sudo apt-get install \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg-agent \
       software-properties-common
   ```

2. Add Docker’s official GPG key:

   ```shell
   curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
   ```

   Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

   ```
   sudo apt-key fingerprint 0EBFCD88
   ```

3. Use the following command to set up the stable repository.

   ```shell
   sudo add-apt-repository \
      "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
      $(lsb_release -cs) \
      stable"
   ```

4. Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:

   ```shell
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

5. 安装最新版本的Docker CE

   ```shell
   sudo apt-get install -y docker-ce
   ```

6. 验证Docker CE正确安装（可选，之后更换存储位置后建议将默认位置/var/lib/docker删除）

   ```shell
   sudo docker run hello-world
   ```


# 安装nvidia-docker2

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html



此处安装还参考了：[官网指引](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

1. Setup the stable repository and the GPG key:

```shell
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
      && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

在执行这一步以及后面的操作时遇到问题：“gpg: 找不到有效的 OpenPGP”、“E: 无法定位软件包 nvidia-docker2”。[解决方案](https://blog.csdn.net/weixin_43002433/article/details/108888927)。

```
sudo vim  /etc/hosts
nvidia.github.io
185.199.108.153 nvidia.github.io
185.199.109.153 nvidia.github.io
185.199.110.153 nvidia.github.io
185.199.111.153 nvidia.github.io

```

2. Install the nvidia-docker2 package (and dependencies) after updating the package listing:

   ```shell
   sudo apt-get update
   
   sudo apt-get install -y nvidia-docker2
   ```

4. 3. Restart the Docker daemon to complete the installation after setting the default runtime:

   ```shell
   sudo systemctl restart docker
   ```

4. At this point, a working setup can be tested by running a base CUDA container:（可不执行，这一步其实就是安装了特定版本的cuda，工作站没必要）

   ```shell
   sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
   ```

5. 安装包含jupyter以及所有主流框架的镜像

   ```shell
   sudo docker pull ufoym/deepo:all-jupyter
   ```




# 创建容器

## 创建可调用GPU的容器

### 1. 使用nvidia-docker创建
```
nvidia-docker run -it -p [local port]:[docker port] --ipc=host -v [dokcer save dir]:/[share floder name] --name [docker name] [docker images id]
```

```
deepo xrdp 3389

nvidia-docker run -it -p 端口:22 -p 端口:3389  --ipc=host -v /home/wsx/:/wsx --name 名字 cf60a305ba7b
```

### 2. 使用docker加参数创建
直接使用docker命令，而非nvidia-docker可以在docker中调用GPU资源(参考https://www.cnblogs.com/chester-cs/p/14444247.html)

```
sudo docker run -it --gpus all  -p 1122:22 -p 1189:3389  --ipc=host -v /home/wsx/:/wsx -v /home/repo/:/repo --name wsx_ubuntu_py  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility -e NVIDIA_VISIBLE_DEVICES=all  074447744283  /bin/bash
```

```
sudo docker run -it --gpus all  -p [ssh端口]:22  -p  [xrdp端口]:3389  --ipc=host -v  [host主机用户路径]:[docker路径]  -v [共用host路劲]:[docker 路径]  --name [docker名]  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility -e NVIDIA_VISIBLE_DEVICES=all  [镜像id]  /bin/bash
```


# 容器常用命令
进入容器docker start -i [容器名or ID]
退出并停止容器crtl+a+d
退出不停止容器crtl+q+p
停止容器docker stop [容器名or ID]
删除容器docker rm [容器名or ID]

启动容器并可执行bash命令
```
docker exec -it [docker id] /bin/bash
```

# 镜像操作
docker rmi <image id> delete one image

# 查看容器大小
查看 每个 image、container 详细大小：docker system df -v


# 容器镜像导入导出

参考博客https://www.cnblogs.com/zhuochong/p/10064350.html

将镜像导出
docker save -o deepo.tar cf60a305ba7b
docker save -o [导出镜像命名] [镜像id]

将容器导出：
docker export wsx_rmtdsk -o wsx_rmtdsk.tar
docker export [容器名] -o [压缩包名]

将导出的容器导入为镜像 
docker import wsx_rmtdsk.tar wsxdocker:imp
docker import [容器包名] [镜像名]:[tag]


镜像是容器导入的，在用上面的命令创建容器的时候，会出现如下错误：
```
Error response from daemon: No command specified
```
解决方法：在末尾加上 /bin/bash
```
sudo nvidia-docker run -it -p 1022:22 -p 1089:3389  --ipc=host -v /home/wsx/:/wsx --name wsxdkr 0517cf8bd653 /bin/bash
```
参考：
```
解决办法有两个 1、题主这种就是使用create给镜像加上cmd命令，题主加的是/bin/bash 2、还有一种就是run的时候，在末尾加上cmd命令，如果是/bin/bash，就加上/bin/bash，如果是/usr/sbin/init，就加上/usr/sbin/init，根据不同镜像加合适的命令
```





# 常见错误	
```
if hit like this
System has not been booted with systemd as init system (PID 1). Can't operate.

change commadn "systemctl" to "service"
systemctl start xrdp -> service xrdp start
```



# 修改容器存储位置
## 软连接方法（参考）
```
默认情况下Docker的存放位置为：/var/lib/docker
可以通过下面命令查看具体位置：

sudo docker info | grep "Docker Root Dir"

解决这个问题，最直接的方法当然是挂载分区到这个目录，但是我的数据盘还有其他东西，这肯定不好管理，所以采用修改镜像和容器的存放路径的方式达到目的。

这个方法里将通过软连接来实现。

首先停掉Docker服务：
systemctl restart docker
或者
service docker stop

然后移动整个/var/lib/docker目录到目的路径：

mv /var/lib/docker /root/data/docker
ln -s /root/data/docker /var/lib/docker

这时候启动Docker时发现存储目录依旧是/var/lib/docker，但是实际上是存储在数据盘的，你可以在数据盘上看到容量变化。
```



修改/etc/docker/daemon.json     "data-root"参数

```
{
    "data-root": "/home/bci/docker_space",
    "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"],
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```

Copy the current data directory to the new one
sudo rsync -aP /var/lib/docker/ /path/to/your/docker

$ sudo systemctl daemon-reload
$ sudo systemctl restart docker






```
docker run -it --gpus all  -p 2022:22 -p 2089:3389  --ipc=host -v /home/bci/usr/wsx/:/wsx --name wsx_dk_py  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility -e NVIDIA_VISIBLE_DEVICES=all  22c95c4181fe /bin/bash
```



docker run -it --gpus all  -p 2022:22 -p 2089:3389  --ipc=host -v /home/lili:/lili -v /home/repo:/repo --name lili  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility -e NVIDIA_VISIBLE_DEVICES=all  78a66e667d90 /bin/bash