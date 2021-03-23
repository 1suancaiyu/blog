paper
```
Rao, H., Wang, S., Hu, X., Tan, M., Guo, Y., Cheng, J., ... & Liu, X. (2020). A Self-Supervised Gait Encoding Approach with Locality-Awareness for 3D Skeleton Based Person Re-Identification. arXiv preprint arXiv:2009.03671.
```

github
```
https://github.com/1suancaiyu/Locality-Awareness-SGE
```
![img/frame_predit.png]

where is code
```
train.py

def endoer_classify()

1026     elif Model == 'prediction':
1027         _targets = np.concatenate((_input_data[1:, :, :], _input_data[-1, :, :].reshape([1, time_steps, series_length])),
1028                                  axis=0)
1029         # _input_data = _input_data[:-1]
1030     # permutation

```
