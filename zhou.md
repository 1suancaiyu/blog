# zhou:
```
## week3
两个数据格式不同的数据集，是如何区分处理的
数据集的实际运动类型

## week4
找预测最后预测最后一帧的项目代码去借鉴
https://github.com/1suancaiyu/Locality-Awareness-SGE

###3
今日任务：
看懂那个预测下一帧的代码思想，并借鉴构造基于st-gcn 的 auto-encoder

完成情况：

查明是代码如何完成预测下一帧这个任务

单从auto-encoder的构造来看，是没有对这三个pre_task有区分的

初步猜想应该是loss约束来区分不同

这里是用
train_loss = tf.reduce_mean(tf.nn.l2_loss(training_decoder_output - targets))

然后这里的targets 应该就是装的下一帧的数据

具体还需要再细看，必要时需要运行代码
