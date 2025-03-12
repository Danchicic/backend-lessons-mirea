# Используем официальный образ Node.js в качестве базового
FROM node:18

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы проекта
COPY . .

# Собираем проект
RUN npm run build

# Указываем порт, который будет использоваться контейнером
EXPOSE 3000

# Запускаем приложение
CMD ["npm", "run", "preview"]