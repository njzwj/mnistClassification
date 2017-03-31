# coding=utf-8
import struct
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from PIL import Image
from sklearn.externals import joblib
# ==================
# data preprocessing
# images in MNIST are 28 * 28 pixels
# ==================

labels = {}
# normalize image
def convert_img(image):
  image = np.array(image)
  return np.round(image / 255)

# read files
def read_image(filename):
  f = open(filename, 'rb')

  index = 0
  buf = f.read()
  f.close()

  magic, images, rows, columns = struct.unpack_from('>IIII', buf, index)
  index += struct.calcsize('>IIII')

  data_set = np.zeros((images, rows*columns))
  for i in range(images):
    raw_image = []
    for x in range(rows):
      for y in range(columns):
        raw_image.append(int(struct.unpack_from('>B', buf, index)[0]))
        index += struct.calcsize('>B')
    image = convert_img(raw_image)
    data_set[i, : ] = image
  return data_set

def read_label(filename):
  f = open(filename, 'rb')

  index = 0
  buf = f.read()
  f.close()

  magic, items = struct.unpack_from('>II', buf, index)
  index += struct.calcsize('>II')

  data_set = np.zeros((items, 1))
  for i in range(items):
    item = int(struct.unpack_from('>B', buf, index)[0])
    index += struct.calcsize('>B')
    data_set[i, :] = item
  return data_set

# create model
def create_svm(dataMat, dataLabel):
  clf = LinearSVC(multi_class='ovr', verbose = True)
  clf.fit(dataMat, dataLabel)
  return clf

# ====
# main
# ====
def main():
  # load and train
  train_data = read_image('./data/train-images.idx3-ubyte')
  train_label = read_label('./data/train-labels.idx1-ubyte')
  print('='*20)
  print('training...')
  svm = create_svm(train_data, train_label.ravel())
  print('done.')
  joblib.dump(svm, './dump/default.m')

  # load model(if exists)
  # svm = joblib.load('./dump/default.m')
  # test_data = read_image('./data/t10k-images.idx3-ubyte')
  # test_label = read_label('./data/t10k-labels.idx1-ubyte')
  
  acc = round(svm.score(test_data, test_label.ravel())*100, 2)
  print('accuracy: ', acc)

  # random test and show
  for i in range(100):
    idx = random.random() * 10000
    img = Image.new('1', (28, 28))
    for y in range(28):
      for x in range(28):
        img.putpixel((x, y), int(test_data[idx][y*28+x]))
    print('='*20)
    predict = svm.predict(test_data[idx])
    print(predict)
    print(' ')
    plt.imshow(img, cmap='gray')
    plt.show()

  

main()
