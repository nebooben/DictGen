#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from dictgenpy3 import *
# from getusers import get_users
from extract import extract
from join import join as the_join
from passgen import password_generator
from addpass import add_passwords
from help import *

main_path = ''


def partition(command):
    command = command.split(' ')
    to_str = []
    for elm in command:
        to_str.append(str(elm))
    command = to_str
    output_list = []
    for i in range(len(command) - 1):
        al = []
        if '-' in command[i] and '-' not in command[i + 1]:
            al.append(command[i])
            al.append(command[i + 1])
            output_list.append(al)
        elif '-' in command[i] and '-' in command[i + 1]:
            al.append(command[i])
            output_list.append(al)
    if '-' in command[len(command) - 1]:
        al = list()
        al.append(command[len(command) - 1])
        output_list.append(al)
    return output_list


def start(argv):
    utility = argv[:1][0]
    command = argv[1:]
    if utility in ['-h', 'help', '-help', '--help']:
        print say_help
        sys.exit()
    alpha_char = 'l'
    pattern = ''
    # service = ''
    # seed_user = ''
    file_path = ''
    passwords_file = ''
    output_name = 'base_' + "_".join(time.ctime(time.time()).replace(':', '-').split(' ')[1:-1])

    length = 8
    amount = 10000
    # deep = 0

    random_flag = False
    index_flag = False
    popular_flag = False
    leet_flag = False
    mix_flag = False
    concat_flag = False
    domains_flag = False
    logins_flag = False
    for part in partition(' '.join(command)):
        if len(part) == 1:
            if part[0] in ['-x', '-mix']:
                mix_flag = True
            elif part[0] in ['-z', '-concat']:
                concat_flag = True
            elif part[0] in ['-r', '-random']:
                random_flag = True
            elif part[0] in ['-i', '-index']:
                index_flag = True
            elif part[0] in ['-w', '-worst', '-popular']:
                # print 'worst'
                popular_flag = True
            elif part[0] in ['-t', '-leet']:
                leet_flag = True
            elif part[0] in ['-d', '-domains']:
                domains_flag = True
            elif part[0] in ['-l', '-logins']:
                logins_flag = True
        elif len(part) == 2:
            opt, arg = part
            # if opt in ['-s', '-service']:
            #     service = arg
            # elif opt in ['-u', '-user', '-seeduser']:
            #     seed_user = arg
            # elif opt in ['-d', '-deep']:
            #     deep = int(arg)
            if opt in ['-a', '-alphabet']:
                alpha_char = arg
            elif opt in ['-l', '-length']:
                length = int(arg)
            elif opt in ['-c', '-amount']:
                amount = int(arg)
            elif opt in ['-e', '-pattern']:
                if arg in ['ldd', 'uldd', 'ldddd', 'uldddd', 'ulll', 'uuu']:
                    pattern = arg
                else:
                    pattern = 'none'
            elif opt in ['-f', '-logins', '-file_path', '-emails', '-emails_file']:
                file_path = main_path + arg
            elif opt in ['-p', '-passwords', '-passwords_file']:
                passwords_file = main_path + arg
            elif opt in ['-o', '-output_name', '-output']:
                output_name = arg
    # if utility == 'getusers':
    #     try:
    #         output = get_users(service, seed_user, deep)
    #     except Exception as e:
    #         print 'getusers ' + e.message
    #         sys.exit()
    if utility == 'addpass':
        try:
            output = add_passwords(file_path, alpha_char, length, amount, pattern, random_flag, index_flag, popular_flag, leet_flag)
        except Exception as e:
            print 'addpass ' + e.message
            sys.exit()
    elif utility == 'passgen':
        try:
            output = password_generator(alpha_char, length, amount, pattern, random_flag, index_flag, popular_flag, leet_flag)
        except Exception as e:
            print 'passgen ' + e.message
            sys.exit()
    elif utility == 'join':
        try:
            output = the_join(mix_flag, concat_flag, passwords_file, file_path)
        except Exception as e:
            print 'join ' + e.message
    elif utility == 'extract':
        try:
            output = extract(logins_flag, domains_flag, file_path)
        except Exception as e:
            print 'extractor ' + e.message
            sys.exit()
    else:
        print 'Invalid utility!'
        sys.exit()

    list_to_file(output, main_path + output_name)

    return output


if __name__ == "__main__":
    try:
        print say_hi
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "Interrupted by user.."
    except:
        sys.exit()
