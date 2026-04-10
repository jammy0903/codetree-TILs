import sys 
from collections import deque
input = sys.stdin.readline


word_input = input()
if type(word_input) != int : 
    word = [ord(c) for c in word_input]
    print(word)    
else : 
    print(type(word_input))