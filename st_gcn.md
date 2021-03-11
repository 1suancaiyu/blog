# st-gcn study note
main contribution
1. open_pose prrporcess
2. gcn
3. tcn

simple attentino block


## dataset
### 1. Kinetics
300,000 video clips
400 human
Each clip in Kinetics lasts around 10 seconds.

RGB to 18 joints (x,y,c) by OpenPose
2D coordinates (x,y) and c: confidence scores

# ?
For the multi-person
cases, we select 2 people with the highest average joint confidence in each clip
```
train_data.npy
shape (240436, 3, 300, 18, 2)

td[1,1,1]
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

td[0,0,0] 
[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]

```




# focus point when reading code
1. dataset format
2. training flow

大家大家监督
