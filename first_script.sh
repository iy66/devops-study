#!/bin/bash
# Это шебанг (магия), который говорит: "Запускай меня через Bash"

echo "Начинаю работу..."

current_folder=$(pwd)
echo "Я в папке: $current_folder"

files_count=$(ls -1 | wc -l| xargs)
echo "В этой папке $files_count файлов и папок"

echo "Работа закончена!"
