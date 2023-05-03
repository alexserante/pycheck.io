def most_frequent(data: list[str]) -> str:
    counts = 0
    for word in data:
        if data.count(word) > counts:
            counts = data.count(word)
            most_freq_word = word
    return most_freq_word


list1 = ["a", "b", "c", "a", "b", "a"]
list2 = ["a", "a", "bi", "bi", "bi"]

'''counts = 0
for word in list2:
    if list2.count(word) > counts:
        print(list2.count(word))
        counts = list2.count(word)
        most_freq_word = word'''

print(max(list2, key=list2.sort))

#print(most_freq_word)
