# Behavioral-Cloning

Model: "sequential"
_________________________________________________________________
| Layer (type)              |         Output Shape      |        Param  |
|---------------------------|:-------------------------:|--------------:|
| lambda (Lambda)           | (None, 160, 320, 3)       |    0          |                                                                  
| random_flip (RandomFlip)  |  (None, 160, 320, 3)      |   0           |                                                                      
| cropping2d (Cropping2D)   |  (None, 90, 320, 3)       |    0          |                                                                      
| conv2d (Conv2D)           |   (None, 86, 316, 24)     |  1824         |                                                               
| conv2d_1 (Conv2D)         |      (None, 82, 312, 36)  |    21636      |                                                                  
| conv2d_2 (Conv2D)         |  (None, 78, 308, 48)      | 43248         |                                                                
| conv2d_3 (Conv2D)         |  (None, 76, 306, 64)      |  27712        |                                                                 
| conv2d_4 (Conv2D)         |   (None, 74, 304, 64)     |  36928        |
                                                                 
 flatten (Flatten)           (None, 1439744)           0         
                                                                 
 dropout (Dropout)           (None, 1439744)           0         
                                                                 
 dense (Dense)               (None, 100)               143974500 
                                                                 
 dropout_1 (Dropout)         (None, 100)               0         
                                                                 
 dense_1 (Dense)             (None, 50)                5050      
                                                                 
 dropout_2 (Dropout)         (None, 50)                0         
                                                                 
 dense_2 (Dense)             (None, 10)                510       
                                                                 
 dense_3 (Dense)             (None, 1)                 11        
                                                                 
=================================================================
Total params: 144,111,419
Trainable params: 144,111,419
Non-trainable params: 0
_________________________________________________________________



| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
