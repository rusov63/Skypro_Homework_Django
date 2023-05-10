## Урок 19.2 Знакомство с Django. Домашнее задание

### Реализовано в проекте:
#### 1. Настроено виртуальное окружение - pipenv
    - python -m venv env
    - env\Scripts\activate.bat
   в файле requirements.txt - библиотеки которые были использованы для проекта

   для установки воспользуйтесь командой pip freeze > requirements.txt
   

#### 2. Установлен Django фреймворк
    - pip install django


#### 3. Создан проект
    - django-admin startproject config .

 
#### 4. Создано приложение с названием `catalog`
    - django-admin startproject config .


#### 5. В папке templates\main\ Реализовано три шаблона:
    - index.html Стартовая страница
    - contacts.html Реaлизовано поля для сбора обратной связи от пользователя, 
     который зашел на страницу контактов и отправил свои данные для обратной связи.
    - media.html Статьи публикуемые на странице блог


#### 6. Под каждый шаблон реализовано три контроллера и прописана маршрутизация
    - views.py. Реализовано POST обработка name, phone, message.

  
#### 7. Реализован metod='POST'


#### 8. Запуск интерпретатора через команду 
    - python manage.py runserver
    - https://127.0.0.1:8000/