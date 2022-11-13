

# res = 256_000_000_000
# count = 1
# i = 1
# while i < res:
#     count += 1
#     i = i * 2 + 1

# print(i)
# print(count)



# import pandas as pd

# db = pd.read_excel('C:/Users/Иван/Desktop/ВСОШ 8 red.xlsx')

# print(db[db['Класс'].isin(['8Б'])])




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