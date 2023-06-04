sentence = "This is a common interview question"

dictionary = {x: sentence.count(x) for x in sentence}

character_count = list(zip([x for x in dictionary], [
                       x for x in dictionary.values()]))
character_count.sort(key=lambda item: item[1], reverse=True)

most_common_character = []
for x in range(len(character_count)-1):
    if character_count[x][1] == character_count[x+1][1]:
        most_common_character.append(character_count[x][0])
    else:
        # revisar
        most_common_character.append(character_count[x][0])
        break

print(most_common_character)
