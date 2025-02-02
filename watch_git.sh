#!/bin/sh

# Функция для обновления кода и перезапуска приложения
update_and_restart() {
    echo "Checking for updates..."
    git pull
    if [ $? -eq 0 ]; then
        echo "Updates found, restarting application..."
        python main.py
    else
        echo "No updates found."
    fi
}

# Функция для проверки изменений в файле .env
check_env_changes() {
    if [ "$(cat .env | md5sum)" != "$(cat .env.bak | md5sum)" ]; then
        echo ".env file changed, restarting application..."
        cp .env .env.bak
        python main.py
    fi
}

# Бесконечный цикл для проверки изменений
while true; do
    update_and_restart
    check_env_changes
    sleep 60  # Проверять изменения каждую минуту
done