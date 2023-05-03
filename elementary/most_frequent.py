def most_frequent(data: list[str]) -> str:
    counts = 0
    for word in data:
        if data.count(word) > counts:
            counts = data.count(word)
            most_freq_word = word
    return most_freq_word


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
