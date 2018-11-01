# 9-1.txt
def longest_word(my_list):
    for word in my_list:
        is_longest = True
        for other_word in my_list:
            if len(word) < len(other_word):
                is_longest = False
                break
        if is_longest:
            return word

if __name__ == '__main__':
    print(longest_word(['A', 'AB', 'ABC', 'A']))
