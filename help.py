#!/usr/bin/env python
# -*- coding: utf-8 -*-


say_help = r"""Usage:
-h: help
[passgen]:
    -r: random passwords
        -a: alpha chars ('u' for uppercase, 'l' for lowercase, 'd' for digits)
        -l: length of password
        -c: amount of passwords
        -o: output filename
        -e: pattern
            Patterns: ('u' for uppercase, 'l' for lowercase, 'd' for digits)
            [0] none --------- no pattern
            [1] ldd ---------- qwerty45
            [2] uldd --------- Qwerty45
            [3] ldddd -------- qwerty1223
            [4] uldddd ------- Qwerty1223
            [5] ulll --------- Qwerty
            [6] uuu ---------- QWERTY

    -i: password by index (from aaa to zzz)
        -a: alpha chars ('u' for uppercase, 'l' for lowercase, 'd' for digits)
        -l: length of password
        -c: amount of passwords
        -o: output filename
        -e: pattern
            Patterns: ('u' for uppercase, 'l' for lowercase, 'd' for digits)
            [0] none --------- no pattern
            [1] ldd ---------- qwerty45
            [2] uldd --------- Qwerty45
            [3] ldddd -------- qwerty1223
            [4] uldddd ------- Qwerty1223
            [5] ulll --------- Qwerty
            [6] uuu ---------- QWERTY

    -w: worst passwords, the most popular passwords
        -o: output filename

    -t: leet-speak variation of the most popular passwords
        -o: output filename

    Example: passgen -w
    Example: passgen -t
    Example: passgen -t -o output.txt
    Example: passgen -r -a uld -e none -l 8 -c 1000
    Example: passgen -i -a ld -e uldd -l 8 -c 1000
    Example: passgen -i -a d -l 4 -c 10000 -o pins

[addpass]:
    -f: file with logins
    -r: random passwords
        -a: alpha chars ('u' for uppercase, 'l' for lowercase, 'd' for digits)
        -l: length of password
        -c: amount of passwords
        -o: output filename
        -e: pattern
            Patterns: ('u' for uppercase, 'l' for lowercase, 'd' for digits)
            [0] none --------- no pattern
            [1] ldd ---------- qwerty45
            [2] uldd --------- Qwerty45
            [3] ldddd -------- qwerty1223
            [4] uldddd ------- Qwerty1223
            [5] ulll --------- Qwerty
            [6] uuu ---------- QWERTY

    -i: password by index (from aaa to zzz)
        -a: alpha chars ('u' for uppercase, 'l' for lowercase, 'd' for digits)
        -l: length of password
        -c: amount of passwords
        -o: output filename
        -e: pattern
            Patterns: ('u' for uppercase, 'l' for lowercase, 'd' for digits)
            [0] none --------- no pattern
            [1] ldd ---------- qwerty45
            [2] uldd --------- Qwerty45
            [3] ldddd -------- qwerty1223
            [4] uldddd ------- Qwerty1223
            [5] ulll --------- Qwerty
            [6] uuu ---------- QWERTY

    -w: worst passwords, the most popular passwords
        -o: output filename

    -t: leet-speak variation of the most popular passwords
        -o: output filename

    Example: addpass -f logins.txt -r -l 6 -c 1000 -o none -a l -e output

[extract]:
    -f: file with emails
    -l: logins flag
    -d: domains flag

    Example: extract -f emails.txt -d
    Example: extract -f emails.txt -l -o logins
    Example: extract -f emails.txt -d -o domains
[join]:
    Example: join -x -f logins.txt -p passwords.txt
    Example: join -z -f logins.txt -p passwords.txt -o brutus

"""
say_hi = r"""      $$\ $$\             $$\
      $$ |\__|            $$ |
 $$$$$$$ |$$\  $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$$$$$$\
$$  __$$ |$$ |$$  _____|\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\
$$ /  $$ |$$ |$$ /        $$ |    $$ /  $$ |$$$$$$$$ |$$ |  $$ |
$$ |  $$ |$$ |$$ |        $$ |$$\ $$ |  $$ |$$   ____|$$ |  $$ |
\$$$$$$$ |$$ |\$$$$$$$\   \$$$$  |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |
 \_______|\__| \_______|   \____/  \____$$ | \_______|\__|  \__|
                                  $$\   $$ |
                                  \$$$$$$  |
                                   \______/

Coded by nebo_oben, 2015
"""
