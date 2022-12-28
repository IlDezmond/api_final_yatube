# api_final

## Описание
Backend для Yatube. Социальной сети блогеров.

## Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/IlDezmond/api_final_yatube.git
```

```
cd yatube_api
```

Создать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов
Документация api
```
http://127.0.0.1:8000/redoc/
```
___
Получение списка постов
```
GET /api/v1/posts/
```
Ответ
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-10-14T20:41:29.648Z",
        "image": "string",
        "group": 0
    }
  ]
}
```
___
Создание поста
```
POST /api/v1/posts/
```
Payload
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Ответ
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
___
Получение одного поста
```
GET /api/v1/posts/{id}/
```
Ответ
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
___
Получение списка групп
```
GET /api/v1/groups/
```
Ответ
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```



