#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dictgenpy3 import *


def join(mix_flag, concat_flag, passwords_file, logins_file):
    passwords = file_to_list(passwords_file)
    logins = file_to_list(logins_file)
    if mix_flag:
        return mix_logins_and_passwords(logins, passwords, ':')
    elif concat_flag:
        return join_logins_and_passwords(logins, passwords, ':')
