## paper
```
Rao, H., Wang, S., Hu, X., Tan, M., Guo, Y., Cheng, J., ... & Liu, X. (2020). A Self-Supervised Gait Encoding Approach with Locality-Awareness for 3D Skeleton Based Person Re-Identification. arXiv preprint arXiv:2009.03671.
```

## github
```
https://github.com/1suancaiyu/Locality-Awareness-SGE
```
![frame_predit](img\frame_predit.png)


## code

### train.py

#### model
```
four choices
1. prediction 
2. sorting 
3. rev_rec 
4. rev_rec_plus: rev_rec_plus" will train three types of models sequentially.
```

main()
```
Model == 'rev_rec_plus'
pre_task = 'prediction'
```

```
 171         # wsx
 172         # Prediction
 173         attention = 'BA'
 174         folder_name = dataset + '_' + attention
 175         folder_name = './Models/Gait_Encoding_models/' + folder_name
 176         pre_task = 'prediction'
 177         for i in ['x', 'y', 'z']:
 178             try:
 179                 os.mkdir(folder_name + '_' + i + '_' + str(time_steps) + '_' + str(temperature) + '_' + Frozen + view + 'pre_' + pre_task)
 180             except:
 181                 pass
 182             # suancaiyu
 183             train(folder_name + '_' + i + '_' + str(time_steps) + '_' + str(temperature)+ '_' + Frozen + view + 'pre_' + pre_task, i, train_dataset=dataset)

```

train()
```
 665             # suancaiyu encoder_decoder()
 666             training_decoder_output, predicting_decoder_output, lstm_weights_1, lstm_weights_2 = encoder_decoder(input_data,
 667                                                                                targets,
 668                                                                                lr,
 669                                                                                target_sequence_length,
 670                                                                                max_target_sequence_length,
 671                                                                                source_sequence_length,
 672                                                                                encoding_embedding_size,
 673                                                                                decoding_embedding_size,
 674                                                                                rnn_size,
 675                                                                                num_layers)

```

encoder_decoder()

```
decoder_input = process_decoder_input(targets, batch_size)
```

process_decoder_input()
```
 590 #suancaiyu
 591 def process_decoder_input(data, batch_size):
 592     '''
 593     transform the target sequence (1,2,3,...,f) to (Z,1,2,3,...,f-1) as input to decoder in training
 594     '''
 595
 596     print("wsx log process_decoder_inut() enter")
 597     print("wsx log data shape",data.shape)
 598     ending = tf.strided_slice(data, [0, 0, 0], [batch_size, -1, series_length], [1, 1, 1])
 599     print("wsx log ending shape",ending.shape)
 600     decoder_input = tf.concat([tf.fill([batch_size, time_steps, series_length], 0.), ending], 1)
 601     print("wsx log decoder_input shape",decoder_input.shape)
 602     return decoder_input
```



```
def GE()
Gait Encoder()

def GD()
Gait Decoder()
```

GD()

```
 582         predicting_decoder_output, predicting_decoder_state, _ = tf.contrib.seq2seq.dynamic_decode(predicting_decoder,
 583                                                                          impute_finished=True,
 584                                                                          maximum_iterations=max_target_sequence_length)
```

**predicting_decoder_output**

if the  pre_task = 'prediction'  and this output will be the next frame

by  **tf.contrib.seq2seq.dynamic_decode**

and the process of decoder is no difference for the three  pre_task 


#### check the loss function

get_data_BIWI()
```
359         # prediction
 360         elif Model == 'prediction':
 361                 targets = np.concatenate((input_data[1:, :, :], input_data[-1, :, :].reshape([1, time_steps, series_length])),
 362                                          axis=0)
 363                 print("wsx log targets shape: ",targets.shape)
 364                 # input_data = input_data[:-1]
 365                 input_data = input_data.tolist()
 366                 print("wsx log input_data.tolist() len(input_data): ",len(input_data))
 367                 targets = targets.tolist()
 368                 print("wsx log targets tolist() len(targets): ",len(targets))
```

loss
```
 683         # suancaiyu
 684         predicting_output = tf.identity(predicting_decoder_output.rnn_output, name='predictions')
 685         training_output = tf.identity(predicting_decoder_output.rnn_output, name='train_output')
 686
 687         # wsx loss
 688         train_loss = tf.reduce_mean(tf.nn.l2_loss(training_decoder_output - targets))
 689         real_loss = tf.identity(train_loss, name='real_loss')
```

targets
```
276     elif Model == 'prediction':
 277         # suancaiyu targets
 278         targets = np.concatenate((input_data[1:,:,:], input_data[-1,:, :].reshape([1, time_steps, series_length])), axis=0)
 279         # input_data = input_data[:-1]
 280         input_data = input_data.tolist()
 281         targets = targets.tolist()
```



decoder input

```
decoder_input = process_decoder_input(targets, batch_size)
```

```
 def get_data_KGBD(
 276     elif Model == 'prediction':
 277         # suancaiyu targets
 278         targets = np.concatenate((input_data[1:,:,:], input_data[-1,:, :].reshape([1, time_steps, series_length])), axis=0)
 279         # input_data = input_data[:-1]
 280         input_data = input_data.tolist()
 281         targets = targets.tolist()

```

```
 593 # suancaiyu
 594 # so for all the three pre_task the input data is 1,,f-1?
 595 def process_decoder_input(data, batch_size):
 596     '''
 597     transform the target sequence (1,2,3,...,f) to (Z,1,2,3,...,f-1) as input to decoder in training
 598     '''
 599     ending = tf.strided_slice(data, [0, 0, 0], [batch_size, -1, series_length], [1, 1, 1])
 600     decoder_input = tf.concat([tf.fill([batch_size, time_steps, series_length], 0.), ending], 1)
 601     return decoder_input
```


## run the project

### datasets

#### BIWI RGBD-ID Dataset

50 training and 56 testing sequences of 50 different people

In the training videos, people performs a certain routine of motions in front of a Kinect, such as a rotation around the vertical axis, several head movements and two walks towards the camera.

The number of body joints J is set to the maximum number on
all datasets: J = 20 for BIWI, IAS-Lab, KGBD datasets and
J = 25 for KS20 dataset  

The sequence length f is empirically
set to 6, since in general this frequently-used value can already
produce satisfactory performance on different datasets
f denotes the sequence length   4 6 8 9 10



http://robotics.dei.unipd.it/reid/index.php/8-dataset/2-overview-biwi

![BIWI](img\BIWI.jpg)

```
BIWI_IAS_KGBD
├── BIWI
│   ├── 10
│   │   ├── BIWI_test_npy_data
│   │   │   ├── frame_id_BIWI_10.npy
│   │   │   ├── ids_BIWI_10.npy
│   │   │   ├── t_source_x_BIWI_10.npy
│   │   │   ├── t_source_y_BIWI_10.npy
│   │   │   ├── t_source_z_BIWI_10.npy
│   │   │   ├── t_target_x_BIWI_10.npy
│   │   │   ├── t_target_y_BIWI_10.npy
│   │   │   └── t_target_z_BIWI_10.npy
│   │   └── BIWI_train_npy_data
│   │       ├── frame_id_BIWI_10.npy
│   │       ├── ids_BIWI_10.npy
│   │       ├── source_x_BIWI_10.npy
│   │       ├── source_y_BIWI_10.npy
│   │       ├── source_z_BIWI_10.npy
│   │       ├── target_x_BIWI_10.npy
│   │       ├── target_y_BIWI_10.npy
│   │       └── target_z_BIWI_10.npy
│   ├── 4
│   │   ├── BIWI_test_npy_data
│   │   │   ├── frame_id_BIWI_4.npy
│   │   │   ├── ids_BIWI_4.npy
│   │   │   ├── t_source_x_BIWI_4.npy
│   │   │   ├── t_source_y_BIWI_4.npy
│   │   │   ├── t_source_z_BIWI_4.npy
│   │   │   ├── t_target_x_BIWI_4.npy
│   │   │   ├── t_target_y_BIWI_4.npy
│   │   │   └── t_target_z_BIWI_4.npy
│   │   └── BIWI_train_npy_data
│   │       ├── frame_id_BIWI_4.npy
│   │       ├── ids_BIWI_4.npy
│   │       ├── source_x_BIWI_4.npy
│   │       ├── source_y_BIWI_4.npy
│   │       ├── source_z_BIWI_4.npy
│   │       ├── target_x_BIWI_4.npy
│   │       ├── target_y_BIWI_4.npy
│   │       └── target_z_BIWI_4.npy
│   ├── 6
│   │   ├── BIWI_test_npy_data
│   │   │   ├── frame_id_BIWI_6.npy
│   │   │   ├── ids_BIWI_6.npy
│   │   │   ├── t_source_x_BIWI_6.npy
│   │   │   ├── t_source_y_BIWI_6.npy
│   │   │   ├── t_source_z_BIWI_6.npy
│   │   │   ├── t_target_x_BIWI_6.npy
│   │   │   ├── t_target_y_BIWI_6.npy
│   │   │   └── t_target_z_BIWI_6.npy
│   │   └── BIWI_train_npy_data
│   │       ├── frame_id_BIWI_6.npy
│   │       ├── ids_BIWI_6.npy
│   │       ├── source_x_BIWI_6.npy
│   │       ├── source_y_BIWI_6.npy
│   │       ├── source_z_BIWI_6.npy
│   │       ├── target_x_BIWI_6.npy
│   │       ├── target_y_BIWI_6.npy
│   │       └── target_z_BIWI_6.npy
│   └── 8
│       ├── BIWI_test_npy_data
│       │   ├── frame_id_BIWI_8.npy
│       │   ├── ids_BIWI_8.npy
│       │   ├── t_source_x_BIWI_8.npy
│       │   ├── t_source_y_BIWI_8.npy
│       │   ├── t_source_z_BIWI_8.npy
│       │   ├── t_target_x_BIWI_8.npy
│       │   ├── t_target_y_BIWI_8.npy
│       │   └── t_target_z_BIWI_8.npy
│       └── BIWI_train_npy_data
│           ├── frame_id_BIWI_8.npy
│           ├── ids_BIWI_8.npy
│           ├── source_x_BIWI_8.npy
│           ├── source_y_BIWI_8.npy
│           ├── source_z_BIWI_8.npy
│           ├── target_x_BIWI_8.npy
│           ├── target_y_BIWI_8.npy
│           └── target_z_BIWI_8.npy
├── IAS
│   ├── 10
│   │   ├── IAS_test_npy_data
│   │   │   ├── frame_id_IAS-A_10.npy
│   │   │   ├── frame_id_IAS-B_10.npy
│   │   │   ├── ids_IAS-A_10.npy
│   │   │   ├── ids_IAS-B_10.npy
│   │   │   ├── t_source_x_IAS-A_10.npy
│   │   │   ├── t_source_x_IAS-B_10.npy
│   │   │   ├── t_source_y_IAS-A_10.npy
│   │   │   ├── t_source_y_IAS-B_10.npy
│   │   │   ├── t_source_z_IAS-A_10.npy
│   │   │   ├── t_source_z_IAS-B_10.npy
│   │   │   ├── t_target_x_IAS-A_10.npy
│   │   │   ├── t_target_x_IAS-B_10.npy
│   │   │   ├── t_target_y_IAS-A_10.npy
│   │   │   ├── t_target_y_IAS-B_10.npy
│   │   │   ├── t_target_z_IAS-A_10.npy
│   │   │   └── t_target_z_IAS-B_10.npy
│   │   └── IAS_train_npy_data
│   │       ├── frame_id_IAS_10.npy
│   │       ├── ids_IAS_10.npy
│   │       ├── source_x_IAS_10.npy
│   │       ├── source_y_IAS_10.npy
│   │       ├── source_z_IAS_10.npy
│   │       ├── target_x_IAS_10.npy
│   │       ├── target_y_IAS_10.npy
│   │       └── target_z_IAS_10.npy
│   ├── 4
│   │   ├── IAS_test_npy_data
│   │   │   ├── frame_id_IAS-A_4.npy
│   │   │   ├── frame_id_IAS-B_4.npy
│   │   │   ├── ids_IAS-A_4.npy
│   │   │   ├── ids_IAS-A_8.npy
│   │   │   ├── ids_IAS-B_4.npy
│   │   │   ├── t_source_x_IAS-A_4.npy
│   │   │   ├── t_source_x_IAS-B_4.npy
│   │   │   ├── t_source_y_IAS-A_4.npy
│   │   │   ├── t_source_y_IAS-B_4.npy
│   │   │   ├── t_source_z_IAS-A_4.npy
│   │   │   ├── t_source_z_IAS-B_4.npy
│   │   │   ├── t_target_x_IAS-A_4.npy
│   │   │   ├── t_target_x_IAS-B_4.npy
│   │   │   ├── t_target_y_IAS-A_4.npy
│   │   │   ├── t_target_y_IAS-B_4.npy
│   │   │   ├── t_target_z_IAS-A_4.npy
│   │   │   └── t_target_z_IAS-B_4.npy
│   │   └── IAS_train_npy_data
│   │       ├── frame_id_IAS_4.npy
│   │       ├── ids_IAS_4.npy
│   │       ├── source_x_IAS_4.npy
│   │       ├── source_y_IAS_4.npy
│   │       ├── source_z_IAS_4.npy
│   │       ├── target_x_IAS_4.npy
│   │       ├── target_y_IAS_4.npy
│   │       └── target_z_IAS_4.npy
│   ├── 6
│   │   ├── IAS_test_npy_data
│   │   │   ├── frame_id_IAS-A_6.npy
│   │   │   ├── frame_id_IAS-B_6.npy
│   │   │   ├── ids_IAS-A_6.npy
│   │   │   ├── ids_IAS-B_6.npy
│   │   │   ├── t_source_x_IAS-A_6.npy
│   │   │   ├── t_source_x_IAS-B_6.npy
│   │   │   ├── t_source_y_IAS-A_6.npy
│   │   │   ├── t_source_y_IAS-B_6.npy
│   │   │   ├── t_source_z_IAS-A_6.npy
│   │   │   ├── t_source_z_IAS-B_6.npy
│   │   │   ├── t_target_x_IAS-A_6.npy
│   │   │   ├── t_target_x_IAS-B_6.npy
│   │   │   ├── t_target_y_IAS-A_6.npy
│   │   │   ├── t_target_y_IAS-B_6.npy
│   │   │   ├── t_target_z_IAS-A_6.npy
│   │   │   └── t_target_z_IAS-B_6.npy
│   │   └── IAS_train_npy_data
│   │       ├── frame_id_IAS_6.npy
│   │       ├── ids_IAS_6.npy
│   │       ├── source_x_IAS_6.npy
│   │       ├── source_y_IAS_6.npy
│   │       ├── source_z_IAS_6.npy
│   │       ├── target_x_IAS_6.npy
│   │       ├── target_y_IAS_6.npy
│   │       └── target_z_IAS_6.npy
│   └── 8
│       ├── IAS_test_npy_data
│       │   ├── frame_id_IAS-A_8.npy
│       │   ├── frame_id_IAS-B_8.npy
│       │   ├── ids_IAS-A_8.npy
│       │   ├── ids_IAS-B_8.npy
│       │   ├── t_source_x_IAS-A_8.npy
│       │   ├── t_source_x_IAS-B_8.npy
│       │   ├── t_source_y_IAS-A_8.npy
│       │   ├── t_source_y_IAS-B_8.npy
│       │   ├── t_source_z_IAS-A_8.npy
│       │   ├── t_source_z_IAS-B_8.npy
│       │   ├── t_target_x_IAS-A_8.npy
│       │   ├── t_target_x_IAS-B_8.npy
│       │   ├── t_target_y_IAS-A_8.npy
│       │   ├── t_target_y_IAS-B_8.npy
│       │   ├── t_target_z_IAS-A_8.npy
│       │   └── t_target_z_IAS-B_8.npy
│       └── IAS_train_npy_data
│           ├── frame_id_IAS_8.npy
│           ├── ids_IAS_8.npy
│           ├── source_x_IAS_8.npy
│           ├── source_y_IAS_8.npy
│           ├── source_z_IAS_8.npy
│           ├── target_x_IAS_8.npy
│           ├── target_y_IAS_8.npy
│           └── target_z_IAS_8.npy
└── KGBD
    ├── 10
    │   ├── KGBD_test_npy_data
    │   │   ├── frame_id_KGBD_10.npy
    │   │   ├── ids_KGBD_10.npy
    │   │   ├── t_source_x_KGBD_10.npy
    │   │   ├── t_source_y_KGBD_10.npy
    │   │   ├── t_source_z_KGBD_10.npy
    │   │   ├── t_target_x_KGBD_10.npy
    │   │   ├── t_target_y_KGBD_10.npy
    │   │   └── t_target_z_KGBD_10.npy
    │   └── KGBD_train_npy_data
    │       ├── frame_id_KGBD_10.npy
    │       ├── ids_KGBD_10.npy
    │       ├── source_x_KGBD_10.npy
    │       ├── source_y_KGBD_10.npy
    │       ├── source_z_KGBD_10.npy
    │       ├── target_x_KGBD_10.npy
    │       ├── target_y_KGBD_10.npy
    │       └── target_z_KGBD_10.npy
    ├── 4
    │   ├── KGBD_test_npy_data
    │   │   ├── frame_id_KGBD_4.npy
    │   │   ├── ids_KGBD_4.npy
    │   │   ├── t_source_x_KGBD_4.npy
    │   │   ├── t_source_y_KGBD_4.npy
    │   │   ├── t_source_z_KGBD_4.npy
    │   │   ├── t_target_x_KGBD_4.npy
    │   │   ├── t_target_y_KGBD_4.npy
    │   │   └── t_target_z_KGBD_4.npy
    │   └── KGBD_train_npy_data
    │       ├── frame_id_KGBD_4.npy
    │       ├── ids_KGBD_4.npy
    │       ├── source_x_KGBD_4.npy
    │       ├── source_y_KGBD_4.npy
    │       ├── source_z_KGBD_4.npy
    │       ├── target_x_KGBD_4.npy
    │       ├── target_y_KGBD_4.npy
    │       └── target_z_KGBD_4.npy
    ├── 6
    │   ├── KGBD_test_npy_data
    │   │   ├── frame_id_KGBD_6.npy
    │   │   ├── ids_KGBD_6.npy
    │   │   ├── t_source_x_KGBD_6.npy
    │   │   ├── t_source_y_KGBD_6.npy
    │   │   ├── t_source_z_KGBD_6.npy
    │   │   ├── t_target_x_KGBD_6.npy
    │   │   ├── t_target_y_KGBD_6.npy
    │   │   └── t_target_z_KGBD_6.npy
    │   └── KGBD_train_npy_data
    │       ├── frame_id_KGBD_6.npy
    │       ├── ids_KGBD_6.npy
    │       ├── source_x_KGBD_6.npy
    │       ├── source_y_KGBD_6.npy
    │       ├── source_z_KGBD_6.npy
    │       ├── target_x_KGBD_6.npy
    │       ├── target_y_KGBD_6.npy
    │       └── target_z_KGBD_6.npy
    └── 8
        ├── KGBD_test_npy_data
        │   ├── frame_id_KGBD_8.npy
        │   ├── ids_KGBD_8.npy
        │   ├── t_source_x_KGBD_8.npy
        │   ├── t_source_y_KGBD_8.npy
        │   ├── t_source_z_KGBD_8.npy
        │   ├── t_target_x_KGBD_8.npy
        │   ├── t_target_y_KGBD_8.npy
        │   └── t_target_z_KGBD_8.npy
        └── KGBD_train_npy_data
            ├── frame_id_KGBD_8.npy
            ├── ids_KGBD_8.npy
            ├── source_x_KGBD_8.npy
            ├── source_y_KGBD_8.npy
            ├── source_z_KGBD_8.npy
            ├── target_x_KGBD_8.npy
            ├── target_y_KGBD_8.npy
            ├── target_z_KGBD_8(1).npy
            └── target_z_KGBD_8.npy

```



#### samples

frame_id_BIWI_10.npy

```
npy = numpy.load('frame_id_BIWI_10.npy')
npy.shape
(6840,)
npy[:1500]

# 50 people for training
# the frame sum of those id is not the same

    array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,
            1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,
            2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,
            2,  2,  2,  2,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,
            3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  6,  6,  6,  6,  6,  6,
            6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  8,  8,  8,  8,
            8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,  8,
            8,  8,  8,  8,  8,  8,  8,  8,  8, 10, 10, 10, 10, 10, 10, 10, 10,
           10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
           10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11,
           11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 16, 16,
           16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
           16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
           17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 19, 19, 19, 19,
           19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19,
           19, 19, 19, 19, 19, 19, 19, 19, 19, 21, 21, 21, 21, 21, 21, 21, 21,
           21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21,
           21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22,
           22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22,
           23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23,
           23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24,
           24, 24, 24, 24, 24, 24, 24, 24, 24, 26, 26, 26, 26, 26, 26, 26, 26,
           26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26,
           26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27,
           27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27,
           27, 27, 27, 27, 27, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
           30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31,
           31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32,
           32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
           32, 32, 32, 32, 32, 32, 32, 32, 32, 36, 36, 36, 36, 36, 36, 36, 36,
           36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36,
           36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37,
           37, 37, 37, 37, 37, 37, 37, 37, 39, 39, 39, 39, 39, 39, 39, 39, 39,
           39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40,
           40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40,
           40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44,
           44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 46, 46, 46, 46, 46, 46, 46,
           46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46,
           47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47,
           47, 47, 47, 47, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49,
           49, 49, 49, 49, 49, 49, 49, 49, 49, 49,  0,  0,  0,  0,  0,  0,  0,
            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
           dtype=int64)
```



ids_BIWI_10 # id : [...]

```
array({0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 2109, 2110, 2111, 2112, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 3490, 3491, 3492, 3493, 3494, 3495, 3496, 3497, 3498, 3499, 3500, 3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 3513, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4182, 4183, 4184, 4185, 4186, 4187, 4188, 4189, 4190, 4191, 4192, 4845, 4846, 4847, 4848, 4849, 4850, 4851, 4852, 4853, 4854, 4855, 4856, 4857, 4858, 4859, 4860, 4861, 4862, 4863, 4864, 4865, 4866, 4867, 4868, 5515, 5516, 5517, 5518, 5519, 5520, 5521, 5522, 5523, 5524, 5525, 5526, 5527, 5528, 5529, 5530, 5531, 5532, 5533, 5534, 5535, 5536, 5537, 6181, 6182, 6183, 6184, 6185, 6186, 6187, 6188, 6189, 6190, 6191, 6192, 6193, 6194, 6195, 6196, 6197, 6198, 6199, 6200, 6201, 6202, 6203], 

1: [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 2133, 2134, 2135, 2136, 2137, 2138, 2139, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844, 2845, 2846, 2847, 2848, 2849, 3514, 3515, 3516, 3517, 3518, 3519, 3520, 3521, 3522, 3523, 3524, 3525, 3526, 3527, 3528, 3529, 3530, 3531, 3532, 3533, 3534, 3535, 4193, 4194, 4195, 4196, 4197, 4198, 4199, 4200, 4201, 4202, 4203, 4204, 4205, 4206, 4207, 4208, 4209, 4210, 4211, 4212, 4213, 4214, 4869, 4870, 4871, 4872, 4873, 4874, 4875, 4876, 4877, 4878, 4879, 4880, 4881, 4882, 4883, 4884, 4885, 4886, 4887, 4888, 4889, 4890, 5538, 5539, 5540, 5541, 5542, 5543, 5544, 5545, 5546, 5547, 5548, 5549, 5550, 5551, 5552, 5553, 5554, 5555, 5556, 5557, 5558, 5559, 6204, 6205, 6206, 6207, 6208, 6209, 6210, 6211, 6212, 6213, 6214, 6215, 6216, 6217, 6218, 6219, 6220, 6221, 6222, 6223, 6224, 6225], 

2: [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165, 2166, 2167, 2168, 2169, 2170, 2171, 2172, 2173, 2174, 2175, 2176, 2177, 2178, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867, 2868, 2869, 2870, 2871, 2872, 3536, 3537, 3538, 3539, 3540, 3541, 3542, 3543, 3544, 3545, 3546, 3547, 3548, 3549, 3550, 3551, 3552, 3553, 3554, 3555, 3556, 3557, 3558, 4215, 4216, 4217, 4218, 4219, 4220, 4221, 4222, 4223, 4224, 4225, 4226, 4227, 4228, 4229, 4230, 4231, 4232, 4233, 4234, 4235, 4236, 4237, 4891, 4892, 4893, 4894, 4895, 4896, 4897, 4898, 4899, 4900, 4901, 4902, 4903, 4904, 4905, 4906, 4907, 4908, 4909, 4910, 4911, 4912, 5560, 5561, 5562, 5563, 5564, 5565, 5566, 5567, 5568, 5569, 5570, 5571, 5572, 5573, 5574, 5575, 5576, 5577, 5578, 5579, 5580, 5581, 6226, 6227, 6228, 6229, 6230, 6231, 6232, 6233, 6234, 6235, 6236, 6237, 6238, 6239, 6240, 6241, 6242, 6243, 6244, 6245, 6246, 6247], 

...
```



source_x_BIWI_10.npy
(68400, 20)     # 20 joints

```
array([[ 4.130e-02,  4.250e-02,  3.800e-02,  3.570e-02, -1.279e-01,
        -1.727e-01, -1.798e-01, -1.822e-01,  2.007e-01,  2.677e-01,
         2.896e-01,  2.892e-01, -3.220e-02, -1.400e-03,  1.730e-02,
         1.610e-02,  1.158e-01,  7.840e-02,  6.160e-02,  5.720e-02],
       [ 3.400e-02,  3.500e-02,  3.900e-02,  3.300e-02, -1.263e-01,
        -1.731e-01, -1.743e-01, -1.708e-01,  2.015e-01,  2.639e-01,
         2.901e-01,  2.918e-01, -4.240e-02,  3.360e-02,  5.070e-02,
         5.200e-02,  1.085e-01,  1.303e-01,  1.145e-01,  9.760e-02],
```



8

```
>>> frame_id_BIWI_8 = numpy.load('frame_id_BIWI_8.npy')
>>> frame_id_BIWI_8.shape
(8656,)
>>> frame_id_BIWI_8
array([ 0,  0,  0, ..., 49, 49, 49], dtype=int64)
>>> source_x_BIWI_8 = numpy.load('source_x_BIWI_8.npy')
>>> source_x_BIWI_8.shape
(69248, 20)
```



### train

python train.py --dataset BIWI --model prediction --length 10 --gpu 0

```
wsx log BIWI input_data shape (70098, 20)
wsx log BIWI input_data reshape (11683, 6, 20)
wsx log targets shape:  (11683, 6, 20)
wsx log input_data.tolist() len(input_data):  11683
wsx log targets tolist() len(targets):  11683
```

