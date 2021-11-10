#!/bin/env python3
#coding = -*- UTF-8 -*-
import sys
class cat_mon(object):
    '''This class is for catching the month to table'''
    def __init__(self):
        year,month = self.get_input()
        days = self.get_days(month,year)
        self.main(year,month,days)

    def get_input(self):
        try:
            date = sys.argv[1]
        except:
            date = input('需要哪年哪个月? 如2000.01')
        year_month = date.split('.')
        year = int(year_month[0])
        month = int(year_month[1])
        return year,month

    def get_days(self,m,y):
        def is_leap(y):
            if y % 100 == 0:
                return y % 400 == 0
            return y % 4 == 0
        if m in [1,3,5,7,8,10,12]:
            return 31
        elif m in [4,6,9,11]:
            return 30
        elif m == 2 and is_leap(y):
            return 29
        else:
            return 28
        
    def main(self,y,m,d):
        sd = []
        for i in range(1,d + 1):
            sd.append(str(i))
        with open('{}.{}_list.tsv'.format(y,m),'w',encoding='gbk') as f:
            f.write('Things\t{}\n'.format('\t'.join(sd)))

if __name__ == '__main__':
    cat_mon()

