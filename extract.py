#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dictgenpy3 import *


def extract(logins_flag, domains_flag, emails_filename):
    input_list = file_to_list(emails_filename)
    if logins_flag:
        return word_extractor(input_list, 0, '@')
    elif domains_flag:
        return word_extractor(input_list, 1, '@')
