# Проект getter_code
## Начало работы
Для начала работы с проектом необходимо создать файл config.json по шаблону из [config_example.json](config_example.json) или переименновать [config_example.json](config_example.json) в config.json, далее дополнить его. После конфигурации можно будет запустить [основной файл (main.py)](main.py).

## Назначение папок
В репозитории две папки:
- [draft](draft) 
- [addon](addon)

В папке [draft](draft) находятся черновики, старый код и тп.
В папке [addon](addon) содержатся дополнения к проекту, которые не затрагивают основной код на прямую.

## Назначение веток
В репозитории две ветки:
- [master](https://github.com/crutoboy/getter_code/tree/master) 
- [indev](https://github.com/crutoboy/getter_code/tree/indev) 

Ветка [master](https://github.com/crutoboy/getter_code/tree/master) является основной, в ней публикуются стадии проекта, которые полностью работоспособны.
Ветка [indev](https://github.com/crutoboy/getter_code/tree/indev) содержит все наработки по проекту, включая все эксперементальные файлы и куски кода. Также код из этой ветки ***может не работать!!!***

## Задачи
- [x] Создать основу бота
- [x] Создать админ-панель
- [ ] Реализовать регистрацию
    - [x] Система регистрации по секретному слову
    - [ ] Рсширенная регистрация
        - [ ] Настройка напоминаний о проходящих олимпиадах
        - [ ] [Возможно] Уведомление о результатах олимпиады
- [ ] [Внеплановое] Переход на другую библиотеку для обрабтки таблицы
    - [x] Выбор библиотеки
    - [ ] Изучение документации
    - [ ] Полный переход
- [ ] Получение кодов олимпиады учениками

Если какой-то пункт задачи не ясен, можно обратиться ко мне.