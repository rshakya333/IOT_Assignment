'''Write a function find_longest_word() that takes a list of words and returns the length of the longest
one.'''

def find_longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)

word_list = ["apple", "banana", "kiwi", "grapefruit"]  
longest_length = find_longest_word(word_list) 
print(f"The length of the longest word is {longest_length}")

