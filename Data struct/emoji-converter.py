message = input(">")
words = message.split(' ')
emojis = {
    ":)": " smiley face",
    ":(": "Sad Face"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
