#任务一：向文件输出句子
'''1，使用print的方式进行输出（输出的目的地是文件）'''
fp=open('G:\Python1\chap17\实操案例1\\text.txt','w',encoding='utf-8')
print('奋斗成就更好的你',file=fp)
fp.close()

'''2.使用文件的读写操作'''
with open('G:\Python1\chap17\实操案例1\\text1.txt','w',encoding='utf-8') as file:
    file.write('奋斗吧，年轻人！！！')


