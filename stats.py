def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def characters(text):
    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] =  1
    return char_count

def sort_on(d):
    return d["count"]

def sort_characters(char_count):
    sorted_chars = []

    for char, count in char_count.items():
        if char.isalpha():
            sorted_chars.append({
                "char": char,
                "count": count
            })
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars


    

