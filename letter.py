def letter_grade(mark:int) -> str:
    '''

Returns the letter grade for given grade mark.
Marks:
A = 80 - 100
B = 70 - 79
C = 60 - 69
D = 50 - 59
F = below 50
'''
    if mark < 0 or mark > 100:
        return "Enter a valid value between 0 and 100."
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else: 
        return "F"
print(letter_grade(55))