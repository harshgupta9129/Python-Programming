letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter Name : ")

date = input("Enter Date : ")

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)

print(letter)