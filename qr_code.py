import pyqrcode
Name = 'Amiya'
A = pyqrcode.create(Name)
A.png(Name+'.png',scale=15)
#To open Image automatically
import os
os.system(Name+'.png')