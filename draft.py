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



import pandas as pd
import time

start = time.time()
db = pd.read_excel('C:/Users/Иван/Desktop/ВСОШ 8 red.xlsx')
print(time.time() - start)

start = time.time()
lst = set(db['ФИО'].to_list())
print('qwe' in lst)
# print(set(db['ФИО'].to_list()))
# db = db[db['ФИО'].isin(['nan'])]
# db = db[db['Класс'].isin(['8Б'])]
# db = db[db['Итальянский язык'].isin(['sit29/sch771190/8/2g759g'])]
# print(db)
print(time.time() - start)



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