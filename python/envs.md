


# envs check
```
import torch
print(torch.__version__)
print(torch.version.cuda) 
```

# pytorch



# cuda

nvidia account
wangshuxim@gmail.com
wo@chijuzi8

check cuda version
```
nvcc --version
```
## install
offical docs
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal

my machine
Linux nvidiat4-vm 5.4.0-1038-gcp #41~18.04.1-Ubuntu SMP Fri Feb 26 22:23:13 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.2.2/local_installers/cuda-repo-ubuntu1804-11-2-local_11.2.2-460.32.03-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-11-2-local_11.2.2-460.32.03-1_amd64.deb
sudo apt-key add /var/cuda-repo-ubuntu1804-11-2-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

then:
nvidia-smi worked

## change version


