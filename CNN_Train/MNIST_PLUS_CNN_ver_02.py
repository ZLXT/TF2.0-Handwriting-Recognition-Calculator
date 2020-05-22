import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets,layers,optimizers,Sequential,metrics,models
import matplotlib.pyplot as plt
import  os
import random

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
os.environ['CUDA_VISIBLE_DEVICES'] = '/gpu:0'

import pathlib

train_patch = pathlib.Path('C:/Users/ZLXT/Desktop/minst/train_minst')#图片路径
test_patch = pathlib.Path('C:/Users/ZLXT/Desktop/minst/test_minst')#图片路径
my_patch = pathlib.Path('C:/Users/ZLXT/Desktop/minst/My_Data')#图片路径

train_image_paths = list(train_patch.glob('*/*'))
test_image_paths = list(test_patch.glob('*/*'))
my_image_paths = list(my_patch.glob('*/*'))

train_image_paths = [str(path) for path in train_image_paths]
test_image_paths = [str(path) for path in test_image_paths]
my_image_paths = [str(path) for path in my_image_paths]

random.shuffle(train_image_paths)
random.shuffle(test_image_paths)
random.shuffle(my_image_paths)

train_label_names = sorted(item.name for item in train_patch.glob('*/') if item.is_dir())
test_label_names = sorted(item.name for item in test_patch.glob('*/') if item.is_dir())
my_label_names = sorted(item.name for item in my_patch.glob('*/') if item.is_dir())

train_label_to_index = dict((name, index) for index, name in enumerate(train_label_names))
test_label_to_index = dict((name, index) for index, name in enumerate(test_label_names))
my_label_to_index = dict((name, index) for index, name in enumerate(my_label_names))

train_image_labels = [train_label_to_index[pathlib.Path(path).parent.name]#图片标签
                    for path in train_image_paths]

test_image_labels = [test_label_to_index[pathlib.Path(path).parent.name]#图片标签
                    for path in test_image_paths]

my_image_labels = [my_label_to_index[pathlib.Path(path).parent.name]#图片标签
                    for path in my_image_paths]

def preprocess(path, label):
    img = tf.io.read_file(path)
    img = tf.io.decode_jpeg(img, channels=1)
    img = tf.image.resize(img, [28, 28])
    #img = tf.image.random_flip_up_down(img)
    #img = tf.image.random_crop(img, [28, 28, 1])
    img = tf.cast(img, dtype=tf.float32) / 255.
    label = tf.convert_to_tensor(int(label))
    label = tf.one_hot(label, depth=16)
    return img, label

batchsz =128
train_db = tf.data.Dataset.from_tensor_slices((train_image_paths, train_image_labels))
train_db = train_db.shuffle(10000).map(preprocess).batch(batchsz)
test_db = tf.data.Dataset.from_tensor_slices((test_image_paths, test_image_labels))
test_db = test_db.map(preprocess).batch(batchsz)
my_db = tf.data.Dataset.from_tensor_slices((my_image_paths, my_image_labels))
my_db = my_db.map(preprocess).batch(batchsz)

network = Sequential([
    layers.Conv2D(16, (5, 5), activation='relu', input_shape=(28, 28,1)),
    layers.MaxPool2D((2, 2)),
    layers.Conv2D(32, (4, 4), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(rate=0.5),
    layers.Dense(128, activation='relu'),
    layers.Dropout(rate=0.5),
    layers.Dense(16, activation='softmax'),
])
network.summary()

network.compile(optimizer=optimizers.Adam(lr=1e-3),
		loss='categorical_crossentropy',
		metrics=['accuracy']
	)

#交叉训练试试
network.fit(train_db,validation_data=test_db, epochs=3, validation_freq=1)

network.fit(my_db,validation_data=test_db, epochs=4, validation_freq=1)

network.fit(train_db,validation_data=test_db, epochs=3, validation_freq=1)

network.fit(my_db,validation_data=test_db, epochs=4, validation_freq=1)
#network.evaluate(my_db)

network.save('model.h5')
print('saved total model.')