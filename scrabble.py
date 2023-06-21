'''Importing wordscore module to compute the score for the given scrabble'''
import wordscore 

def run_scrabble(rack):
    '''Scrabble function business logic. Initiate Variables'''
    rack_low = rack.lower()
    rack_letters = list(rack_low)
    clean_rack = []
    valid_words = []
    sorted_scores = [] 
    valid_rack = True
    if rack_low.count('?') >1  or rack_low.count('*') >1:
        #Check if program has more than one wildcard and return a string error message.
        valid_rack = False
        return ("You have entered more than 2 special characters")

    elif len(rack_low) > 7 or len(rack_low) < 2:
        #Check if length of word if less than two or greater than seven and return a string error message.
        valid_rack = False
        return ("You have entered more than 7 characters or less than 2")
    elif all(x.isalpha() or x in ('?', '*') for x in rack_low):
        #Check if only one of the wildcard is used ? or * and return true for further processing. 
        valid_rack = True
    else:
        #All other categories to return generic error and ask user to enter allowed values only.
        valid_rack = False
        return ('Please enter only alphabets and/or special characters * and ?')
    if valid_rack:
        #If all validations are passed program will execute further.
        #Read file sowpods.txt and check each word in lower case in a loop.
        #Remove duplicate word for temp_rack_letters once it has occurred to avoid duplication.
        with open("sowpods.txt","r", encoding="utf-8") as infile:
            raw_input = infile.readlines()
            data = [datum.strip('\n') for datum in raw_input]
        for word in data:
            word_low = word.lower()
            temp_rack_letters = rack_letters.copy()
            for letter in word_low:
                if letter in temp_rack_letters :
                    temp_rack_letters .remove(letter)
                elif '*' in temp_rack_letters :
                    temp_rack_letters .remove('*')
                elif '?' in temp_rack_letters :
                    temp_rack_letters .remove('?')
                else:
                    break 
            else:
                clean_rack = ''.join([i for i in temp_rack_letters if i.isalpha()])
                # removes the special characters from the rack 
                valid_words.append((wordscore.score_word(clean_rack), word_low.upper()))
                sorted_scores = sorted(valid_words, key=lambda x: (-x[0], x[1]), reverse=True)
        return sorted_scorest,len(sorted_scores)
