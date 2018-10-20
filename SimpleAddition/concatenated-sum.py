def concatenated_sum(a, b):
    word = ""
    for x in range(a):
        word = word + "A"
    for y in range(b):
        word = word + "B"
    return len(word)

print(concatenated_sum(9, 4))

