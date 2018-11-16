#==============================================

'''
with open(r'E:\Python3\data1.txt','w') as f:
    f.write('123\n')
    f.write('abc\n')
    f.writelines(['456\n','def\n']) #写入一个序列

with open("data1.txt",'a') as f:
    f.write("我是小周啊\n")
    f.write("我在九江学院计算机科学与技术系A1613班\n")


'''

'''
with open(r'data1.txt','r') as f:
    for s in f:
        print(s,end='')
    print('\n')

'''

'''
f = open('data1.txt')
for each_line in f:
    print(each_line,end='')
f.close()
'''

#分割文件

def save_file(you,me,count):
        file_name_you = 'you' + str(count) + '.txt'
        file_name_me  = 'me_' + str(count) + '.txt'
            
        you_file = open(file_name_you, 'w')
        me_file  = open(file_name_me,  'w')

        you_file.writelines(you)
        me_file.writelines(me)
            
        you_file.close()
        me_file.close()
        
def split_file(file_name):
    f = open(file_name)

    you = []
    me  = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            #字符串分割操作
            
            (role, line_spoken) = each_line.split(':', 1)
            
            if role == '你':
                you.append(line_spoken)
            if role == '我':
                me.append(line_spoken)
        else:
            save_file(you,me,count)     #保存
            you = []
            me  = []
            count+=1
    save_file(you,me,count)

    f.close()

split_file("data1.txt")















