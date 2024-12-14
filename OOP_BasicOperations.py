
class BasicOperations:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.nucleotides = ["A", "T", "G", "C"]
        self.garbage_dict = {}
        self.mRNA = ""

    def validate_sequence(self):
        for index, nucl in enumerate(self.sequence):
            if nucl in self.nucleotides:
                pass
            elif nucl not in self.nucleotides:
                self.garbage_dict[nucl] = index
                print(f"Обнаружен ненуклеотидный элемент {nucl} на позиции {index}!")

        if self.garbage_dict == {}:
            print("Данная последовательность является ДНК")

        return self.garbage_dict


    def count_nucleotides(self):
        self.count_dict = {}
        for nucl in self.sequence:
            if nucl in self.count_dict:
                self.count_dict[nucl] += 1
            else:
                self.count_dict[nucl] = 1
        return self.count_dict


    def transcribe_to_RNA(self):
        self.mRNA = self.sequence.replace("T", "U")
        return(self.mRNA)






