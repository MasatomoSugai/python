# 正方形をかく
# from turtle import *
# shape("turtle")
# for i in range(4):
#   forward(100)
#   left(90)
# done()

# カラフルな星を描く
# from turtle import *
# shape("turtle")
# col =["orange", "limegreen","gold","plum","tomato"]
# for i in range(5):
#   color(col[i])
#   forward(200)
#   left(144)
# done()

# カラフルな花を描く
# from turtle import *
# shape("turtle")
# col = ["orange","limegreen","gold","plum","tomato","blue","red","purple"]
# for i in range(8):
#   color(col[i])
#   circle(100)
#   left(45)
# done()

# 文字列の処理
# w = "こんにちは" +"\n"+ "私はパイソンです。"
# print(w)
# print(len(w))
# print(w[0])
# print(w[4:7])
# print(w[-2])
# print(w[4:])
# print(w[:8])

# 文字列の変換
# a = "100"
# print(a+20)
# 文字列と整数なので計算できない

# print(int(a)+20)
# これでOK

# うまく数値に変換できるのか判定できる チェックしたい変数.isdigit()
# b = "こんにちは"
# print(a.isdigit())
# print(b.isdigit())

# a = "100"
# b = "こんにちは"

# if b.isdigit():
#   print(int(b)+23)
# else:
#   print("数値じゃないよ")

# if a.isdigit():
#   print(int(a)+30)
# else:
#   print("数値じゃないよ")

# リストの書き方
# lunch=["おにぎり","パスタ","ハンバーガー","定食"]
# print(lunch[2])
# ランチをランダムで決めてみる
# import random
# print(random.choice(lunch))

# if文の練習
# score = 55
# if score <=60:
#   print("ドンマイ")
# elif score <= 80:
#   print("惜しかったね")
# else:
#   print("おめでとう")

# for文の練習
# for i in range(20):
#   print(7,"x",i,"=",7*i)
  
# scorelist = [64, 100, 78, 80, 72]
# total = 0
# for i in scorelist:
#   # print(i)
#   # print(i*10)
#   total = total + i
#   print(total)
# print ("合計は",total,"です")

# for文の入れ子
# for i in range(10):
#   for j in range(10):
#     print(j,"x",i,"=",j*i)

# 関数
# def sayhello():
#   print("こんにちは")

# sayhello()
# sayhello()
# sayhello()

# 消費税⑧％を計算してくれるプログラム
# def postTaxPrice(price):
#   ans = price*1.08
#   return ans

# print(postTaxPrice(100), "円")
# print(postTaxPrice(1200), "円")
# print(postTaxPrice(14440), "円")

# 引数だけある関数
# def sayhello2(name):
#   print("こんにちは、" + name + "さん。")
# sayhello2("スガイ")

# 戻り値だけある関数
# import random
# def omikuji():
#   kuji = ['大吉',"中吉","小吉","凶"]
#   return random.choice(kuji)
# kekka = omikuji()
# print("結果は。。。。",omikuji(),"でした！！！！")
# print("結果は。。。。",kekka,"でした！！！！")
# どちらでもエラーにはならない

# モジュールを作ってみよう
# tax.pyに関数を設置してそれを呼び出す。tax.が必要になる。
# import tax

# print(tax.postTaxPrice(100), "円")
# print(tax.postTaxPrice(1200), "円")
# print(tax.postTaxPrice(14440), "円")

# 時刻を扱うモジュール カレンダーを表示
import calendar
print(calendar.month(1984,12))
