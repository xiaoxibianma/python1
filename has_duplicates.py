def has_duplicates(list1):
    count = dict()
    for word in list1:
        count[word] = count.get(word, 0) + 1
    return any(1 < n for n in count.values())
