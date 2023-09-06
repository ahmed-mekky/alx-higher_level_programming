#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "" or str[n] == "":
        return ""
    chr = str[n]
    return str.replace(chr, "")
