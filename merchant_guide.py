import sys

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

global_script_verbosity = 0

def smart_print(string_to_print, string_verbosity_level):
    if (string_verbosity_level <= global_script_verbosity):
        output_fh = open("merchant_guide_output.txt",'a')
        output_fh.write(string_to_print)
        output_fh.write("\n\r")
        output_fh.close()
        print (string_to_print)


def decode_the_roman_numeral_string(roman_numeral_string):
    maintained_total = 0
    preceding_is_part_of_num = False

    the_full_string_length = len(roman_numeral_string)
    smart_print(("String Length = "+str(the_full_string_length)),1)
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
        smart_print (current_value,1)
    smart_print("================",1)
    smart_print(maintained_total,1)
    return maintained_total


def read_the_file(the_file):
    fh = open(the_file, 'r')
    for line in fh:
        # prepare the line the parsing
        processed_line = line.strip()
        the_words = processed_line.split()
        #-----------------------------------------------------------------------------------------------------------
        # this is a comment
        #-----------------------------------------------------------------------------------------------------------
        if the_words[0].startswith("#"):
            continue        
        #-----------------------------------------------------------------------------------------------------------
        # if the sentence has 3 words and ends with a roman numeral - its a mapping to roman numerals
        #-----------------------------------------------------------------------------------------------------------
        if ((len(the_words) == 3) and (processed_line[len(processed_line)-1] in roman_numeral_dictionary.keys())):
            # This is the intergalactic to roman numeral mapping
            # so push to that dictionary
            intergalactic_to_roman[the_words[0]] = the_words[2]
            continue
        #-----------------------------------------------------------------------------------------------------------
        # if the sentence ends with "Credits" and has a number before it, starts with a intergalactic currency and 
        # has an "is" before the number - then this is a rate 
        #-----------------------------------------------------------------------------------------------------------
        if ((the_words[len(the_words)-1] == "Credits") and (the_words[len(the_words)-2].isnumeric())
            and (the_words[0] in intergalactic_to_roman.keys()) and (the_words[len(the_words)-3] == "is")):
            # This is a rate statement
            rate_amount = ""
            for each_word in the_words:
                if each_word in intergalactic_to_roman.keys():
                    rate_amount = rate_amount + intergalactic_to_roman[each_word]
            mineral_dust = the_words[len(the_words)-4]
            credits_per_piece[mineral_dust] = (int(the_words[len(the_words)-2])/decode_the_roman_numeral_string(rate_amount))
            continue
        #-----------------------------------------------------------------------------------------------------------
        # if the sentence starts with how many/much and ends with a question mark - its a question we need to answer
        #-----------------------------------------------------------------------------------------------------------
        if ((the_words[0].lower() == "how") and ((the_words[1].lower() == "many") or (the_words[1].lower() == "much"))
            and (the_words[len(the_words)-1].endswith('?'))):
            # This is a question that needs to be answered
            questions_to_answer.append(processed_line)
            continue
            
        smart_print("I'm sorry but \""+line+"\" doesn't make sense to me - if Marvin's in a good mood he could help!",0)
        

def are_any_of_these_in_those(these, those):
    for one_of_these in these:
        if (one_of_these in those):
            return True
    return False


def which_of_these_in_those(these, those):
    for one_of_these in these:
        if (one_of_these in those):
            return one_of_these
    return False


def process_the_questions():
    for question in questions_to_answer:
        # Is it a general question or is it a commodities based question
        the_words = question.replace('?','').split()
        intergalactic_sentence = ""
        roman_numeral_sentence = ""
        # Build up the intergalactic and roman numeral strings
        for item in the_words:
            if item in intergalactic_to_roman:
                intergalactic_sentence = intergalactic_sentence + item + " "
                roman_numeral_sentence = roman_numeral_sentence + intergalactic_to_roman[item]
        if (len(intergalactic_sentence) == 0):
            smart_print("I'm sorry but \""+question+"\" doesn't make sense to me!  Perhaps you should consult DEEP THOUGHT!",0)
            continue
        if (("Credits" in the_words) and (are_any_of_these_in_those(credits_per_piece.keys(),the_words))):
            smart_print((question+":"+"CQ"),1)            
            current_commodity = which_of_these_in_those(credits_per_piece.keys(),the_words)
            smart_print((intergalactic_sentence + current_commodity + " is " + str(decode_the_roman_numeral_string(roman_numeral_sentence)*credits_per_piece[current_commodity])),0)
        else:
            if (the_words[len(the_words)-1] in intergalactic_to_roman.keys()):
                smart_print((question+":"+"NQ"),1)            
                smart_print((intergalactic_sentence + " is " + str(decode_the_roman_numeral_string(roman_numeral_sentence))),0)
            else:
                smart_print("I'm sorry but I don't know this metal: "+the_words[len(the_words)-1],0)
            

if __name__ == "__main__":
    file_name = "" 
    if (len(sys.argv) == 1):
        smart_print("You need to specify an input file. Alternatively I could read you some Vogon poetry?",0) 
    else: 
        output_fh = open("merchant_guide_output.txt", 'w')
        output_fh.close()
        if (len(sys.argv) == 3):
            # we have passed in the test script and verbosity level
            file_name = sys.argv[2]
            global_script_verbosity = int(sys.argv[1])
        if (len(sys.argv) == 2):
            file_name = sys.argv[1]
            global_script_verbosity = 0
        smart_print ("Welcome to the Merchant's Guide To the Galaxy",0)

        read_the_file(file_name)
        process_the_questions()    

