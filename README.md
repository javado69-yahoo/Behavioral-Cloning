# Behavioral-Cloning
Model : Sequential
_________________________________________________________________
| Layer (type)            |    Output Shape            |   Param #  |
-------------------------------------------------------------------- 
| lambda (Lambda)         |   (None, 160, 320, 3)      | 0          |   
| random_flip (RandomFlip)|  (None, 160, 320, 3)       | 0          |
| cropping2d (Cropping2D) |    (None, 90, 320, 3)      |  0         |
| conv2d (Conv2D)         |       (None, 43, 158, 24)  |     1824   |
| conv2d_1 (Conv2D)       |       (None, 20, 77, 36)   |     21636  |
| conv2d_2 (Conv2D)       |       (None, 8, 37, 48)    |     43248  |
| conv2d_3 (Conv2D)       |       (None, 6, 35, 64)    |     27712  |
| conv2d_4 (Conv2D)       |       (None, 4, 33, 64)    |     36928  |
| flatten (Flatten)       |      (None, 8448)          |   0        |
| dropout (Dropout)       |       (None, 8448)         |     0      |
| dense (Dense)           |       (None, 100)          |     844900 |
| dropout_1 (Dropout)     |       (None, 100)          |     0      |
| dense_1 (Dense)         |       (None, 50)           |     5050   |
| dropout_2 (Dropout)     |       (None, 50)           |        0   |
| dense_2 (Dense)         |       (None, 10)           |        510 |
| dense_3 (Dense)         |       (None, 1)            |  11        |

=================================================================
Total params: 981,819
Trainable params: 981,819
Non-trainable params: 0
