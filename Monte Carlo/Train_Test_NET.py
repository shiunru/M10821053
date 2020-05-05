from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv1D, MaxPooling1D
from keras import backend as K


labelNames = ["NOR", "US", "DS", "UT", "DT", "CYC"]

model = build(width=50, height=1 , classes=6)

print(model.summary())

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['acc','mse'])

H = model.fit(trainX, trainY,
          batch_size=64,
          epochs=16,
          verbose=1,
          validation_data=(testX, testY)
         )

# evaluate the network
from sklearn.metrics import classification_report
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=64)
print(classification_report(testY.argmax(axis=1),
    predictions.argmax(axis=1), target_names=labelNames))