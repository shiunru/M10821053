from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv1D, MaxPooling1D
from keras import backend as K




def build(width, height, classes):
    # initialize the model along with the input shape to be
    # "channels last" and the channels dimension itself
    model = Sequential()
    inputShape = (height, width)
    #         chanDim = -1         # 為了指定channel --> BatchNormalization

    # if we are using "channels first", update the input shape
    # and channels dimension
    #         if K.image_data_format() == "channels_first":
    #             inputShape = (depth, height)
    #             chanDim = 1

    # 第一層
    #         model.add(Dense(1, input_shape=(width,height)))

    # 第二層
    model.add(Conv1D(6, 2, input_shape=(width, height), activation='relu'))

    #         model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling1D(pool_size=2, strides=2))
    # 第三層
    model.add(Conv1D(12, 9, activation='relu'))

    #         model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling1D(pool_size=2, strides=2))  # 預設Stride = 2*2
    #         model.add(Dropout(0.25))

    # 最後一層，攤平
    model.add(Flatten())

    model.add(Dense(24, activation='relu'))

    #       model.add(BatchNormalization())
    #       model.add(Dropout(0.5))

    # ReLU-soft classifier
    model.add(Dense(classes, activation='relu'))

    # return the constructed network architecture
    return model
