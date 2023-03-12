#!/usr/bin/python3
#
# DESC : This script take a hex string an display the little endian hex string version
#
# EXAMPLE : ./hexToLittle bffff450
#           \x50\xf4\xff\xbf
#
# CREDITS : @yorgsone , @lobbyra

import sys

sys.stderr.write("be careful to enter an odd lengthed hex string\n")

userInput = sys.argv[1]
arr = []

for i, v in enumerate(userInput):
    if i % 2:
        arr.append(userInput[i - 1] + userInput[i])

arr.reverse()

res = '\\x'.join(arr)
res = '\\x' + res
print(res)
