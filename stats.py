def get_file_content(filepath):
    content = ""
    with open(filepath) as f:
        content = f.read()
    return content

def get_num_words(filepath):
    content = get_file_content(filepath=filepath)
    return len(content.split())

def get_characters_count_dict(filepath):
    file_content = get_file_content(filepath)
    char_count_dict = {}
    for c in file_content:
        if c.isalpha():
            c = c.lower()
            if c not in char_count_dict:
                char_count_dict[c] = 0
            char_count_dict[c] += 1
    char_count_dict = order_char_count_by_value(char_count_dict)
    return char_count_dict

def order_char_count_by_value(char_count_dict):
    char_count_tuple = char_count_dict.items()
    sorted_tuple = sorted(char_count_tuple, key=lambda char_count: char_count[1], reverse=True)
    return dict(sorted_tuple)
    
