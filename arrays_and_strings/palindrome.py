def is_palindrome(str):

    word = str.lower()
    beginning_str = 0
    end_str = len(word) - 1 # conts started in 0

    for i in range(len(word)//2):
        if word[beginning_str] != word[end_str]:
            return False
        beginning_str += 1
        end_str -= 1
    return True

word = "Osso"
word_is_palindrome = is_palindrome(word)
print("A palavra",word, "é um palindrome?", word_is_palindrome)
