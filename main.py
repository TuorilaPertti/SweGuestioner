import os
import msvcrt
import csv
import random
from colorama import Fore,Back,Style,init
from spellcheck import checkSpelling

#Colorama colors: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET

def debug(*args):
    try:
        print(*args)
    except SyntaxError:
        print(Back.RED+'Error occured while debugging')

init(autoreset=True)

clear = lambda: os.system('cls')
paktc = lambda: os.system('pause') #Press Any Key To Continue


#def 

def loadDictionary(dic_name=False):
    name_dictionary = dic_name
    dick = {}
    with open(name_dictionary, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                dick[row[0]] = row[1:]
                line_count += 1
        print(f'Processed {line_count} lines.')
    if len(dick) == 0:
        raise Exception('Incorrect dictionary file, no valid translations')
    else:
        return dick

def showDicKeys():
    clear()
    dictionary = loadDictionary()
    max_len = len(max([*dictionary], key=len))
    print('Visat nycklarna med längd:')
    for word in dictionary:
        print(f'{word:20} :{len(word)} karaktärar')
    print(f'Max dick key: {max_len}')
    paktc()
    
def showResults(dictionary, results):
    form_len = len(max([*dictionary], key=len))+3
    #debug(f"DEBUG: {form_len}")
    print(Fore.MAGENTA+'\tSLUTRESULTATET')
    '''
    for index,word in enumerate(dictionary):
        if results[index] is True:
            print(Fore.CYAN+f'{word:{form_len}}'+Fore.GREEN+f'{dictionary[word]}')
        else:
            print(Fore.CYAN+f'{word:{form_len}}'+Fore.RED+f'{dictionary[word]}')
    '''
    for word in results:
        if results[word] is True:
            print(Fore.CYAN+f'{word:{form_len}}'+Fore.GREEN+f'{dictionary[word]}')
        else:
            print(Fore.CYAN+f'{word:{form_len}}'+Fore.RED+f'{dictionary[word]}')


    
def askWords(dic_name=False):
    clear()
    try:
        dictionary = loadDictionary(dic_name)
    except Exception as e:
        print(e)
        paktc()
        return False
    words = len(dictionary)
    num_to_ask = min(words,10)
    right_quesses = []
    quesses = {}
    insults = ["Hoppsan! Det här är inte rätt.",\
               "Du dum!",\
               "Försökte du?",\
               "Jag ska göra du om till en man!"]
    ''' '''
    for i in range(num_to_ask):
        #debug(f'Done quesses: {quesses}')
        while (True):
            x = random.choice( [*dictionary] )
            #debug(f' random: {x}')
            if x not in [*quesses]:
                break
            
        
        quess = input('Vad menar '+Fore.CYAN+f'{x}'+Fore.RESET+'?\n')
        quess_arr  = [word.rstrip().lstrip() for word in quess.split(',')]
        all_right = False
        if len(quess_arr) > 1 and quess_arr == dictionary[x]:
            quesses[x] = True
            all_right = True
        elif quess in dictionary[x]:
            quesses[x] = True
        else:
            quesses[x] = False
            print(random.choice(insults))
        if not all_right:
            print(f'{dictionary[x]}')
        else:
            print(Fore.YELLOW+'* '+Fore.GREEN+'FABULÖS!'+Fore.YELLOW+' *')

    num_right = [*quesses.values()].count(True)
    if num_right/num_to_ask <= 0.5:
        print(Fore.RED+f'Got right answers: {num_right}/{num_to_ask}')
    elif num_right/num_to_ask < 0.8:
        print(Fore.YELLOW+f'Got right answers: {num_right}/{num_to_ask}')
    else:
        print(Fore.GREEN+f'Got right answers: {num_right}/{num_to_ask}')

    paktc()
    showResults(dictionary, quesses)
    paktc()

def printMenu():
    clear()
    dic_files = []
    for root,folders,files in os.walk(os.getcwd()):
        for file in files:
            if '.txt' in file:
                dic_files.append(file)


    command = False
    selected = int(0)

    while (command is not chr(27).encode()):
        if int(selected) < int(0) or int(selected) >= len(dic_files):
            selected = 0
        print('Välj en ordbuk som du vill.\n'\
                'Tryck på ESC för att sluta')
        for i,filename in enumerate(dic_files):
            if selected == i:
                print(f'{i+1}.[x] {filename}')
            else:
                print(f'{i+1}.[ ] {filename}')

        command = msvcrt.getch()
        if command == b'\r':
            askWords(dic_files[selected])
        elif command.decode().isnumeric():
            selected = int(command.decode())-1
        clear()
        #debug(f'files: {dic_files} selected file: {dic_files[selected]}')
        #debug(f'selected: {selected}')
          

def printGreet():
    print('Välkomnen till Fråga Olle! \nJag ska lära dig')    

def main():
    printGreet()
    paktc()
    printMenu()
    print('Exiting program...')


main()
