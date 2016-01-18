#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dictgenpy3 import *
from random import choice
from requests import get


lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'


def pattern_maker(input_list, word_pattern):
    if word_pattern == "":
        word_pattern = 'none'

    if word_pattern == 'none':
        return input_list
    elif word_pattern == 'ldd':
        return ldd_pattern(input_list)
    elif word_pattern == 'uldd':
        return uldd_pattern(input_list)
    elif word_pattern == 'ldddd':
        return ldddd_pattern(input_list, 0, 2200)
    elif word_pattern == 'uldddd':
        return uldddd_pattern(input_list, 0, 2200)
    elif word_pattern == 'ulll':
        return ulll_pattern(input_list)
    elif word_pattern == 'uuu':
        return uuu_pattern(input_list)


def random_passwords(alphabet, length, amount):
    output_list = []
    for i in range(amount):
        password = []
        for j in range(length):
            password.append(choice(list(alphabet)))
        output_list.append("".join(password))
    return output_list


def index_passwords(alphabet, length, amount):
    output_list = []
    for i in xrange(amount):
        output_list.append(chars_combination(alphabet, length, i))
    return output_list


def alpha_maker(alpha_char):
    alphabet = ''
    if 'l' in alpha_char:
        alphabet += lowercase
    if 'u' in alpha_char:
        alphabet += uppercase
    if 'd' in alpha_char:
        alphabet += digits
    return alphabet


def popular_passwords():
    # Create your own passwords lists with https://github.com/danielmiessler/SecLists/tree/master/Passwords
    # and pastebin.com :)
    output_list = get('http://pastebin.com/raw.php?i=BWHjRs5L').text.split('\r\n')
    return output_list


def leet_passwords():
    return leet(popular_passwords())


def password_generator(alpha_char, length, amount, pattern, random_flag, index_flag, popular_flag, leet_flag):
    answer = []
    if popular_flag:
        answer = popular_passwords()
    elif leet_flag:
        answer = leet_passwords()
    elif random_flag:
        answer = pattern_maker(random_passwords(alpha_maker(alpha_char), length, amount), pattern)
    elif index_flag:
        answer = pattern_maker(index_passwords(alpha_maker(alpha_char), length, amount), pattern)
    return answer
