user_text = input()

chars_to_remove =' .,!'
char_count = 0
for character in user_text:
    if character not in chars_to_remove:
        char_count+=1
        
print(char_count)
