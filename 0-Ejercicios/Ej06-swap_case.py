def swap_case(sentence):
    sentence_converted = ""
    for x in sentence:
        if x.isupper():
            sentence_converted += x.lower()
        else:
            sentence_converted += x.upper()
    return sentence_converted


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
