#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dictgenpy3 import *
from passgen import password_generator


def add_passwords(file_path, alpha_char, length, amount, pattern, random_flag, index_flag, popular_flag, leet_flag):
    logins = file_to_list(file_path)
    passwords = password_generator(alpha_char, length, amount, pattern, random_flag, index_flag, popular_flag, leet_flag)
    return mix_logins_and_passwords(logins, passwords, ':')
