## Чтобы запустить проект локально нужно:

1. Скачать python 3.12 с официального сайта
2. Склонировать репозиторий (git clone git@github.com:Danchicic/backend-lessons-mirea.git)
3. Перейти в ветку practice5-6(git checkout practice5-6)
4. скачать зависимости (pip install -r requirements.txt)
5. Открыть два терминала

## Запуск user view

В первом перейти в папку user_server(cd user_server)

```bash
uvicorn main:app --port 8080
```

## Запуск admin view

Во втором перейти в папку admin_server (cd admin_server)

```bash
uvicorn main:app --port 8000
```
## Теперь маршруты доступны по адресам
    localhost:8000/
    localhost:8080/

