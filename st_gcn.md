# st-gcn study note
main contribution
1. open_pose preporcess
2. gcn
3. tcn

simple attention block


## dataset
```
st-gcn-processed-data
├── Kinetics
│   └── kinetics-skeleton
│       ├── train_data.npy
│       ├── train_label.pkl
│       ├── val_data.npy
│       └── val_label.pkl
└── NTU-RGB-D
    ├── xsub
    │   ├── train_data.npy
    │   ├── train_label.pkl
    │   ├── val_data.npy
    │   └── val_label.pkl
    └── xview
        ├── train_data.npy
        ├── train_label.pkl
        ├── val_data.npy
        └── val_label.pkl

```
### 1. Kinetics
#### info
300,000 video clips
400 human
Each clip in Kinetics lasts around 10 seconds.

RGB to 18 joints (x,y,c) by OpenPose
2D coordinates (x,y) and c: confidence scores

## ?
For the multi-person
cases, we select 2 people with the highest average joint confidence in each clip. So if there is only one person in the frame, the another pad 0 ?
#### shape
```
train_data.npy
(240436, 3, 300, 18, 2)

val_data.npy
(19796, 3, 300, 18, 2)

train_label.pkl
([...],   # _.json * 240436]
 [...])   # number * 240436]

val:train  8:100
```


#### analyize
```
train_data.npy
shape (240436, 3, 300, 18, 2)

240436 
clips

3 
(X,Y,C)

300 
frames

18 
joints

2 
For the multi-person cases, we select 2 people with the highest average joint confidence in each clip
```


#### Sample 
```
>>> print(td[1,0,1]) 
[[ 0.061  0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [-0.013  0.   ]
 [ 0.208  0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]]

# y 
>>> print(td[1,1,1])
[[ 0.122  0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]
 [-0.033  0.   ]
 [-0.011  0.   ]
 [ 0.     0.   ]
 [ 0.     0.   ]]

 # c
>>> print(td[1,2,1])
[[0.301 0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.    0.   ]
 [0.397 0.   ]
 [0.44  0.   ]
 [0.    0.   ]
 [0.    0.   ]]
>>>

train_label_pkl[0][:10]:
 ['xl6vmD0XBS0.json', 'OkLnSMGCWSw.json', 'IBopZFDKfYk.json', 'HpoFylcrYT4.json', 'mlAtn_zi0bY.json', 'P924_DoqgaA.json', 'Qvqr7tHPSBY.json', 'wj6VN9D0B1Q.json', '8F4rDSxTJlQ.json', 'k2pUg1s6yvk.json']

train_label_pkl[1][:10]:
 [235, 388, 326, 306, 105, 369, 72, 306, 229, 44]


val_label[0][:10]:
 ['_3qg-oAr7b0.json', 'HxGk6WDkOzk.json', 'fa1WrHOTjxY.json', 'pF6EjkDzs5o.json', 'syJ-6ygTmVM.json', 'Hu4OX-8jzoc.json', 'EUIGpdmtzuA.json', 'HXhYD9z_DlE.json', 'PcaO-L9HPrU.json', 'yGkAoxnV-Fw.json']

val_label[1][:10]:
 [66, 6, 187, 323, 278, 183, 213, 92, 290, 377]

```

### 2. NTU-RGB-D
#### info
56,000 action clips
60 action classes
40 volunteers
3D joint locations (X; Y; Z) 
25 joints
each clip most 2 subject

detected by the Kinect depth sensors
three camera views recorded simultaneously

**x-sub**
40320 train actors subset1
16560 evaluate actors subset2

**x-view**
37920 train camera view 2&3
18960 evaluate camera view 1

#### shape
```
#x-sub
train_data.npy
(40091, 3, 300, 25, 2)

"val_data.npy"
(16487, 3, 300, 25, 2)

train_label.pkl
data[0][:10]:
 ['S011C001P019R001A005.skeleton', 'S010C001P019R002A027.skeleton', 'S011C002P001R001A023.skeleton', 'S013C001P019R002A024.skeleton', 'S001C003P005R002A060.skeleton', 'S011C003P027R002A053.skeleton', 'S003C001P019R002A043.skeleton', 'S011C001P002R002A050.skeleton', 'S014C003P017R001A014.skeleton', 'S013C003P015R001A055.skeleton']
data[1][]:
 [4, 26, 22, 23, 59, 52, 42, 49, 13, 54]
tuple1:  40091
tuple2:  40091

val_label.pkl
data[0][:10]:
 ['S003C002P007R001A026.skeleton', 'S005C001P010R001A059.skeleton', 'S009C003P007R001A020.skeleton', 'S002C003P007R001A020.skeleton', 'S016C001P021R001A053.skeleton', 'S008C003P032R002A036.skeleton', 'S016C003P040R002A025.skeleton', 'S008C002P036R001A040.skeleton', 'S014C001P039R001A022.skeleton', 'S008C001P030R001A029.skeleton']
data[1][:10]:
 [25, 58, 19, 19, 52, 35, 24, 39, 21, 28]
tuple1:  16487
tuple2:  16487


#x-veiw
train_data.npy
(37646, 3, 300, 25, 2)

val_data.npy
(18932, 3, 300, 25, 2)

```





## training process

# focus point when reading code
1. dataset format
2. training process

