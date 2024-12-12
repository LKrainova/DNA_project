"""Скрипт для получения данных из базы данных NCBI (National Center for Biotechnology Information).
Используется EFetch - одна из утилит NCBI API,позволяющая извлекать из NCBI данные в различных
форматах.
"""


'''Библиотека для HTTP-запросов'''
# pip install requests
import requests


'''Указываем параметры для запроса к API NCBI'''

base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi" # Базовый URL для EFetch
db = "nuccore" # база данных по нуклеотидам
# Здесь вводим accession number интересующей нас последовательности:
accession_number = input("Введите Accession number нуклетидной последовательности: \n") # Например: PQ633951.1
format = "fasta" # в каком формате хотим получить данные
mode = "text" # в каком виде мы хотим данные (ну мы хотим в блокноте)


'''Конструируем эндпойнт-ссылку для запроса к API через EFetch,
 запрашиваем данные у базы данных. '''

api_url = f"{base_url}?db={db}&id={accession_number}&rettype={format}&retmode={mode}"
print(api_url)
'''Вообще на этом этапе можно уже кликнуть на ссылку и файл сам скачается в загрузки, 
но мы честно допишем GET-запрос!
'''

'''Делаем GET-запрос'''
try:
    ncbi_response = requests.get(api_url)
    print("Запрос на сервер отправлен успешно!")

except Exception as e:
    print(f"Не удалось подключиться к серверу,{e}")


'''Если запрос прошёл успешно, скачиваем файл (куда?)
N.B. Если код в try не выполнился, то эта переменная и не создалась как бы и дальше
не пойдёт'''
# todo: куда скачиваем-то? Прописать папку "Здесь"

try:
    with open(f"{accession_number}.fasta", 'w+') as file:
        file.write(ncbi_response.text)
        print("Файл сохранён")
except Exception as e1:
    print("Не удалось сохранить файл", e1)
# Step 4: Check if the request was successful
# if response.status_code == 200:
#     # Step 5: Save the data to a file
#     with open("sequence.fasta", "w") as file:
#         file.write(response.text)
#     print("Sequence data saved to 'sequence.fasta'")
# else:
#     print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
#