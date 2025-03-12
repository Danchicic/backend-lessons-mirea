# My Shop

Это проект интернет-магазина, созданный с использованием React и Vite.

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/your-username/my-shop.git
    cd my-shop
    ```

2. Установите зависимости:

    ```sh
    npm install
    ```

## Запуск проекта

### Локально

Для запуска проекта в режиме разработки используйте команду:

```sh
npm run dev
```
С использованием Docker
Постройте Docker образ:


```sh
docker build -t my-shop .
```
Запустите контейнер:


```sh
docker run -p 3000:3000 my-shop
```

Приложение будет доступно по адресу http://localhost:3000.

Скрипты
npm run dev: Запуск проекта в режиме разработки.
npm run build: Сборка проекта.
npm run preview: Предпросмотр собранного проекта.
npm run lint: Запуск линтера.

Структура проекта
src/: Исходный код проекта.
public/: Публичные файлы.
Dockerfile: Конфигурация Docker.
vite.config.js: Конфигурация Vite.
eslint.config.js: Конфигурация ESLint.
