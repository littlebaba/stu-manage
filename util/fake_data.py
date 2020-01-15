import datetime
from random import choice, randint

import numpy as np

cst_data = np.load('cst_data.npy', allow_pickle=True)
dt = datetime.datetime


def mk_name():
    _first, _second = cst_data[1], cst_data[2]
    _ming = [_second, ' ']
    strR = choice(_first) + choice(_second) + choice(choice(_ming))
    return strR.strip()


def mk_ID(max: str = '2010'):
    tmp = ''
    addr = cst_data[0]
    addr_num = choice(addr)[0]
    tmp = tmp + addr_num
    start, end = '1950-1-1', str(int(max) + 1) + '-1-1'
    delta = (dt.strptime(end, '%Y-%m-%d') - dt.strptime(start, '%Y-%m-%d')).days
    date = dt.strftime(dt.strptime(start, '%Y-%m-%d') + datetime.timedelta(randint(0, delta)), '%Y%m%d')
    tmp = tmp + date + str(randint(100, 1000))
    last_num = [str(i) for i in range(10)] + ['X']
    tmp = tmp + choice(last_num)
    return tmp


def mk_studentId(year: str='2017'):
    return '0' + year + str(randint(100, 1000))


def mk_tel():
    tel = cst_data[3]
    suffix = randint(9999999, 99999998) + 1
    tel = choice(tel) + str(suffix)
    return tel


def mk_unit():
    prefix, suffix = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'], '所'
    return choice(prefix) + suffix


def mk_train_order():
    prefix, suffix = list(range(1, 10)), '班'
    return str(choice(prefix)) + suffix


def mk_train_type():
    return choice(['A', 'B', 'C'])


def mk_position():
    return choice(['战士', '班长', '排长'])


def mk_gender(id):
    return '男' if int(id[-2]) % 2 == 1 else '女'


def mk_edu():
    edu = ['小学', '初中', '高中', '本科', '研究生', '博士']
    return choice(edu)


def mk_service():
    service = ['陆军', '海军', '空军']
    return choice(service)


def mk_train_time():
    return choice(['3月', '6月', '9月'])


def get_student():
    id=mk_ID()
    return mk_name(), id, mk_studentId(), mk_tel(), mk_unit(), mk_train_order(), \
           mk_train_type(), mk_position(), mk_gender(id), mk_edu(), mk_service(), mk_train_time()


if __name__ == '__main__':
    print(get_student())
