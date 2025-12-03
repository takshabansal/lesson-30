def reverse_words(text):
    return " ".join(text.split()[::-1])
sentence = "I love Python programming"
result = reverse_words(sentence)
print(result)