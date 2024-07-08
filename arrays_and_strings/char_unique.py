def has_unique_characters(str):
    if len(str)>128:
        return False
    else:
        char_set = set()
        for char in str:
            if char in char_set:
                return False
            char_set.add(char)
        return True

string1 = "abcdefghijklmnopqrstuvwxyz"
string2 = "hello"
string3 = "abcabc"

print(has_unique_characters(string1))  # True
print(has_unique_characters(string2))  # False
print(has_unique_characters(string3))  # False