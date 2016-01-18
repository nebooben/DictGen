#!/usr/bin/env python
# -*- coding: utf-8 -*-


def word_extractor(input_list, position, separator):
    output_list = []
    for i in range(0, len(input_list)):
        output_list.append(input_list[i].split(separator)[position])
    return output_list

########################################################################################################################


def join_logins_and_passwords(logins_list, passwords_list, separator):
    output_list = []
    for i in range(min(len(logins_list), len(passwords_list))):
        output_list.append(str(logins_list[i] + separator + passwords_list[i]))
    return output_list
########################################################################################################################


def file_to_list(filename):
    output_list = []
    with open(filename) as input_file:
        for line in input_file:
            output_list.append(line.strip())
    return output_list


def list_to_file(input_list, filename):
    with open(filename + ".txt", "w") as input_file:
        for i in xrange(0, len(input_list)):
            input_file.write(str(input_list[i]) + "\n")
    input_file.close()
    # return 0

########################################################################################################################


def mix_logins_and_passwords(logins_list, passwords_list, separator):
    return [x + separator + y for x in logins_list for y in passwords_list]

########################################################################################################################
########################################################################################################################


def all_combinations(string):
    from itertools import combinations
    output_list = []
    for i in range(1, len(string) + 1):
        output_list.append(combinations(string, i))
    return output_list


def get_indexes(input_string, chars):
    indexes_output = []
    input_string = list(input_string.lower())
    for ittr1 in range(len(input_string)):
        for ittr2 in range(len(chars)):
            if input_string[ittr1] == chars[ittr2]:
                indexes_output.append(str(ittr1))
    return indexes_output


def change(string, input_list, chars, replacement):
    string = list(string.lower())
    for ittr in range(len(string)):
        for ittr1 in range(len(input_list)):
            if ittr == int(input_list[ittr1]):
                for ittr2 in range(len(chars)):
                    if string[ittr] == chars[ittr2]:
                        string[ittr] = replacement[ittr2]
    return "".join(string)


def leet_word(input_word):
    # EXPAND
    first_round_a = "abeiostdg"
    first_round_n = "483105796"

    output_list = []
    combinations = all_combinations(get_indexes(input_word, first_round_a))
    for elements in combinations:
        for element in elements:
            output_list.append(change(input_word, element, first_round_a, first_round_n))

    second_round_a = "asithxce"
    second_round_n = "@$!+#%(&"
    combinations = all_combinations(get_indexes(input_word, second_round_a))
    for elements in combinations:
        for element in elements:
            output_list.append(change(input_word, element, second_round_a, second_round_n))
    return output_list


def leet(input_list):
    output_list = []
    for element in input_list:
        output_list.append(str(element))
        output_list += leet_word(str(element))
    return output_list

########################################################################################################################


def chars_combination(alphabet, length, itter):
    answer = []
    alpha_length = len(alphabet)
    if itter > alpha_length ** length:
        return None
    else:
        for i in range(length):
            answer.append(alphabet[(itter / (alpha_length ** (length - i - 1))) % alpha_length])
        return "".join(answer)


def expand_chars_combination(alphabet, length, itter, function):
    return function(chars_combination(alphabet, length, itter))
########################################################################################################################
# EXPANDERS


def ulll_expander(word):
    """
    """
    return first_to_upp(word)


def leet_expander_numbers(input_word):
    """
    """
    round_a = "abeiostdg"
    round_n = "483105796"
    return change(input_word, get_indexes(input_word, round_a), round_a, round_n)


def leet_expand_symbols(input_word):
    """
    """
    round_a = "asithxce"
    round_n = "@$!+#%(&"
    return change(input_word, get_indexes(input_word, round_a), round_a, round_n)

########################################################################################################################


def first_to_upp(word):
    """
    """
    word = list(word)
    word[0] = word[0].upper()
    return "".join(word)


def dd(word):
    """
    """
    output_list = []
    for ittr in range(100):
        if ittr < 10:
            output_list.append(word + "0" + str(ittr))
        else:
            output_list.append(word + str(ittr))
    return output_list

# PATTERNS


def ldd_pattern(input_words):
    """u - uppercase letter, l - lowercase letters, d - digit
    Pattern: a*n + 11
    """
    output_list = []
    for element in input_words:
        output_list += dd(element)
    return output_list


def uldd_pattern(input_words):
    """u - uppercase letter, l - lowercase letters, d - digit
    Pattern: A + a*n + 11
    """
    output_list = []
    for element in input_words:
        output_list += dd(first_to_upp(element))
    return output_list


def ldddd_pattern(input_list, start, stop):
    """u - uppercase letter, l - lowercase letters, d - digit
    Pattern: a*n + 1111
    """
    numbers_list = []
    for i in range(stop - start + 1):
        numbers_list.append(str(start))
        start += 1
    return [x + y for x in input_list for y in numbers_list]


def uldddd_pattern(input_list, start, stop):
    """u - uppercase letter, l - lowercase letters, d - digit
    Pattern: A + a*n + 1111
    """
    numbers_list = []
    for j in range(len(input_list)):
        input_list[j] = first_to_upp(input_list[j])

    for i in range(stop - start + 1):
        numbers_list.append(str(start))
        start += 1
    return [x + y for x in input_list for y in numbers_list]


def ulll_pattern(input_list):
    """u - uppercase letter, l - lowercase letters, d - digit
    Pattern: A + a*n
    """
    output_list = []
    for element in input_list:
        output_list.append(first_to_upp(element))
    return output_list


def uuu_pattern(input_list):
    """u - uppercase letter, l - lowercase letters, d - digit
    Pattern: A*n
    """
    output_list = []
    for element in input_list:
        output_list.append(element.upper())
    return output_list

########################################################################################################################
