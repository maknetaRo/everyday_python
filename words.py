def format_words(words):
    if words == None:
        return ""
    else:
        sentence = [word for word in words if word != ""]
        if len(sentence)  < 1:
            return ""
        elif len(sentence) == 1:
            return sentence[0]
        return ', '.join(sentence[:-1]) + " and " + sentence[-1]

print(format_words(['ninja', 'samurai', 'ronin']))
print(format_words(['ninja', '', 'ronin']))
print(format_words([]))
print(format_words(['ninja', 'samurai', 'ronin', 'me']))
print(format_words(['ninja']))
print(format_words(None))
