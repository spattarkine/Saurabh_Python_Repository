'''Importing wordscore module to compute the score for the given scrabble'''
import wordscore 

def run_scrabble(rack):
    '''Scrabble function business logic. Initiate Variables'''
    rack_low = rack.lower()
    rack_letters = list(rack_low)
    clean_rack = []
    valid_words = []
    valid_rack = True
    if rack_low.count('?') >1  or rack_low.count('*') >1:
        #Check if program has more than one wildcard and return a string error message.
        valid_rack = False
        return ("You have entered more than 2 special characters")

    elif len(rack_low) > 7 or len(rack_low) < 2:
        #Check if length of word if less than two or greater than seven and return a string error message.
        valid_rack = False
        return ("You have entered more than 7 characters or less than 2")
    elif all(x.isalpha() == False or x not in ('?', '*') for x in rack_low):
        #Check if only one of the wildcard is used ? or * and return error and ask user to enter allowed values only. 
        valid_rack = False
        return ('Please enter only alphabets and/or special characters * and ?')
    else:
        #All validations went well.
        valid_rack = True
        
    if valid_rack:
        #If all validations are passed program will execute further.
        #Read file sowpods.txt and check each word in lower case in a loop. This will act like a base or a dictionary.
        #Remove duplicate word for temp_rack_letters once it has occurred to avoid duplication.
        with open("sowpods.txt","r", encoding="utf-8") as infile:
            raw_input = infile.readlines()
            data = [datum.strip('\n') for datum in raw_input]
        for word in data:
            #For each word in lower case from file below logic should check the rack.
            word_low = word.lower()
            temp_rack_letters = rack_letters.copy() # Keeping original copy intact.
            for letter in word_low:
                #For each letter in word remove letter once encountered.
                if letter in temp_rack_letters :
                    temp_rack_letters .remove(letter)
                elif '*' in temp_rack_letters :
                    temp_rack_letters .remove('*')
                elif '?' in temp_rack_letters :
                    temp_rack_letters .remove('?')
                else:
                    break 
            else:
                clean_rack = ''.join([i for i in rack_low if i.isalpha()]) #Removes the extra special characters (if any) and we have a clean rack now.
                valid_words.append((wordscore.score_word(clean_rack), word_low.upper())) #Clean rack is passed to calculate wors score.
                sorted_scores = sorted(valid_words, key=lambda x: (-x[0], x[1]), reverse=True) #Sorting logic plus conversion to tuple.
        return sorted_scores[::-1],len(sorted_scores) #Return final result and its length
