text=input("enter a string:")

print("*"*10+"Indexing and Slicing"+"*"*10)

print("first character :",text[0])

print("last character:",text[-1])

print("first 3 characters:",text[0:3])

print("from 3 onwards:",text[3:5])

print("reverse of text:",text[: : -1])

print("every third character:",text[: : 3])

print("*"*10+"case conversion"+"*"*10)

print("uppercase:",text.upper())

print("lowercase:",text.lower())

print("swapcase:",text.swapcase())

print("*"*10+"count occurrences"+"*"*10)

sub=input("enter a character or substring:")

print("'"+sub+"'occurs",text.count(sub),"time(s)")

print("*"*10+"replace a word"+"*"*10)

old=input("enter the word to replace:")

new=input("enter the new word:")

print("after replacing:",text.replace(old,new))

print("*"*10+"split and join"+"*"*10)

words=text.split()

print("after split:",words)

print("after join:","-".join(words))

print("*"*10+"starts with ends with"+"*"*10)

start=input("enter the substring to check at the start:")

end=input("enter the substring to check at end:")

print("starts with"+start+"':",text.startswith(start))

print("ends with"+end+"':",text.endswith(end))




