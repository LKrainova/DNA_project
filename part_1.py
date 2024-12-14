#todo: научиться подтягивать сиквенсы из NCBI либо GenBank
# Ну или хотя бы из документа
# Отрезать у BLAST-формата его лишнюю часть
# Подумать, что делать с переводом букв в верхний регистр, чтобы пользователь постоянно работал с
# upper_case переменной (сразу добавлять на input? (dna = 'tgct'.upper()?)
#
# sur_dna = str(input("Введите ДНК: \n")).upper()
# print(sur_dna)
# dna = 'ctaatgagccatgctgatcgatgtccgttgcgagttttcgataacttaaaagcacgcggatacgtatttaggaaaaaacttatgtgagactcacctgagactaagtcgtgtggacctcaataagtcctttctaaggtatcacatcgaaacgcatagtgttgaaatccttttttcatgtaaattcaattgattctcgaaatctgcacaagtcgctgacaaactttaccttatcctagaagaggtacgcccacctgtccaggcgctgttgtcatgcaagtacattagcactacggagcggaataatcactccgatacgagacgtatatagacaggcgccgtcggtagagctagtgacgggcagctaccgtctctaataggagataactggctctcagacgacagccgcagccctacctgggttccaaccgtttacattaaactggcctacatggtgacgcctccagcaacataaccacaagtgtgttgttaggaagtagagtgtgctggaaccatcctcattggaaccttactgcgactgccggagttccaccatcgtgaagggccgagaataggtaacgtaaacgggacgcattgtctgaaaatgagtctccgagaagaaaagatcatttccattatagatgagttgcgacggaagtaacgtgtgtcaatgctagtcctggtagatggcgacaagcac'


with open(f"PQ633951.1.fasta", "r+") as f: # PQ633951.1
    lines = f.readlines()
    '''
    Убираем имеющиеся в FASTA-файле пробелы в конце строк.
    Читаем со второй строки.
    '''
    dna = ''.join(line.strip() for line in lines[1:])
print(dna)
print(type(dna))



# Вообще нужно перевести её в upper case и дальше с ним работать
def upper_dna(seq):
    DNA = seq.upper()
    return DNA

DNA = upper_dna(dna)
print(f'ДНК в корректной записи: {upper_dna(dna)}')


nucleotides = ["A", "T", "G", "C"]

# todo: Проверить, является ли приведённая последовательность ДНК (что нет лишних элементов)

def validating_sequence(seq):
    """
    Валидация последовательности

    Проверка, не содержится ли в последовательности ДНК элементов,
    не являющихся нуклеотидами.

    Параметры: ...
    - seq (str): строка, представляющая последовательность ДНК

    Возвращает:
    - print statement: утверждение, подтверждающее либо опровергающее то,
    что последовательность представляет собой ДНК
    - garbage_dict (dict): словарь с найденными ненуклеотидными элементами

    """

    nucleotides = ["A", "T", "G", "C"]
    garbage_dict = {}
    for index, nucl in enumerate(seq.upper()):
        if nucl in nucleotides:
            pass
        elif nucl not in nucleotides:
            garbage_dict[nucl] = index
            print(f"Обнаружен ненуклеотидный элемент {nucl} на позиции {index}!")

    if garbage_dict == {}:
        print("Данная последовательность является ДНК")

    return garbage_dict

validation_result = validating_sequence(dna)
print(validation_result)



#todo: Подсчёт количества каждого из нуклеотидов в цепи ДНК

def nucleotide_frequency(seq):
    """
    Подсчёт количественного содержания нуклеотидов в цепи ДНК

    Функция возвращает словарь, в котором указано количество
    каждого из нуклеотидов в данной цепи ДНК

    """
    dic = {}
    for nucl in seq.upper():
        if nucl in dic:
            dic[nucl] += 1 # nucl это ключ, 1 это value
        else:
            dic[nucl] = 1
    return dic

nucl_frequency_result = nucleotide_frequency(dna)
print(f'Нуклеотидный состав цепи ДНК: {nucl_frequency_result}')


#todo: Транскрипция

def transcription(seq):
    """
    Транскрипция ДНК в РНК

    Синтез мРНК идёт с антисенс-цепи (template strand).
    У нас задана кодирующая цепь (coding strand).

    Последовательность мРНК будет совпадать с последовательностью кодирующей цепи,
    за исключением того, что тимин(T) заменяется на урацил(U)

    """
    coding_RNA = seq.replace("T", "U")
    return(coding_RNA)

coding_RNA = transcription(DNA)
print(f'Кодирующая цепь: {DNA}')
print(f'Матричная РНК: {coding_RNA}')

# print(transcription.__doc__) # Это мы можем посмотреть, что записано в комменте про функцию!
# help(transcription) # Или так
# print(validating_sequence.__doc__)

'''
Reverse Complement of Coding Strand:

Take the coding strand (5' - ATGCCA - 3').
Find the complement: TACGGT (same as the template strand).
Reverse it to make it 5' to 3': 5' - TGGCAT - 3'.
'''

