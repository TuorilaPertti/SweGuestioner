def isVowel(character):
    vowels = 'eyuioåaöä'
    if character in vowels:
        return True
    else:
        return False

def isConsonant(character):
    if character.isalpha() and not isVowel(character):
        return True
    else:
        return False


def checkSpelling(answer,quess):
    ''' Returns: error percentage (errors/len_answer)'''

    num_errors = 0
    fatal_error = False
    len_answer = len(answer)
    len_quess  = len(quess)
    print(f'DEBUG: len_quess = {len_quess}')
    mixed_letters = (   'mn',\
                        'jl',\
                        'åoöä',\
                        'vf')

    prev_letter = ''
    offset = 0
    for i,c in enumerate(answer):
        print(f'DEBUG: i =  {i}, offset = {offset}')
        if not (i+offset < len_quess):
            break
        
        #print(f'DEBUG: answer[{i}]={c}\n'\
        #      f'       quess[{i}]={quess[i]} offset={offset}')

        
        if (quess[i+offset] == c):
            prev_letter = c
            continue
        elif prev_letter == quess[i+offset]:
            num_errors +=1
            offset +=1
        elif prev_letter == c:
            num_errors +=1
            offset -=1
        else:
            fatal_error = True
            for mixable in mixed_letters:
                if (c in mixable) and (quess[i+offset] in mixable):
                    num_errors +=1
                    fatal_error = False

    if fatal_error:
        return 1.0
    else:
        return(num_errors/len_answer)
