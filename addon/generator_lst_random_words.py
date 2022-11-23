import requests
lst = []
for _ in range(100):
    r = requests.get('http://free-generator.ru/generator.php?action=word&type=1')
    lst.append(r.json()['word']['word'])
print(lst)