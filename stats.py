
def book_word_count(book):
    words = book.split()
    return len(words)

def book_letter_count(book):
    book = book.lower()
    letter_count= {}
    for b in book:
        if b not in letter_count:
            letter_count[b] = 1
        else:
            letter_count[b] +=1

    return letter_count


def sort_on(items):
    return items["num"]

def letter_count_sort(items):
    letters = []
    for i in items:
        letters.append({"char":i, "num": items[i]})
    letters.sort(reverse=True, key=sort_on)
    return letters
