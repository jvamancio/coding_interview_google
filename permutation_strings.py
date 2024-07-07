def sort_strings(string):
    return "".join(sorted(string))

def permutation_two_strings(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    return sort_strings(string_one) == sort_strings(string_two)

string_one = "god"
string_two = "dog"

print(permutation_two_strings(string_one, string_two))