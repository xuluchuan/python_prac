def three_list(menu):
    while True:
        print('-' * 20)
        for province in menu:
            print(province)
        print('-' * 20)
        province_choice = input('请选择要进入的省份，e退出：')
        if province_choice and province_choice in menu:
            cities = menu[province_choice]
            if not cities:
                print('内容为空')
                continue
        elif province_choice == 'e':
            return
        else:
            print('输入错误，请重新输入')
            continue
        while True:
            print('-' * 20)
            for city in cities:
                print(city)
            print('-' * 20)
            city_choice = input('请选择要进入的城市，q返回上一级, e退出：')
            if city_choice and city_choice in cities:
                locations = menu[province_choice][city_choice]
                if not locations:
                    print('内容为空')
                    continue
            elif city_choice == 'q':
                break
            elif city_choice == 'e':
                return
            else:
                print('输入错误，请重新输入')
                continue
            while True:
                print('-' * 20)
                for location in locations:
                    print(location)
                print('-' * 20)
                location_choice = input('请选择进入的位置, q返回上一级, e退出：')
                if location_choice and location_choice in locations:
                    companies = menu[province_choice][city_choice][location_choice]
                    if companies:
                        for company in companies:
                            print(company)
                    else:
                        print('内容为空')
                        continue
                elif location_choice == 'q':
                    break
                elif location_choice == 'e':
                    return
                else:
                    print('输入错误，请重新输入')
                    continue


menu_three = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

three_list(menu_three)
