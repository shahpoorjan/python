inp = input("enter your words? ").split()
longest_word = inp[0]
for char in inp:
    if len(char) > len(longest_word):
        longest_word = char
print(longest_word)