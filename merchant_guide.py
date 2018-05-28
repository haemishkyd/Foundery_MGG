roman_numeral_dictionary = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

intergalactic_to_roman = {
    "dummy_value":"Z"
}

credits_per_piece = {
    "Silver":0,
    "Iron":0,
    "Gold":0
}

questions_to_answer = []


def decode_the_roman_numeral_string(roman_numeral_string):
    maintained_total = 0
    preceding_is_part_of_num = False

    the_full_string_length = len(roman_numeral_string)
    print ("String Length = "+str(the_full_string_length))
    for rn_idx in reversed(range(0, the_full_string_length)):
        if (preceding_is_part_of_num):
            preceding_is_part_of_num = False
            continue
        current_value = 0        
        if (rn_idx >= 1):
            if (roman_numeral_dictionary[roman_numeral_string[rn_idx-1]] < roman_numeral_dictionary[roman_numeral_string[rn_idx]]):
                current_value = roman_numeral_dictionary[roman_numeral_string[rn_idx]
                                                        ] - roman_numeral_dictionary[roman_numeral_string[rn_idx-1]]
                preceding_is_part_of_num = True
            else:
                current_value = roman_numeral_dictionary[roman_numeral_string[rn_idx]]
        else:
            current_value = roman_numeral_dictionary[roman_numeral_string[rn_idx]]
        maintained_total = maintained_total + current_value
        print (current_value)
    print("================")
    print (maintained_total)
    return maintained_total


def read_the_file(the_file):
    fh = open(the_file, 'r')
    for line in fh:
        # prepare the line the parsing
        processed_line = line.strip()
        the_words = processed_line.split()        
        # check which part of the file this is
        if ((len(the_words) == 3) and (processed_line[len(processed_line)-1] in roman_numeral_dictionary.keys())):
            # This is the intergalactic to roman numeral mapping
            # so push to that dictionary
            intergalactic_to_roman[the_words[0]] = the_words[2]
        if ((the_words[0].lower() == "how") and (the_words[len(the_words)-1].endswith('?'))):
            # This is a question that needs to be answered
            questions_to_answer.append(processed_line)


def process_the_questions():
    for question in questions_to_answer:
        # check if this has any mention of the commodities
        for key in credits_per_piece.keys():
            elements_of_sentence = question.replace('?','').split()
            if key not in elements_of_sentence:
                # This is a basic question 
                roman_numeral_sentence = ""
                for item in elements_of_sentence:
                    if item in intergalactic_to_roman:
                        roman_numeral_sentence= roman_numeral_sentence + intergalactic_to_roman[item]
                print(decode_the_roman_numeral_string(roman_numeral_sentence))
                break

if __name__ == "__main__":    
    print ("Welcome to the Merchant's Guid To the Galaxy")
    read_the_file("test1.txt")
    print(questions_to_answer)
    process_the_questions()
    #decode_the_roman_numeral_string("XCVIII")

