# noflags

1. Требуется python 3.X и 7zip
2. Склонировать репозиторий
```git clone https://github.com/qMBQx8GH/noflags```
3. Перейти в папку noflags
```cd noflags```
4. Установить зависимости
```python -m pip install -r requirements.txt```
5. Скопировать и настроить build.ini
```cp build.ini.dist build.ini```
6. Скопировать файлы из ресурсов игры
```python game_update.py```
7. Создать модифицированные файлы
```python make_flags.py```
8. Создать архив с модом для распаковки в папке с игрой
```build.cmd```
