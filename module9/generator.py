def all_variants(text):
    length = len(text)
    for i in range(1, length + 1):
        for j in range(length - i + 1):
            yield text[j:j+i]


a = all_variants("abc")
for i in a:
    print(i)
