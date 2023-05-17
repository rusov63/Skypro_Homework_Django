## 20.1 Работа с ORM в Django. Домашнее задание

### Реализовано в проекте:

#### 1. Подключена СУБД PostgreSQL для работы в проекте. Настройки подключения вынесены в переменные окружения, смотрите config.settings.py
    - pip install psycopg2


#### 2. В приложении каталога создано две модели с полями. Cоздана миграции для новых моделей:
    - Product (Наименование, Описание, Изображение, Категория, Цена за покупку, Дата создания, Дата последнего изменения)
    - Category (Наименование, Описание)
    - python manage.py makemigrations


#### 3. Внесены изменения в модель категорий, добавлено поле created_at. Осуществлен откат миграции
    - creation_at = models.DateField(verbose_name='Дата создания')
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py migrate catalog 0001
![migrate_catalog_0001.png](screenshots%2Fmigrate_catalog_0001.png)



#### 4. Для моделей категории и продукта настроено отображение в административной панели.
#### Для категорий выведен id и наименование в список отображения, а для продуктов выведен в список id, название, 
#### цену и категорию. Отображение можно фильтровать по категории, а также осуществлять поиск по названию и полю описания.
    - python manage.py createsuperuser
    - localhost:8000/admin


#### 6. Через инструмент shell заполнен список категорий, применены фильтры.
    - python manage.py shell
    - Category.objects.create(name='Оборудование', description='Автотовары')
![objects.create.png](screenshots%2Fobjects.create.png)


    - category_list = category.objects.all()
![objects.all.png](screenshots%2Fobjects.all.png)


    - category_list = category.objects.filter(name='Детейлинг')
    - category_list.count(), category_list.exists()
![objects.filter, count(), exists().png](screenshots%2Fobjects.filter%2C%20count%28%29%2C%20exists%28%29.png)


    - category_list = category.objects.exclude(name='Домкраты')
![objects.exclude().png](screenshots%2Fobjects.exclude%28%29.png)


    - category_list = category.objects.get(pk=1)
![objects.get().png](screenshots%2Fobjects.get%28%29.png)


    - category_list = category.objects.get(name='9')
    - category_list.__dict__
    - category_list.delete()
![get, dict, delete().png](screenshots%2Fget%2C%20dict%2C%20delete%28%29.png)


#### Сформирована фикстура для заполнения и выгрузка json из базы данных.
    - python -Xutf8 manage.py loaddata catalog_product.json
    - python -Xutf8 manage.py dumpdata catalog -o catalog_product.json


#### Написана кастомная команда, которая умеет заполнять данные в базу данных
    - python manage.py catalog_fill.py
    - python manage.py product_fill.py






## Урок 19.2 Знакомство с Django. Домашнее задание

### Реализовано в проекте:
#### 1. Настроено виртуальное окружение - pipenv
    - python -m venv env
    - env\Scripts\activate.bat
   requirements.txt - использованые библиотеки для для проекта.

   Для установки воспользуйтесь командой pip install -r requirements.txt
   

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
    - Реализован metod='POST'

#### 7. Запуск интерпретатора через команду 
    - python manage.py runserver
    - https://127.0.0.1:8000/