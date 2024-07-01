def decode_string(s: str) -> str:
    stack = []
    current_num = 0
    current_string = ''
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push the current number and string onto the stack
            stack.append((current_string, current_num))
            current_string = ''
            current_num = 0
        elif char == ']':
            # Pop the stack and get the last string and number
            last_string, num = stack.pop()
            current_string = last_string + current_string * num
        else:
            current_string += char
            
    return current_string

# Exemplo de uso
encoded_string = "3[a2[c]]"
decoded_string = decode_string(encoded_string)
print(decoded_string)  # Saída: "accaccacc"
