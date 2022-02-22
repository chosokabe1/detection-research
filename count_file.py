import os
 
#ディレクトリのパスを指定
dir = '../gousei_rot_50'
 
#ファイル数を出力
print(sum(os.path.isfile(os.path.join(dir, name)) for name in os.listdir(dir)))
