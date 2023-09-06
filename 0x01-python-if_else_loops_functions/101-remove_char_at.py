#!/usr/bin/python3
def remove_char_at(str, n):
    if str == NULL or str[n] == NULL:
        return NULL
    chr = str[n]
    return str.replace(chr, "")
