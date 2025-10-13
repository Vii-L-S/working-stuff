sen = input('Type a sentence: ')
count = 0
for c in sen:
    if c == " ":
        count += 1
print(f'The amount of spaces you typed is: {count}')
words = sen.split()
wcount = len(words)
print (f'The amount of words you typed is: {wcount}')
