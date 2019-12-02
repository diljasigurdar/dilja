file_object = str(input("Enter a string: "))

punctations = ""'!()-[]{\};:'",<>./?@#$%^&*_~''"
word_without_punctation = ""
for word in file_object:
    if word not in punctations:
        word_without_punctation += word

word_without_punctation = word_without_punctation[-1:]

print(word_without_punctation)
