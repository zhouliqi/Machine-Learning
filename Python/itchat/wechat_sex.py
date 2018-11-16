# coding:utf-8

import itchat

'''
微信好友性别比例

'''

# 登录
itchat.auto_login(hotReload=True)

# 获取好友列表
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器
male = female = other = 0

# 遍历这个列表,列表的第一位是自己,从第二个人开始计算
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 计算比例
total = len(friends[1:])

# 打印结果
print(u"男性好友: %.2f%%" % (float(male) / total * 100))
print(u"女性好友: %.2f%%" % (float(female) / total * 100))
print(u"未填性别 %.2f%%" % (float(other) / total * 100))

'''
from echarts import echart, legend, pie
chart = echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')

chart.use(pie('WeChat',
              [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
               {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
               {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
                radius=["50%", "70%"]))
chart.use(legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()

'''
