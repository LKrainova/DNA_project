
dna = 'ctaatgagccatgctgatcgatgtccgttgcgagttttcgataacttaaaagcacgcggatacgtatttaggaaaaaacttatgtgagactcacctgagactaagtcgtgtggacctcaataagtcctttctaaggtatcacatcgaaacgcatagtgttgaaatccttttttcatgtaaattcaattgattctcgaaatctgcacaagtcgctgacaaactttaccttatcctagaagaggtacgcccacctgtccaggcgctgttgtcatgcaagtacattagcactacggagcggaataatcactccgatacgagacgtatatagacaggcgccgtcggtagagctagtgacgggcagctaccgtctctaataggagataactggctctcagacgacagccgcagccctacctgggttccaaccgtttacattaaactggcctacatggtgacgcctccagcaacataaccacaagtgtgttgttaggaagtagagtgtgctggaaccatcctcattggaaccttactgcgactgccggagttccaccatcgtgaagggccgagaataggtaacgtaaacgggacgcattgtctgaaaatgagtctccgagaagaaaagatcatttccattatagatgagttgcgacggaagtaacgtgtgtcaatgctagtcctggtagatggcgacaagcac'
#nucleotides = ["A", "T", "G", "C"]

# todo: Проверить, является ли приведённая последовательность ДНК (что нет лишних элементов)

def validating_sequence(seq):
    nucleotides = ["A", "T", "G", "C"]
    garbage_dict = {}
    for index, nucl in enumerate(seq.upper()):
        if nucl in nucleotides:
            pass
        elif nucl not in nucleotides:
            garbage_dict[nucl] = index
            print(f"Обнаружен лишний элемент {nucl} на позиции {index}!")

    if garbage_dict == {}:
        print("Данная последовательность является ДНК")

    return garbage_dict

validation_result = validating_sequence(dna)
print(validation_result)


#todo: Очистка последовательности в случае, если были обнаружены лишние элементы
# Наверно,не нужно это делать, п.ч. это м.б. непрочтённый нуклеотид N и лучше сохранить
# его позицию


#todo: Подсчёт количества каждого из нуклеотидов в цепи ДНК

def nucleotide_frequency(seq):
    dic = {}
    for nucl in seq.upper():
        if nucl in dic:
            dic[nucl] += 1 # nucl это ключ, 1 это value
        else:
            dic[nucl] = 1
    return dic

nucl_frequency_result = nucleotide_frequency(dna)
print(nucl_frequency_result)

