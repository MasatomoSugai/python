
# 数字のデータを数値リストで表示
# import sklearn.datasets

# digits = sklearn.datasets.load_digits()

# print("データの個数=", len(digits.images))
# print("画像データ=", digits.images[3])
# print("なんの数字か=", digits.target[3])

# 数値データを画像化
import sys #sixにpathが通っていないので明示的に追加
sys.path.append('/Users/user/Library/Python/3.8/lib/python/site-packages')

import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

# plt.imshow(digits.images[0], cmap="Greys") #数値データをグレーの濃淡画像にする
# plt.show()

for i in range(50):
  plt.subplot(5, 10, i+1) #5x10に順番に表示する
  plt.axis("off") #枠線を非表示
  plt.title(digits.target[i]) #この数字は何か
  plt.imshow(digits.images[i], cmap="viridis_r") #cmap=~で表示色の指定Greys,Pastle1,etc
plt.show()
