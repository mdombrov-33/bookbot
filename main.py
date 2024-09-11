def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_occurence = count_book_string(book_text)
    report = convert_and_sort(num_occurence)
    # print(f"Number of words in the book: {num_words}")
    # print(f"Number of occurences of each character: {num_occurence}")
    for entry in report:
        char = entry['char']
        count = entry['count']
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path, "r") as book:
        return book.read()


def count_book_string(text):
    string_dictionary = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in string_dictionary:
                string_dictionary[char] += 1
            else:
                string_dictionary[char] = 1
    return string_dictionary


def convert_and_sort(dictionary):
    # Convert dictionary to list of dictionaries
    list_of_dicts = [{"char": k, "count": v} for k, v in dictionary.items()]
    # Sort the list by the count value
    list_of_dicts.sort(key=lambda x: x["count"], reverse=True)
    return list_of_dicts


if __name__ == '__main__':
    main()
