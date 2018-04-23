def encode(text, rot=0):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    code_text = ''
    if rot >= len(alpha):
        new_rot = rot - int(rot/len(alpha)) * len(alpha)
    else:
        new_rot = rot

    for k in text:
        if k.isalpha() == True:
            if k.isupper() == True:
                if alpha.index(k.lower()) + new_rot + 1 > len(alpha):
                    ind = alpha.index(k.lower()) + new_rot - len(alpha)
                    code_text += alpha[ind].upper()
                elif alpha.index(k.lower()) + new_rot + 1 <= len(alpha):
                    code_text += alpha[alpha.index(k.lower()) + new_rot].upper()

            elif k.islower() == True:
                if alpha.index(k.lower()) + new_rot + 1 > len(alpha):
                    ind = alpha.index(k.lower()) + new_rot - len(alpha)
                    code_text += alpha[ind]
                elif alpha.index(k.lower()) + new_rot + 1 <= len(alpha):
                    code_text += alpha[alpha.index(k.lower()) + new_rot]

        else:
            code_text += k

    print(code_text)
    if code_text == 'Ifmmp, Qzuipo3!':
        print('ok')
    elif code_text == 'Hello, Python3!':
        print('ok')
    elif code_text == "The cleaner and nicer the program, the faster it's going to run. And if it doesn't, it'll be easy to make it fast.":
        print('ok')
    elif code_text == 'Sgdqd hr mn oqnfqzllhmf kzmftzfd, mn lzssdq gnv rsqtbstqdc, sgzs vhkk oqdudms oqnfqzlldqr eqnl lzjhmf azc oqnfqzlr.':
        print('ok')
    #elif code_text == 'Hello, Python3!':
    #    print('ok')
    else:
        print('no')



def decode(text, rot=0):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    code_text = ''
    if rot >= len(alpha):
        new_rot = rot - int(rot/len(alpha)) * len(alpha)
    else:
        new_rot = rot

    for k in text:
        if k.isalpha() == True:
            if k.isupper() == True:
                if alpha.index(k.lower()) - new_rot < 0:
                    ind = alpha.index(k.lower()) + len(alpha) - new_rot
                    code_text += alpha[ind].upper()
                elif alpha.index(k.lower()) - new_rot >= 0:
                    code_text += alpha[alpha.index(k.lower()) - new_rot].upper()

            elif k.islower() == True:
                if alpha.index(k.lower()) - new_rot < 0:
                    ind = alpha.index(k.lower()) + len(alpha) - new_rot
                    code_text += alpha[ind]
                elif alpha.index(k.lower()) - new_rot  >= 0:
                    code_text += alpha[alpha.index(k.lower()) - new_rot]

        else:
            code_text += k

    print(code_text)
    if code_text == 'Hello, Python3!':
        print('ok')
    elif code_text == 'Hello, Python3!':
        print('ok')
    elif code_text == "Gur pyrnare naq avpre gur cebtenz, gur snfgre vg'f tbvat gb eha. Naq vs vg qbrfa'g, vg'yy or rnfl gb znxr vg snfg.":
        print('ok')
    elif code_text == 'There is no programming language, no matter how structured, that will prevent programmers from making bad programs.':
        print('ok')
    #elif code_text == 'Hello, Python3!':
    #    print('ok')
    else:
        print('no')


encode('z',27)
encode('Hello, Python3!',26000000000)
#encode('Hello, Python3!',30)
encode("Gur pyrnare naq avpre gur cebtenz, gur snfgre vg'f tbvat gb eha. Naq vs vg qbrfa'g, vg'yy or rnfl gb znxr vg snfg.", 13)
encode('There is no programming language, no matter how structured, that will prevent programmers from making bad programs.', 25)
#encode('Ifmmp, Qzuipo3!',1)

print('===================')

decode('z',27)
decode('Ifmmp, Qzuipo3!',1)
decode("The cleaner and nicer the program, the faster it's going to run. And if it doesn't, it'll be easy to make it fast.",13)
decode('Sgdqd hr mn oqnfqzllhmf kzmftzfd, mn lzssdq gnv rsqtbstqdc, sgzs vhkk oqdudms oqnfqzlldqr eqnl lzjhmf azc oqnfqzlr.',25)

