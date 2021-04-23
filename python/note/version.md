check cuda version
```
apt install nvidia-cuda-toolkit
nvcc --version
```
check torch
```
import torch
import torchvision
print("torch.__version__: ", torch.__version__)
print("torchvision.__version__: ", torchvision.__version__)
```
