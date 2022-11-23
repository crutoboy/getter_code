import time
import openpyxl as xl

file = xl.load_workbook('C:/Users/Иван/Desktop/ВСОШ 8 red.xlsx', False)

db = file[file.sheetnames[0]]

start = time.time()

# print(db['1'][-1].column)
header = tuple(map(lambda x: x.value, db['1']))
# print(header)

for i in db.rows:
    if i[header.index('ФИО')].value == None and i[header.index('Класс')].value == '8Б':
        print(tuple(map(lambda x: x.value, i)))
        i[header.index('ФИО')].value = '16418426'
        break
    # print(tuple(map(lambda x: x.value, i)))

print(time.time() - start)
# db.close()
file.save('C:/Users/Иван/Desktop/ВСОШ 8 red.xlsx')


# lst = [2,3,1,4,9,5].sort()
# for i in lst:
#     print(i)
# print(len(lst))
# import random

# lst = [1,2,3,4,5,6,7,8,9]

# print(random.choice(lst))


# import json
# import requests
# lst = []
# for _ in range(100):
#     r = requests.get('http://free-generator.ru/generator.php?action=word&type=1')
#     lst.append(r.json()['word']['word'])
# print(lst)




# lst = []
# while True:
#     tmp = input()
#     if tmp == 'стоп':
#         break
#     lst.append(tmp)
# print(lst)


# import tkinter.filedialog as tk

# print(tk.askopenfilename())

# import json

# jsn = json.load(open('ex.json'))
# print(jsn)
# print(type(jsn))
# print(jsn['token'])
# print(jsn['admins'])
# print(type(jsn['admins']))

# res = 256_000_000_000
# count = 1
# i = 1
# while i < res:
#     count += 1
#     i = i * 2 + 1

# print(i)
# print(count)


# from numpy import nan
# import pandas as pd
# import time

# db = pd.read_excel('C:/Users/Иван/Desktop/ВСОШ 8 red.xlsx')

# start = time.time()

# db.at[db[(db['ФИО'].isnull()) & (db['Класс'] == '8А')].first_valid_index(), 'ФИО'] = '3547681'

# print(time.time() - start)
# print(db)




# import sqlite3
# import pandas as pd

# sql = sqlite3.connect('C:/Users/Иван/Desktop/test.db')
# xl = pd.read_excel('C:/Users/Иван/Desktop/ВСОШ 8 red.xlsx')
# xl.to_sql(name='mytable',con=sql,if_exists='replace',index=True)

# sql.commit()
# sql.close()




# import pandas as pd

# db = pd.read_excel('C:/Users/Иван/Desktop/ВСОШ 8 red.xlsx')

# # print(db)
# print(db['Класс'].tolist())
# print(set(db['Класс'].tolist()))