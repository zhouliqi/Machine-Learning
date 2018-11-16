#天气查询

import urllib.request  
import json

import pickle
pickle_file = open('city_data.pickle', 'rb')
city = pickle.load(pickle_file)
pickle_file.close()

password = input("你想查询那个城市的天气：")

name1 = city[password]
File1 = urllib.request.urlopen('http://m.weather.com.cn/data/' +  name1)
weatherHTML = File1.read().decode('utf-8')  #读入打开的url
        
weatherJSON = json.JSONDecoder().decode(weatherHTML)    #创建json  
weatherINFO = weatherJSON['weatherinfo']
#输出天气信息
print('时间: ',weatherINFO['data_y'])
print('24小时天气: ')
print('-----------------------------------')
print('温度: ',weatherINFO['temp1'])
print('天气: ',weatherINFO['weather1'])
print('风速: ',weatherINFO['wind1'])
print('紫外线: ',weatherINFO['index_uv'])
print('穿衣指数: ',weatherINFO['index_d'])
print('-----------------------------------')
print('48小时天气: ')
print('-----------------------------------')
print('温度: ',weatherINFO['temp2'])
print('天气: ',weatherINFO['weather2'])
print('风速: ',weatherINFO['wind2'])
print('紫外线: ',weatherINFO['index48_uv'])
print('穿衣指数: ',weatherINFO['index48_d'])
print('-----------------------------------')
print('72小时天气: ')
print('-----------------------------------')
print('温度: ',weatherINFO['temp3'])
print('天气: ',weatherINFO['weather3'])
print('风速: ',weatherINFO['wind3'])
#print('紫外线: ',weatherINFO['index72_uv'])
#print('穿衣指数: ',weatherINFO['index72_d'])
input('按任意键退出; ')


