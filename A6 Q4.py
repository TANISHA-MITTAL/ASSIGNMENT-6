Check = 'the quick brown fox jumps over the lazy dog'
def pangram_check(str):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for c in abc:
        if c not in str.lower():
            return False
        else:
            return True
if(pangram_check(Check) == True):
    print("this is a pangram")
    print(Check)
else:
    print("this is not a pangram")
    print(Check)
