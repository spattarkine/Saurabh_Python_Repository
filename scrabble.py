"Import Wordscore module"
import wordscore

def run_scrabble(rack):
    "Run Scrapable Function Definision"    
    rack_low = rack.lower()
    rack_letters = list(rack_low)
    valid_words = []

    with open("sowpods.txt","r" , encoding="utf-8") as infile:
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
            valid_words.append([wordscore.score_word(word_low), word_low])
            valid_words.sort(reverse = True)

    for entry in valid_words:
        score = entry[0]
        word_low = entry[1]
        print((score, word_low))

    print("Total number of words:", len(valid_words))
    