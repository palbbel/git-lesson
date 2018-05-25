import json
import re

path_src = 'headers-1.txt'
#path_src = 'headers-2.txt'
#path_src = 'headers-3.txt'

def http_headers_to_json():
    #path_src = str(input())
    #path_dest = str(input())
    data_dict = {}

    with open(path_src) as f:
        list_line = f.readlines()

    for row in list_line[1:]:
        if row != '\n':
            data_dict.update([[x.strip() for x in row.split(': ')], ])

    check_answer = re.match('HTTP', list_line[0])
    # файл с заголовком запроса
    if not check_answer:
        data_dict.update({'method': list_line[0][:list_line[0].find(' ')]})
        data_dict.update({'uri': list_line[0][list_line[0].find(' ')+1:list_line[0].find(' ', list_line[0].find(' ')+1)]})
        data_dict.update({'protocol': list_line[0][list_line[0].find(' ', list_line[0].find(' ')+1)+1:].replace('\n', '')})

    # файл с заголовком ответа
    else:
        data_dict.update({'protocol': list_line[0][:list_line[0].find(' ')]})
        data_dict.update({'status_code': list_line[0][list_line[0].find(' ')+1:list_line[0].find(' ', list_line[0].find(' ')+1)]})
        # проверяем версию (не 2 версия)
        if list_line[0][:6] != 'HTTP/2':
            data_dict.update({'status_message': list_line[0][list_line[0].find(' ', list_line[0].find(' ')+1)+1:].replace('\n', '')})

    with open('results-1.json', 'w') as f:
    #with open('results-2.json', 'w') as f:
    #with open('results-3.json', 'w') as f:
    #with open(path_dest, 'w') as f:
        json.dump(data_dict, f, indent=4)

if __name__ == '__main__':
    http_headers_to_json()

