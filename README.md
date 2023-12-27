### QRKot

### Описание:
Проект QRKot - приложение для Благотворительного фонда поддержки котиков. 

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.


### Инструкция по запуску:
**Клонируйте репозиторий:**
```
git clone git@github.com:SGERx/cat_charity_fund.git
```

**Установите и активируйте виртуальное окружение:**
для MacOS:
```
py -3.9 -m venv venv
```

для Windows:
```
py -3.9 -m venv venv
source venv/bin/activate
source venv/Scripts/activate
```
**Установите зависимости из файла requirements.txt:**
```
pip install -r requirements.txt
```

**Из корневой директории запустите приложение:**
```
uvicorn app.main:app
```


### Документация приложения:
- Swagger
```
http://127.0.0.1:8000/docs
```

- Redoc
```
http://127.0.0.1:8000/redoc
```


### Отправка запросов:

Подробные примеры запросов описаны в интерфейсе Swagger, там же можно протестировать их отправку:

```
http://127.0.0.1:8000/docs
```

- Аккаунт superuser:
```
username: superuser@example.com
password: 12345
```

- Аккаунт обычного пользователя:
```
username: user@example.com
password: 12345
```


### Технологии:
- Python 3.9
- FASTApi
- SQLAlchemy
- Alembic
- Pydantic
- Google Cloud Platform
- Google Sheets API
- Google Drive API
