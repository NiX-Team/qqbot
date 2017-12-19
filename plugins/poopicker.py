from datetime import datetime
from qqbot import qqbotsched


poopicker_list = ['勾雷',
                  '张沛',
                  '章强',
                  '李鑫瑜',
                  '周东生',
                  '袁小玲',
                  '洪渝涛']

pick_day = '19950418'


def get_today_poopicker():
    return poopicker_list[datetime.now().weekday()]

@qqbotsched(hour='10,15,20,21,22,23', minute='0')
def poopicker(bot):
    group = bot.List('group', 'NiX-Team')[0]
    
    if pick_day != datetime.now().strftime('%Y%m%d'):
        bot.SendTo(group, '{0}该你铲屎了'.format(get_today_poopicker()))

def onQQMessage(bot, contact, member, content):
    global pick_day
    if '@ME' in content and\
       member.name.split('-')[-1] == get_today_poopicker() and\
       '铲完了' in content:
        pick_day = datetime.now().strftime('%Y%m%d')
        bot.SendTo(contact, '朕知道了')
