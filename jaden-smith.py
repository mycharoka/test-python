
# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
# import string
def to_jaden_case(string):
    # 1. harus hilangin spasi (jika ada)
    # 2. 
    # if string.isspace() == True:
    #     capital = string.title()
    #     return capital
    # else:
    #     capitalize = string.capitalize()
    #     return capitalize
    
    
    # 1st solution
    # return ' '.join(w[:1].upper() + w[1:] for w in string.split(' ')) 

    # 2nd solution
    # import string <= gotta do this first
    # return string.capwords(jaden_string)
    string_list = []
    container = string.split()

    for iteration in container:
        each_letter = list(iteration)
        each_letter[0] = each_letter[0].upper()
        string_list.append(''.join(each_letter))
    
    return ' '.join(string_list)

sentence = 'oneletteronly'
sentence = 'space that you need'
space_checker = sentence.isspace()
print(to_jaden_case(sentence))
print('space checker: ' + str(space_checker))
