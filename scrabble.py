'''Importing wordscore module to compute the score for the given scrabble'''
import wordscore

def run_scrabble(rack):
    "Scrabble function business logic"
    rack_low = rack.lower()
    rack_letters = list(rack_low)
    valid_words = []
    result=[]
    result_tuple = ()
    valid_rack = True
    if (rack_low.count('?') > 1 or  rack_low.count('*')) > 1:
        #If program has more than one wildcard.
        valid_rack = False
        return False
        #return ("You have entered more than 2 special characters")

    elif len(rack_low) > 7 or len(rack_low) < 2:
        #If length of word if less than two or greater than seven.
        valid_rack = False
        return False
        #return ("You have entered more than 7 characters or less than 2")
    elif all(x.isalpha() or x in ('?', '*') for x in rack_low):
        valid_rack = True
    else:
        valid_rack = False
        return False
        #return ('Please enter only alphabets and/or special characters * and ?')
    if valid_rack:
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
                valid_words.append([wordscore.score_word(word_low), word_low.upper()])
                valid_words.sort(reverse = True)
        for counter in valid_words:
            score = counter[0]
            word_low = counter[1]
            result_tuple += (score, word_low)
            result.append(result_tuple)
        return result
