import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

def imageToData(filename): #画像ファイルを数値リストに変換
  #画像を8x8のグレースケールに変換
  grayImage = PIL.Image.open(filename).convert("L") 
  grayImage = grayImage.resize((8,8), PIL.Image.ANTIALIAS) #ANTIALIASで小さくても自然な画像になるように指定
  #数値リストに変換
  numImage = numpy.asarray(grayImage, dtype = float) #画像を8x8の数値リストに変換
  print(numImage)
  numImage = numpy.floor(16 - 16 *(numImage /256))
  print(numImage)
  numImage = numImage.flatten()
  print(numImage)
  return numImage

def predictDigits(data): #数字を予測する
  digits = sklearn.datasets.load_digits() #学習用データを読み込む
  #機械学習する
  clf = sklearn.svm.SVC(gamma = 0.001) #学習の準備
  clf.fit(digits.data, digits.target) #データを使って学習
  #予測結果を表示する
  n = clf.predict([data])
  print("予測＝", n)

data = imageToData("3.png")
predictDigits(data)
