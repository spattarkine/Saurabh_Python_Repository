"Importing wordscore module"
import wordscore

def run_scrabble(rack):
    "Scrabble function business logic"
    rack_low = rack.lower()
    rack_letters = list(rack_low)
    valid_words = []
    valid_rack = True
    clean_rack = []
    if (rack_low.count('?') > 1 or  rack_low.count('*')) > 1:
        valid_rack = False
        return ("You have entered more than 2 special characters")

    elif len(rack_low) > 7 or len(rack_low) < 2:
        valid_rack = False
        return ("You have entered more than 7 characters or less than 2")
    elif all(x.isalpha() or x in ('?', '*') for x in rack_low):
        valid_rack = True
    else:
        valid_rack = False
        return ('Please enter only alphabets and/or special characters * and ?')
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
                clean_rack = ''.join([i for i in rack_low if i.isalpha()])
                valid_words.append([wordscore.score_word(clean_rack), word_low.upper()])
                valid_words.sort(reverse = True) #Descending Order
        for entry in valid_words:
            score = entry[0]
            word = entry[1]
            print(str(score) + " " + word)
        return word
    else:
        valid_rack = False
