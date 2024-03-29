
## dataset
```
data
|-- NTU-RGB+D
|   `-- samples_with_missing_skeletons.txt
`-- nturgb_d
    |-- xsub
    |   |-- train_data_joint_pad.npy #(40091,3,300,25,2)
    |   |-- train_label.pkl
    |   |-- val_data_joint_pad.npy
    |   `-- val_label.pkl
    `-- xview
        |-- train_data_joint_pad.npy
        |-- train_label.pkl
        |-- val_data_joint_pad.npy
        `-- val_label.pkl
```

```
for data, data_downsample, target_data, data_last, label in loader:

data: (32,3,290,25,2) 
data_downsample:(32,3,50,25,2) 
target_data:(32,3,10,25,2) 
data_last:(32,3,1,25,2) 
label:(32)

32 batch_size
3 x,y,z cordinate
290 frame
50 #downsample the videos to obtain 50 frames from the valid frames at regular intervals
25 joints
2 For the multi-person cases, we select 2 people with the highest average joint confidence in each clip
```

```
data = {Tensor: (32, 3, 290, 25, 2)} tensor([[[[[-1.6099e-01, -2.0000e-01],\n           [-2.0000e-01, -2.0000e-01],\n           [-2.4691e-01, -2.0000e-01],\n           ...,\n           [-2.8890e-01, -2.0000e-01],\n           [ 9.6081e-02, -2.0000e-01],\n           [ 4.6539e-02, -2.0000e-01]],\n\n          [[-1.6398e-01, -1.9900e-01],\n           [-1.9900e-01, -1.9900e-01],\n           [-2.3470e-01, -1.9900e-01],\n           ...,\n           [-2.9801e-01, -1.9900e-01],\n           [ 8.2085e-02, -1.9900e-01],\n           [ 6.7159e-02, -1.9900e-01]],\n\n          [[-1.6591e-01, -1.9799e-01],\n           [-1.9799e-01, -1.9799e-01],\n           [-2.3446e-01, -1.9799e-01],\n           ...,\n           [-2.9946e-01, -1.9799e-01],\n           [ 1.3246e-01, -1.9799e-01],\n           [ 1.1738e-01, -1.9799e-01]],\n\n          ...,\n\n          [[ 8.6192e-02,  8.7960e-02],\n           [ 8.7960e-02,  8.7960e-02],\n           [ 7.1746e-02,  8.7960e-02],\n           ...,\n           [-1.0777e-01,  8.7960e-02],\n           [ 4.3478e-01,  8.7960e-02],\n           [ 4.28...

data_downsample = {Tensor: (32, 3, 50, 25, 2)} tensor([[[[[-1.6398e-01, -1.9900e-01],\n           [-1.9900e-01, -1.9900e-01],\n           [-2.3470e-01, -1.9900e-01],\n           ...,\n           [-2.9801e-01, -1.9900e-01],\n           [ 8.2085e-02, -1.9900e-01],\n           [ 6.7159e-02, -1.9900e-01]],\n\n          [[-1.6591e-01, -1.9799e-01],\n           [-1.9799e-01, -1.9799e-01],\n           [-2.3446e-01, -1.9799e-01],\n           ...,\n           [-2.9946e-01, -1.9799e-01],\n           [ 1.3246e-01, -1.9799e-01],\n           [ 1.1738e-01, -1.9799e-01]],\n\n          [[-1.6725e-01, -1.9699e-01],\n           [-1.9699e-01, -1.9699e-01],\n           [-2.3333e-01, -1.9699e-01],\n           ...,\n           [-3.0102e-01, -1.9699e-01],\n           [ 1.0391e-01, -1.9699e-01],\n           [ 9.9645e-02, -1.9699e-01]],\n\n          ...,\n\n          [[-1.4140e-01, -1.3880e-01],\n           [-1.3880e-01, -1.3880e-01],\n           [-1.4650e-01, -1.3880e-01],\n           ...,\n           [-3.5354e-01, -1.3880e-01],\n           [ 2.1654e-01, -1.3880e-01],\n           [ 2.10...

data_last = {Tensor: (32, 3, 1, 25, 2)} tensor([[[[[ 0.0773,  0.0900],\n           [ 0.0900,  0.0900],\n           [ 0.1030,  0.0900],\n           ...,\n           [-0.1194,  0.0900],\n           [ 0.4658,  0.0900],\n           [ 0.4588,  0.0900]]],\n\n\n         [[[ 0.0949,  0.0967],\n           [ 0.0967,  0.0967],\n           [ 0.1110,  0.0967],\n           ...,\n           [-0.0271,  0.0967],\n           [ 0.1569,  0.0967],\n           [ 0.1618,  0.0967]]],\n\n\n         [[[-0.2549,  0.0000],\n           [ 0.0000,  0.0000],\n           [ 0.2551,  0.0000],\n           ...,\n           [-0.3625,  0.0000],\n           [-0.2681,  0.0000],\n           [-0.2399,  0.0000]]]],\n\n\n\n        [[[[-0.0998, -0.0967],\n           [-0.0967, -0.0967],\n           [-0.1079, -0.0967],\n           ...,\n           [-0.1097, -0.0967],\n           [ 0.2325, -0.0967],\n           [ 0.2264, -0.0967]]],\n\n\n         [[[-0.1403, -0.0933],\n           [-0.0933, -0.0933],\n           [-0.0369, -0.0933],\n           ...,\n           [ 0.1979, -0.0933],\n           [-0.0280, -0.0933],\n   ...


label = {Tensor: (32,)} tensor([25, 43, 45, 21, 18, 11, 55, 21, 20, 14, 27, 39,  3, 33, 57, 20,  7, 41,\n        30, 59, 30, 51, 51, 13, 44, 36, 44, 37, 43,  4, 29,  9],\n       device='cuda:0')

target_data = {Tensor: (32, 3, 10, 25, 2)} tensor([[[[[ 7.6411e-02,  9.0970e-02],\n           [ 9.0970e-02,  9.0970e-02],\n           [ 1.0361e-01,  9.0970e-02],\n           ...,\n           [-1.2520e-01,  9.0970e-02],\n           [ 4.6641e-01,  9.0970e-02],\n           [ 4.5930e-01,  9.0970e-02]],\n\n          [[ 8.3167e-02,  9.1973e-02],\n           [ 9.1973e-02,  9.1973e-02],\n           [ 8.4413e-02,  9.1973e-02],\n           ...,\n           [-1.0910e-01,  9.1973e-02],\n           [ 4.4733e-01,  9.1973e-02],\n           [ 4.4146e-01,  9.1973e-02]],\n\n          [[ 9.2062e-02,  9.2977e-02],\n           [ 9.2977e-02,  9.2977e-02],\n           [ 8.3123e-02,  9.2977e-02],\n           ...,\n           [-1.1745e-01,  9.2977e-02],\n           [ 4.4610e-01,  9.2977e-02],\n           [ 4.4027e-01,  9.2977e-02]],\n\n          ...,\n\n          [[ 1.3301e-01,  9.7993e-02],\n           [ 9.7993e-02,  9.7993e-02],\n           [ 6.2288e-02,  9.7993e-02],\n           ...,\n           [-1.0177e-03,  9.7993e-02],\n           [ 3.7908e-01,  9.7993e-02],\n           [ 3.64...

```

```
{'work_dir': './work_dir/recognition/ntu-xsub/AS_GCN', 'config': 'config/as_gcn/ntu-xsub/train_aim.yaml', 'phase': 'train', 'save_result': False, 'start_epoch': 0, 'num_epoch': 10, 'use_gpu': True, 'device': [0, 1, 2], 'log_interval': 100, 'save_interval': 1, 'eval_interval': 5, 'save_log': True, 'print_log': True, 'pavi_log': False, 'feeder': 'feeder.feeder.Feeder', 'num_worker': 4, 'train_feeder_args': {'data_path': './data/nturgb_d/xsub/train_data_joint_pad.npy', 'label_path': './data/nturgb_d/xsub/train_label.pkl', 'random_move': True, 'repeat_pad': True, 'down_sample': True, 'debug': False}, 'test_feeder_args': {'data_path': './data/nturgb_d/xsub/val_data_joint_pad.npy', 'label_path': './data/nturgb_d/xsub/val_label.pkl', 'random_move': False, 'repeat_pad': True, 'down_sample': True}, 'batch_size': 1, 'test_batch_size': 32, 'debug': False, 'model1': 'net.as_gcn.Model', 'model2': 'net.utils.adj_learn.AdjacencyLearn', 'model1_args': {'in_channels': 3, 'num_class': 60, 'dropout': 0.5, 'edge_importance_weighting': True, 'graph_args': {'layout': 'ntu-rgb+d', 'strategy': 'spatial', 'max_hop': 4}}, 'model2_args': {'n_in_enc': 150, 'n_hid_enc': 128, 'edge_types': 3, 'n_in_dec': 3, 'n_hid_dec': 128, 'node_num': 25}, 'weights1': None, 'weights2': None, 'ignore_weights': [], 'show_topk': [1, 5], 'base_lr1': 0.1, 'base_lr2': 0.0005, 'step': [50, 70, 90], 'optimizer': 'SGD', 'nesterov': True, 'weight_decay': 0.0001, 'max_hop_dir': 'max_hop_4', 'lamda_act': 0.5, 'lamda_act_dir': 'lamda_05'}
```



## Errors
### GPU error
```
python main.py recognition -c config/as_gcn/ntu-xsub/train.yaml --device 0 1 2

pytorch多个显卡并行训练 RuntimeError: Caught RuntimeError in replica 0 on device 0.

就是 网络模型的某个参数复制分配到 不同的GPU的时候，部分参数始终在GPU_0上
https://blog.csdn.net/liu_yuan_kai/article/details/109290375
```


```
(stgcn) root@bd3db6c890cb:~/AS-GCN/data/nturgb_d/xsub# ls
train_data_joint_pad.npy  train_label.pkl  val_data_joint_pad.npy  val_label.pkl
(stgcn) root@bd3db6c890cb:~/AS-GCN/data/nturgb_d/xsub# python 
Python 3.6.13 |Anaconda, Inc.| (default, Feb 23 2021, 21:15:04) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> data = numpy.load("train_data_joint_pad.npy")
>>> data.shape
(40091, 3, 300, 25, 2)
>>> data = numpy.load("val_data_joint_pad.npy")
>>> data.shape
(16487, 3, 300, 25, 2)
>>> 
```

```
>>> import torch.nn as nn
>>> loss = nn.CrossEntropyLoss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> import torch
>>> input = torch.randn(3, 5, requires_grad=True)
>>> input
tensor([[-0.0728,  0.4230,  1.5608, -0.2655, -1.5106],
        [ 0.4999, -1.3030,  0.4470, -0.9654,  1.2195],
        [ 0.1500,  0.5560, -0.3185,  0.8140, -0.6456]], requires_grad=True)
>>> target = torch.empty(3, dtype=torch.long).random_(5)
>>> target
tensor([0, 1, 2])
>>> output = loss(input, target)
>>> output
tensor(2.5462, grad_fn=<NllLossBackward>)

```

### RuntimeError
```
RuntimeError: Tensor for argument #2 ‘weight’ is on CPU, but expected it to be on GPU (while checking arguments for cudnn_batch_norm)


make the net to the cuda()
self.model3.cuda()
```



### 3090 cuda version error
GeForce RTX 3090 with CUDA capability sm_86 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_61 sm_70 sm_75 compute_37.

cuda 版本和pytorch版本不匹配

solution
https://pytorch.org/get-started/locally/

```
cuda 11.1

pip3 install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```



## model analysis


### data loader
for data, data_downsample, target_data, data_last, label in loader:
```
data: (32,3,290,25,2) 
data_downsample:(32,3,50,25,2) 
target_data:(32,3,10,25,2) 
data_last:(32,3,1,25,2) 
label:(32)
```

### model

#### model2	
**net.utils.adj_learn.AdjacencyLearn**

A_batch, prob, outputs, data_target = self.model2(data_downsample)

it will train at first 10 epoches

![clipboard](img/as_gcn/clipboard-1624623582810.png)

<img src="img/as_gcn/clipboard-1622648514733.png" alt="img" style="zoom:60%;" />

<img src="img/as_gcn/clipboard-1622648580804.png" alt="img" style="zoom:67%;" />











#### model1 

**net.as_gcn.Model**

x_class, pred, target = self.model1(data, target_data, data_last, A_batch, self.arg.lamda_act)



#### pipeline
PretrainAIM
the first 10 epoches
```train() if training_A```

TrainMainPipeline
after the first 10 epoches
```train() else```



```
input:
data: (4,3,290,25,2)
target_data: (4,3,10,25,2)
data_last: (4,3,1,25,2)
A_batch: (8,2,25,25)
self.arg.lamda_act 0.5

output:
x_class (4,60)
pred (4,3,10,25)
target (4,3,10,25)
```

def   forward(self, x, x_target, x_last, A_act, lamda_act):
```
x			data: 			(4,3,290,25,2) 
x_target	target_data: 	(4,3,10,25,2)
x_last		data_last: 		(4,3,1,25,2)
A_act		A_batch: 		(8,2,25,25)
lamda_act	self.arg.lamda_act 0.5
```



## args

```
train:
recognition -c config/as_gcn/ntu-xsub/train.yaml --device 1 --batch_size 4

python main.py recognition -c config/as_gcn/ntu-xsub/train.yaml --device 0 --batch_size 32

test:
python main.py recognition -c config/as_gcn/ntu-xsub/test.yaml --device 0

```






## log

train as the asgcn origin hyper parameter list
train loss
<img src="img/as_gcn/clipboard-1624625427825.png" alt="img" style="zoom:50%;" />
train
>3.8870446980296913
>3.808238947053699
>3.9460883728403027
>3.9241404717755017
>4.117355283280614
>nan
>nan
>eval
>4.041288025619448
>\###############################################
>[06.20.21|15:19:08] 	Top1: 54.67%
>[06.20.21|15:19:08] 
>[06.20.21|15:19:08] 	Top5: 86.08%





**change the learn rate to 0.0075**
tranining curve

<img src="img/as_gcn/clipboard-1624625843115.png" alt="img" style="zoom:50%;" />

vlidation curve

<img src="img/as_gcn/clipboard-1624625860789.png" alt="img" style="zoom:50%;" />



best epoch

>[06.21.21|00:02:58] Eval epoch: 54
>
>[06.21.21|00:04:43] 	mean_loss_class: 1.0486512068052625
>
>[06.21.21|00:04:43] 
>
>[06.21.21|00:04:43] 	Top1: 73.49%
>
>[06.21.21|00:04:43] 
>
>[06.21.21|00:04:43] 	Top5: 92.97%
>
>test this model on test set
>
>top1  73%



test this model on test set
top1  73%
![img](img/as_gcn/d7ea5fed5c1c048075bdb2e6d4e9608.png)



paper result

![img](img/as_gcn/clipboard-1624625982239.png)




## notes
**classification details**

![img](img/as_gcn/clipboard-1624626035169.png)

![img](img/as_gcn/clipboard-1624625427826.png)





## tuning


### bigger batch_size

python main.py recognition -c config/as_gcn/ntu-xsub/train.yaml --device 0 --batch_size 32



![image-20210629182226540](img/as_gcn/image-20210629182226540.png)

![image-20210629182200805](img/as_gcn/image-20210629182200805.png)

```
[06.29.21|15:05:52] Eval epoch: 99
[06.29.21|15:07:11]     mean_loss_class: 1.326048486136882
[06.29.21|15:07:11]
[06.29.21|15:07:11]     Top1: 72.27%
[06.29.21|15:07:12]
[06.29.21|15:07:12]     Top5: 91.36%
```



weight_decay: 0.0001
base_lr1: 0.076
Top1: 72.27%

weight_decay: 0.0001
base_lr1: 0.008
Top1: 73.59%



weight_decay: 0.0001
base_lr1: 0.01
Top1  73.27%




## SpatialGcn
```
class SpatialGcn(nn.Module):

    def __init__(self,
                 in_channels,
                 out_channels,
                 k_num,
                 edge_type=2,
                 t_kernel_size=1,
                 t_stride=1,
                 t_padding=0,
                 t_dilation=1,
                 bias=True):
        super().__init__()

        self.k_num = k_num
        self.edge_type = edge_type
        self.conv = nn.Conv2d(in_channels=in_channels,
                              out_channels=out_channels*k_num,
                              kernel_size=(t_kernel_size, 1),
                              padding=(t_padding, 0),
                              stride=(t_stride, 1),
                              dilation=(t_dilation, 1),
                              bias=bias)

    def forward(self, x, A, B, lamda_act):

        x = self.conv(x)
        n, kc, t, v = x.size()
        x = x.view(n, self.k_num,  kc//self.k_num, t, v)
        x1 = x[:,:self.k_num-self.edge_type,:,:,:]
        x2 = x[:,-self.edge_type:,:,:,:]
        x1 = torch.einsum('nkctv,kvw->nctw', (x1, A))
        x2 = torch.einsum('nkctv,nkvw->nctw', (x2, B))
        x_sum = x1+x2*lamda_act

        return x_sum.contiguous(), A
```