import io
import os
from shutil import copyfile

#(os) get duong dan hien tai
# print(os.getcwd())

#(os) doi duong dan thu muc
# os.chdir(r'C:\Users\nghiahsgs\Desktop\Python-Automation-Course-nghiahsgs\bai 2 Thao tac voi file')

#(os) tao 1 file
# f=open('nghiahsgs.txt','w')
# f.close()

#(os) doi ten 1 file
# os.rename(src, dst) 

#(os) xoa 1 file
# os.remove("ahhihi.txt")

#shutil copy file
# copyfile(src,dst)

#viet file ko utf8
# def writeFileLine(filename, nd_line):
# 	f = open(filename, "a")
# 	f.write(nd_line + '\n')
# 	f.close()

#viet file co utf8 => append
# def writeUtf8(filename,nd_line):
#     f = io.open(filename, mode="a", encoding="utf-8")
#     f.write(nd_line + '\n')
#     f.close()


#doc file co utf8
# f = io.open("nghiahsgs2.txt", mode="r", encoding="utf-8")
# list_lines=f.readlines()
# print(list_lines)
# for line in list_lines:
#     print(line)

#doc file ko co utf8
# f=open("file_demo.txt", mode="r")
# f.read()
# f.readlines()
