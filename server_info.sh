#!/bin/bash
echo "Начинаю работу..."

server=$(hostname|xargs)
echo "Сервер: $server"

user=$(whoami|xargs) 
echo "Пользователь: $user"

empty=$(df -h / | tail -1 | awk '{print $4}'|xargs)
echo "Свободно на диске: $empty"

uptime=$(uptime | awk '{print $10}' | xargs)
echo "Загрузка системы:$uptime"
