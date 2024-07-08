def urlify(s, true_length):
    """
    Substitutes all spaces in a string with "%20".

    Args:
        s (str): The string to be modified.
        true_length (int): The actual length of the string (excluding trailing spaces).

    Returns:
        str: The modified string with spaces replaced by "%20".
    """

    new_string = ""  # Create an empty string to store the modified version
    for i in range(true_length):
        if s[i] == " ":
            new_string += "%20"
        else:
            new_string += s[i]
    return new_string

s = "Mr J o h n Smith       "
true_length = 1
modified_string = urlify(s, true_length)
print(modified_string)
