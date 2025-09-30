def count_words(text):
    count = 0
    for _ in text.split():
        count += 1
    print(f"Found {count} total words")  

def count_characters(text):
    character_counts = {}
    for character in text.lower():
        if character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    return character_counts

def sorted_list(dictionary):
    list_dict = []
    for char in dictionary:
        if char.isalpha():
            char_dict = {}
            char_dict["char"] = char
            char_dict["num"] = dictionary[char]
            list_dict.append(char_dict)
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def sort_on(dict):
    return dict["num"]
        