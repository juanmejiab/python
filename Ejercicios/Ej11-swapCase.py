def swap_case(sentence):
    sentence_converted = ""
    for x in sentence:
        if x.isupper():
            sentence_converted += x.lower()
        else:
            sentence_converted += x.upper()
    return sentence_converted


result = "Mi Nombre es jUaN PabLo"
print(swap_case(result))
