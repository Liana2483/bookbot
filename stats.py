def count_words(text):
    return len(text.split())

def char_amount_in_text(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict  


def sort_dic_and_counts(char_dict):
    char_list = []
    for ch, n in char_dict.items():
            char_list.append({"char": ch, "num": n})

    def sort_on(d):
        return d["num"]

    char_list.sort(key=sort_on, reverse=True)       
    return char_list
