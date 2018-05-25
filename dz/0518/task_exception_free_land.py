

def get_free_land(data1, data2):
    a = None # сторона участка
    b = None # сторона участка
    s_garden = None # площадь грядки

    if data1[0] <= 0:
        #raise ValueError('Не задана площадь участка')
        return [ValueError, 'Не задана площадь участка']

    if data2[0] == 0 or data2[1] == 0:
        #raise ValueError('Не задана площадь грядки')
        return [ValueError, 'Не задана площадь грядки']

    s_land = data1[0] * 100
    data1_dif = data1[1]
    #data2_l = data2[0]
    #data2_w = data2[1]

    #dif = tuple(map(int,data1_dif.split(':')))
    dif = data1_dif.split(':')

    x = (s_land/(int(dif[0]) * int(dif[1]))) ** 0.5
    a = int(dif[0]) * x
    b = int(dif[1]) * x
    print('{}  {}'.format(a, b))

    s_garden = data2[0] * data2[1]

    if s_garden > s_land:
        #raise ValueError('азмер грядки больше размера участка')
        return [ValueError, 'Размер грядки больше размера участка']

    free_land = s_land - (s_land // s_garden) * s_garden
    return free_land

if __name__ == '__main__':
    data1 = input()#[6, '2:3']
    data2 = input()#[40, 28]
    print(get_free_land(data1, data2))