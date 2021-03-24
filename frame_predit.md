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


