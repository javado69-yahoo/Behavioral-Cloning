import csv
import os
import numpy as np
from keras.layers import Dense , Flatten,Cropping2D,Conv2D,Dropout,Lambda,RandomFlip
from keras import Sequential
import cv2
from sklearn.model_selection import train_test_split
import sklearn.utils
samples = []
with open('C:/myvenv/CarND-Behavioral-Cloning-P3/data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)  
train_samples, validation_samples = train_test_split(samples, test_size=0.2, shuffle=True)
def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1: # Loop forever so the generator never terminates
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]
            images = []
            angles = []
            for batch_sample in batch_samples:
                name = 'C:/myvenv/CarND-Behavioral-Cloning-P3/data/IMG/'+batch_sample[0].split('/')[-1]
                center_image = cv2.imread(name)
                center_angle = float(batch_sample[3])
                images.append(center_image)
                angles.append(center_angle)

            X_train = np.array(images)
            y_train = np.array(angles)
            yield sklearn.utils.shuffle(X_train, y_train)

# compile and train the model using the generator function
train_generator = generator(train_samples, batch_size=32)
validation_generator = generator(validation_samples, batch_size=32)
      

######## Keras Layers
model = Sequential()
model.add(Lambda(lambda x: x/255.0, input_shape=(160,320,3)))
model.add(RandomFlip(mode="horizontal"))
model.add(Cropping2D(cropping=((50,20), (0,0))))
model.add(Conv2D(24,(5,5), (2,2), activation='relu'))
model.add(Conv2D(36,(5,5), (2,2), activation='relu'))
model.add(Conv2D(48,(5,5), (2,2), activation='relu'))
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(Conv2D(64,(3,3), activation='relu'))
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(100))
model.add(Dropout(0.3))
model.add(Dense(50))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Dense(1))
model.compile(loss='mse',optimizer='adam')
model.summary()

model.fit(train_generator,validation_data=validation_generator, epochs=3,steps_per_epoch=len(train_samples),validation_steps=len(validation_samples))

model.save('modelf.h5')
print('Done')



