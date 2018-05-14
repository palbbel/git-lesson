#!/usr/bin/env python
# -*- coding: utf-8 -*-


dict = {}
dict1 = {}

ggg = ['Server: nginx/1.2.4\n', 'Date: Fri, 06 Oct 2017 23:23:55 GMT\n','Content-Type: text/html\n', 'Connection: keep-alive\n', 'Keep-Alive: timeout=20\n', 'X-Powered-By: PHP/5.5.5\n']
for ff in ggg:
    #print ff
    #ff= 'Server: nginx/1.2.4\n'
    dict.update([[x.strip() for x in ff.split(': ')], ])
'''
jj = 'Content-Type: text/html\n'
ff= 'Server: nginx/1.2.4\n'
s = '<name>\t<vasya>'
#print dict([[x[1:-1].strip() for x in s.split('\t')], ])
#{'name': 'vasya'}

dict.update([[x.strip() for x in ff.split(':')], ])
dict.update([[x.strip() for x in jj.split(':')], ])
#print dict([[x.strip() for x in ff.split(':')], ])
'''
#print dict

dict1.update({'dgds': 'eegg'})
print dict1

#print(ff.find(' ',3))


