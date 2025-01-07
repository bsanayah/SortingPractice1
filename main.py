from typing import List

def sort_colleges(words: List[str]) -> List[str]:
    words.sort() #sort in ascending order
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers

#class call sort gpa
#list of stuff is called gpa
#have this class return the gpa
def sort_gpa(gpa: List[float]) -> List[float]:
    gpa.sort()
    return gpa



# presets; don't change
print(sort_colleges(["UCF", "FIU", "USF", "UNF"]))

print(sort_numbers([22, 6, 7, 15, 4, 6, 30, 499, 8, 10]))

print(sort_gpa([3.45, 2.7, 3.5, 4.0, 4.0, 3.9, 3.1]))