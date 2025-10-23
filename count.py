li=input("enter a line of code: ")
words=li.split()
count={}
for word in words:
    if word in count:
        count[word] +=1
    else:
        count[word] = 1
for word, freq in count.items():
    print(f"{word}: {freq}")

