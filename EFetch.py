'''
Скрипт для получения данных из базы данных NCBI
(National Center for Biotechnology Information).

Используется EFetch - одна из утилит NCBI API,
позволяющая извлекать из NCBI данные в различных форматах.
'''


'''Библиотека для HTTP-запросов'''
# pip install requests
import requests

# def download_sequence():
'''Указываем параметры для запроса к API NCBI'''

base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi" # Базовый URL для EFetch
db = "nuccore" # база данных по нуклеотидам
# Здесь вводим accession number интересующей нас последовательности:
accession_number = input("Введите Accession number нуклетидной последовательности: \n") # Например: PQ633951.1
format = "fasta" # в каком формате хотим получить данные
mode = "text" # в каком виде мы хотим данные (ну мы хотим в блокноте)


'''
Конструируем эндпойнт-ссылку для запроса к API через EFetch,
запрашиваем данные у базы данных.
'''

api_url = f"{base_url}?db={db}&id={accession_number}&rettype={format}&retmode={mode}"
print(api_url)

'''
Вообще на этом этапе можно уже кликнуть на ссылку,
и файл сам скачается в загрузки. 

Но мы честно допишем GET-запрос!
'''

'''Делаем GET-запрос'''
try:
    ncbi_response = requests.get(api_url)
    print("Запрос на сервер отправлен успешно!")

except Exception as e:
    print(f"Не удалось подключиться к серверу,{e}")


'''
Если запрос прошёл успешно, скачиваем файл (куда?)
N.B. Если код в try не выполнился, то эта переменная и не создалась как бы и дальше
не пойдёт.
'''
# todo: куда скачиваем-то? Прописать папку "Здесь"

try:
    with open(f"{accession_number}.fasta", 'w+') as f:
        f.write(ncbi_response.text)
        print(f"Файл сохранён как {accession_number}.fasta")
except Exception as e1:
    print("Не удалось сохранить файл", e1)

# if __name__ == "__main__":
#     download_sequence()

