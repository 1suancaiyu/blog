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

7. 看到以下结果，即证明已经Docker已经安装成功

<img src="01.png" style="zoom:80%;" />

```

```



# 安装nvidia-docker2

此处安装还参考了：[官网指引](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker)

1. Setup the stable repository and the GPG key:

   ```shell
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
      && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   ```

   在执行这一步以及后面的操作时遇到问题：“gpg: 找不到有效的 OpenPGP”、“E: 无法定位软件包 nvidia-docker2”。[解决方案](https://blog.csdn.net/weixin_43002433/article/details/108888927)。

2. Install the nvidia-docker2 package (and dependencies) after updating the package listing:

   ```shell
   sudo apt-get update
   
   sudo apt-get install -y nvidia-docker2
   ```

3. Restart the Docker daemon to complete the installation after setting the default runtime:

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




# build docker
```
nvidia-docker run -it -p [local port]:[docker port] --ipc=host -v [dokcer save dir]:/[share floder name] --name [docker name] [docker images id]
```

```
deepo xrdp 3389

nvidia-docker run -it -p 端口:22 -p 端口:3389  --ipc=host -v /home/sci/private/liu_ping_zhi:/lpz --name 名字 cf60a305ba7b
```



在容器中执行bash命令

```
docker exec -it [docker id] /bin/bash
```




# errors	
```
if hit like this
System has not been booted with systemd as init system (PID 1). Can't operate.

change commadn "systemctl" to "service"
systemctl start xrdp -> service xrdp start
```


## export image
```
docker export name/id > xxx.tar
docker import xxx.tar [new_docker_name]
docker run -it 新容器:v1
```



## 软链接修改Docker本地镜像与容器的存储位置
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