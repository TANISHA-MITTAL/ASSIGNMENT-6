list=[n for n in input("Enter the words with sapce as hyphen").split('-')]
list.sort()
print('-'.join(list))