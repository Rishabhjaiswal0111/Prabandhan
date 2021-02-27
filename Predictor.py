import numpy as np
import cv2
import glob
from keras.models import Sequential
from keras.models import load_model
# from sklearn.preprocessing import LabelBinarizer
# from sklearn.model_selection import train_test_split
from keras.utils import np_utils

global size
size = 100
# model = Sequential()
model = load_model('Pothole_model.h5')


## load Testing data : non-pothole
#nonPotholeTestImages = glob.glob("D:/sagar/My Dataset/test/Plain/*.jpg")
# nonPotholeTrainImages.extend(glob.glob("C:/Users/anant/Desktop/pothole-and-plain-rode-images/My Dataset/train/Plain/*.jpeg"))
# nonPotholeTrainImages.extend(glob.glob("C:/Users/anant/Desktop/pothole-and-plain-rode-images/My Dataset/train/Plain/*.png"))
#test2 = [cv2.imread(img,0) for img in nonPotholeTestImages]
# train2[train2 != np.array(None)]
'''
for i in range(0,len(test2)):
    test2[i] = cv2.resize(test2[i],(size,size))
temp4 = np.asarray(test2)
'''

## load Testing data : potholes
def find_potholes(path):
    potholeTestImages = glob.glob('static/'+path)
    test1 = [cv2.imread(img,0) for img in potholeTestImages]
    for i in range(0,len(test1)):
        test1[i] = cv2.resize(test1[i],(size,size))
    temp3 = np.asarray(test1)



    X_test = []
    X_test.extend(temp3)
    #X_test.extend(temp4)
    X_test = np.asarray(X_test)

    X_test = X_test.reshape(X_test.shape[0], size, size, 1)



    # y_test1 = np.ones([temp3.shape[0]],dtype = int)
    #
    # y_test = []
    # y_test.extend(y_test1)
    # y_test = np.asarray(y_test)
    #
    # y_test = np_utils.to_categorical(y_test)




    tests = model.predict_classes(X_test)
    print(tests)
    for i in range(len(X_test)):
        if (tests[i]) == 0:
            return "Plain road"
        elif (tests[i]) == 1:
            return "Pothole"
        else:
            return "Error"



'''
metrics = model.evaluate(X_test, y_test)
for metric_i in range(len(model.metrics_names)):
     metric_name = model.metrics_names[metric_i]
     metric_value = metrics[metric_i]
     print('{}: {}'.format(metric_name, metric_value))
'''