## paper
```
Rao, H., Wang, S., Hu, X., Tan, M., Guo, Y., Cheng, J., ... & Liu, X. (2020). A Self-Supervised Gait Encoding Approach with Locality-Awareness for 3D Skeleton Based Person Re-Identification. arXiv preprint arXiv:2009.03671.
```

## github
```
https://github.com/1suancaiyu/Locality-Awareness-SGE
```
![frame_predit](D:\workspace\blog\frame_predit-1616511272077.png)


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

get _data_KGBD()
```
 275     # wsx: prediction
 276     elif Model == 'prediction':
 277         # suancaiyu targets
 278         targets = np.concatenate((input_data[1:,:,:], input_data[-1,:, :].reshape([1, time_steps, series_length])), axis=0)
 279         # input_data = input_data[:-1]
 280         input_data = input_data.tolist()
 281         targets = targets.tolist()
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

datasets
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

```
python train.py --dataset BIWI --model prediction --gpu 0
```

