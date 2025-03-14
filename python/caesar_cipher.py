def caesar_cipher(string, shift_amount):
    string_ascii_list = []
    a_char_code_lower = ord('a')
    prev_a_char_code = ord('a') - 1
    last_char_code_lower = ord('z')


    for n in string:
        new_char_code = ord(n.lower()) + shift_amount
        lower = True if n.islower() else False

        if n  == " " or not n.isalpha():
            string_ascii_list.append(n)
        elif shift_amount > 0:
                lower_char = n.lower()

                if new_char_code <= last_char_code_lower:
                    string_ascii_list.append(chr(new_char_code)) if lower else string_ascii_list.append((chr(new_char_code).upper()))
                    # string_ascii_list.append(chr(new_char_code))
                elif new_char_code > last_char_code_lower:
                    amount_over = new_char_code - last_char_code_lower
                    string_ascii_list.append(chr(prev_a_char_code + amount_over)) if lower else string_ascii_list.append((chr(prev_a_char_code + amount_over).upper()))
        elif shift_amount < 0:
            if new_char_code >= a_char_code_lower:
                string_ascii_list.append(chr(new_char_code)) if lower else string_ascii_list.append((chr(new_char_code)).upper())
            elif new_char_code < a_char_code_lower:
                amount_over = a_char_code_lower - new_char_code
                # print("a",a_char_code_lower, "new",new_char_code, "over", amount_over, last_char_code_lower - amount_over)
                string_ascii_list.append(chr(last_char_code_lower - amount_over + 1)) if lower else string_ascii_list.append((chr(last_char_code_lower - amount_over + 1).upper()))
            
    # print(''.join(string_ascii_list))
    return ''.join(string_ascii_list)


            
# 'a'	97	
# 'z'	122

# 'A'	65
# 'Z'	90

# " "   32