def camel_to_snake(name):
    snake = ''
    letters = []
    for i in range(len(name)):
        letters.append(name[i])
        if letters[i].isupper():
            if i == 0:
                snake +=  name[0].lower()
            elif i != 0:
                snake += '%s%s' %('_',name[i].lower())
        elif letters[i].islower() or letters[i].isalpha() == False:
            snake += '%s' % (name[i])


    print(snake)








def snake_to_camel(name):
    snake = name.split('_')
    camel = ''
    for element in snake:
        camel = camel + element.title()

    print(camel)




snake_to_camel('gou_errt_eury')


camel_to_snake('Yh3jRh4ghgOjbj33kb')