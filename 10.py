import string
def check_pangram(str):
    alphabet = set(string.ascii_lowercase)
    valid = set(str.lower().replace(" ",""))
    if sorted(valid) == sorted(alphabet):
        return True
    return False
print(check_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))