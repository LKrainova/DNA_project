Программа для обработки и анализа нуклеотидных последовательностей 
из базы данных Национального центра биотехнологической информации США (NCBI)

# Структура проекта:

README.md - документация
main.py - файл для пользователя
EFetch - скрипт для скачивания fasta-файла из базы данных
... - тут ещё названия самих моих модулей
requirements.txt - файл со списком библиотек, которые нужно будет скачать


#### Суть работы программы:

Вы вводите: 
- Accession number нуклеотидной последовательности

Вы получаете:
- В папку проекта скачивается fasta-файл c данными по этой последовательности;
- Файл автоматически переименовывается в соответствии с Accession number;
- Программа анализирует последовательность и генерирует текстовый файл 
с результатами анализа, названный по Accession number


#### О формате FASTA:

FASTA - это текстовый формат для записи нуклеотидных или белковых последовательностей.

Имеет стандартную структуру:

1) Первая строка: описание последовательности
(Accession number, название организма, название гена). 
2) Вторая строка и далее: нуклеотидная последовательность. 
Всегда начинается со 2-ой строки и разбита на строки фиксированной длины 
(как правило, по 60-70 нуклеотидов в строке).

Поскольку для анализа нам понадобится чистая последовательность, мы будем считывать файл 
со второй строки.



#### Quick start:

Подготовка:

#### Вам понадобится Accession number геномной последовательности, с которой Вы будете работать

1) Зайдите на страницу базы данных: https://www.ncbi.nlm.nih.gov/nucleotide/
2) Введите на латинском название интересующего вас организма
(например, мухомор: Amanita muscaria)
3) Нажмите "Поиск" и в появившемся списке выберите нужную вам последовательность
4) Скопируйте её индивидуальный номер (Accession number). При наличии нескольких версий скопируйте 
номер версии (Version)
(например: AJ010142.1)

#### Работа с программой

1) Клонируйте репозиторий в отдельную директорию на свой компьютер

2) Запустите скрипт EFetch
На ввод у Вас будет запрошен Accession number последовательности.
Скрипт скачает файл в формате .fasta в вашу ди и присвоит ему название по Accession number
запрошенной последовательности

3) Запустите файл main.py.
На ввод у Вас будет запрошен Accession number последовательности.
Импортированные в файл main.py библиотеке (!!!названия библиотек!!!) проведут
анализ последовательности и запишут результат в отдельный файл (!!! Название файла!!!)
