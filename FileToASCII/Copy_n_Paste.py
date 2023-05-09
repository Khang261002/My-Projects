import os
import shutil

src = "D:\Gallery\Girl_with_a_Pearl_Earring.jpg"
file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(src)))
__current_location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_name = src.replace(file_location + "\\", '')
#print(file_name)
file_copy = __current_location__ + "\\" + file_name

if file_location != __current_location__:
    shutil.copyfile(src, file_copy)
    print(file_name + " created in " + __current_location__)
