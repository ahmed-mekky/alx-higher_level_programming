#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "":
        return ""
    elif n > len(str) or n < 0:
        return str
    chr = str[n]
    return str.replace(chr, "")
