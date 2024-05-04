# TwisterFingers - Хакатон

### Про проект:
- Твистер, но только для пальцев на клавиатуре
- На экране будет выведены клавиши. Нужно зажать определённую клавишу пальцем (либо переставить)
- Игра развитие моторику пальцев
- Игра написана на Python3 + PyQt5

### Запуск проекта:
```shell
# Linux
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt

# Windows
py -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt

# Запуск
python main.py
```

### Структура проекта:
- `ui/` - интерфейс программы
- `libs/` - библиотеки и модули программы
- `data/` - данные 

### Release
Программа собрана в два исполняемых файла. Программу можно запустить на Linux и Windows. 
