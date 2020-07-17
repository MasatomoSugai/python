# tkinterをインポートしてtkと略して使う
import tkinter as tk
import random

# def dispLabel():
  # lbl.configure(text="こんにちは")

# おみくじアプリ
def disLabel():
  kuji = ['大吉','中吉','小吉','凶']
  lbl.configure(text = random.choice(kuji))



# 画面を作る
root = tk.Tk()
# 画面の大きさを決める（ピクセル）
root.geometry("200x100")

# ラベルを作る
lbl = tk.Label(text="LABEL")
# ボタンを作る
btn = tk.Button(text="PUSH", command = disLabel)
# command~~で関数を実行するように修正

# 画面にラベルを配置する。packの命令を実行した順に上から配置される
lbl.pack()
# 画面にボタンを配置する
btn.pack()
# 作ったウィンドウを表示する。作った画面がこの命令で動き始める
tk.mainloop()
