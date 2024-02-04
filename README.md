# <p align="center">ИНТЕРНЕТ-МАГАЗИН "Zay"</p>
![image](https://github.com/EvdokimovAnR/Online-shop-Zay/assets/145903848/b832499d-f0c5-43d4-a6ca-1e97c507761f)
---
## О проекте:
Добро пожаловать в наш интернет-магазин! У нас вы найдете широкий выбор товаров в удобном каталоге, где можно легко находить нужные вам предметы, добавлять их в корзину и оформлять заказ. Регистрация и авторизация позволят вам получить доступ к личному кабинету, где вы сможете управлять своим профилем и изменять настройки. Мы предлагаем удобный и безопасный способ оплаты товаров с помощью Stripe, так что вы можете совершать покупки со спокойным сердцем. 
## Технологии:
* Python 3.9.13
* Django  4.2.4
* Django REST framework 3.14.0
* django-debug-toolbar
* SQLite3
* HTML
* CSS
## Использование:
* Просматривайте категории товаров для выбора нужных вам продуктов.
* Добавляйте выбранные товары в корзину.
* Оформляйте заказ, указывая необходимые данные для доставки.
* Выбирайте удобный способ оплаты и вводите необходимую информацию.

## Видеообзор сайта:
https://github.com/EvdokimovAnR/Online-shop-Zay/assets/145903848/5d0e3efd-8041-40ba-968f-9122fd84b993

## Установка:
1. Клонируйте репозиторий:
```
https://github.com/EvdokimovAnR/Online-shop-Zay.git

cd Online-shop-Zay
```
Если вы не используете Git, вы можете просто скачать репозиторий исходного кода в ZIP-архив и распаковать его на свой компьютер.

2. Cоздайте виртуальное окружение:
* Для Mac и Linux: ``` python3 -m venv venv  ```
* Для Windows: ```python -m venv venv ```
  
3. Активируйте виртуальную среду:
* Для Mac и Linux: ``` source venv/bin/activate ```
* Для Windows: ```venv/bin/activate```
4. Установите  зависимости:
```
pip install -r requirements.txt
```
5. Создать в корне проекта .env и заполнить его по аналогии с файлом .env
6. Настройте и заполните базу данных:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata categories.json
python manage.py loaddata products.json
python manage.py loaddata productinfo.json
python manage.py loaddata users.json
```
7. Запустите сервер:
```
python manage.py runserver
```
Откройте браузер и перейдите по адресу http://127.0.0.1:8000



