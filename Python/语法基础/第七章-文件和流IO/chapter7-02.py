#pickle


import pickle

my_list = ['小周', '九江学院', '计算机科学与技术系','A1613',20]
pickle_file = open('data2.pickle', 'wb')

pickle.dump(my_list,pickle_file)        #dump()是将数据写入文件
pickle_file.close()
