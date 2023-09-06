#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "" or n > len(str):
        return ""
    chr = str[n]
    return str.replace(chr, "")
