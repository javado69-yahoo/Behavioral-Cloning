import cv2
from sklearn.model_selection import train_test_split
import os
import csv
import numpy as np
import sklearn.utils
angles=[]
rows_c=[]
images=[]
import cv2
with open(os.path.join("C:/myvenv/CarND-Behavioral-Cloning-P3/data/driving_log.csv"), 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        row_c=row[0]
        rows_c.append(row_c)
        angles.append(float(row[3]))
        
index=0        
for row in rows_c:
    image=cv2.imread(os.path.join("C:/myvenv/CarND-Behavioral-Cloning-P3/data/"+row))
    # index+=1
    # if index<20:
    images.append(image) 
train_samples, validation_samples = train_test_split(images, test_size=0.2, shuffle=True)
def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1: # Loop forever so the generator never terminates
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]
            images = []
            angles = []
            for batch_sample in batch_samples:
                name = './IMG/'+batch_sample[0].split('/')[-1]
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


