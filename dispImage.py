import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
  # 画像を読み込む convert~で色の変換
  newImage = PIL.Image.open(path).convert("L").resize((20,20)).resize((300,300))
# そのイメージをラベルに表示する
  imageData = PIL.ImageTk.PhotoImage(newImage)
  imageLabel.configure(image = imageData)
  imageLabel.image = imageData

def openFile():
  fpath = fd.askopenfilename()

  if fpath:
    dispPhoto(fpath)
  else:
    print("そうですか。。。")

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()



