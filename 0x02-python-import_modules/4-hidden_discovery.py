#!/usr/bin/python3
import hidden_4 as hidden

if __name__ == '__main__':
    for item in dir(hidden):
        if item[:2] != '__':
            print(f"{item}")
