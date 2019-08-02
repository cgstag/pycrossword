#!/bin/python3

import math
import os
import random
import re
import sys

# print board
def print_board(board):
    for row in board:
        fptr.write(''.join(row))
        fptr.write('\n')
        print(''.join(row))


# get possible locations for a given word in the board
def get_possible_locations(board, word):
    length = len(word)

    for i in range(10):
        for j in range(10):

            properSlotH = True
            properSlotV = True

            for k in range(length):
                if j<10-length+1:  # Horizontal direction, axis marked as 0:
                    if board[i][j+k] not in ['-',word[k]]:
                        properSlotH = False

                if i<10-length+1:  # Vertival direction, axis marked as 1:
                    if board[i+k][j] not in ['-',word[k]]:
                        properSlotV = False

            if properSlotH and j<10-length+1:
                yield (i,j,0)
            if properSlotV and i<10-length+1:
                yield (i,j,1)


# rollback commited word
def rollback(board, word, loc):
    i, j, axis = loc
    if axis == 0: # axis 0 is horizontal
        for k in range(len(word)):
            board[i][j + k] = '-'
    else: # axis 1 is vertical
        for k in range(len(word)):
            board[i + k][j] = '-'

# write the word on board at specified loc
def move(board, word, loc):
    i, j, axis = loc
    if axis == 0:
        for k in range(len(word)):
            board[i][j + k] = word[k]
    else:
        for k in range(len(word)):
            board[i + k][j] = word[k]

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(board, words):
    global finished

    if len(words) == 0:
        if not finished:
            print_board(board)
        finished = True
        return board

    word = words.pop()
    locations = get_possible_locations(board,word)

    for location in locations:
        move(board, word, location)
        crosswordPuzzle(board, words)
        rollback(board, word, location)

    words.append(word)


# Main Execution
if __name__ == "__main__":
    os.environ["OUTPUT_PATH"] = "/tmp/output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    crossword = []
    for _ in range(10):
        crossword_item = input()
        crossword.append(list(crossword_item))
    words = str(input()).split(";")

    finished = False
    crosswordPuzzle(crossword, words)

    fptr.close()