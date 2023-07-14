### Инструкция по развертыванию бэкенда в контейнере докер для тестирования фронтом:

- Клонировать себе репозиторий Back, перейти в ветку develop

- Перейти в папку encryption_machine

```cd encryption_machine```

- Запустить docker-compose:

```docker-compose -f docker-compose.develop.yaml up```

- При необходимости выполнить миграции внутри контейнера докер
```
python manage.py makemigrations
python manage.py migrate
```

- Документация redoc и swagger будет доступна по следующим адресам:
```
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
```
