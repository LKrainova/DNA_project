from OOP_FastaReader import FastaReader
from OOP_BasicOperations import BasicOperations

'''Считываем нуклеотидную последовательность из FASTA-файла'''

# Примеры Accession numbers:
# PP694298.1 - горноазиатский сурок Marmota baibacina, фрагмент рРНК большой рибосомальной субъединицы

'''dna - это переменная, в которую записывается нуклеотидная последовательность из файла'''

accession_number = input("Введите accession number: \n")
instance_FastaReader = FastaReader(accession_number)
dna = instance_FastaReader.read_file()


'''
dna_instance - это объект класса BasicOperation, 
для которого мы будем вызывать имеющиеся в классе методы.
В него передаём переменную dna.
'''

dna_instance = BasicOperations(dna)


'''Проверяем последовательность на наличие ненуклеотидных элементов'''

validation_result = dna_instance.validate_sequence()
print(validation_result)


'''Считаем количественное содержание нуклеотидов в последовательности'''

nucleotide_content = dna_instance.count_nucleotides()
print(f"Количественное содержание нуклеотидов в последовательности: {nucleotide_content}")


'''Получаем матричную РНК для заданной последовательности'''

coding_RNA = dna_instance.transcribe_to_RNA()
print(f"Матричная РНК для данной последовательности: {coding_RNA}")



