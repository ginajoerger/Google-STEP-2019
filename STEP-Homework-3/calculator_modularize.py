#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:11:38 2019

@author: ginajoerger
"""
def start(line): #starting point for given line
    if '*' in line or '/' in line:
        addedLine = addNone(line) #adds '@' at the end
        tokens = tokenize2(addedLine) #tokenizes the line
        partOne = evaluate2(tokens) #evaluates the line
        final = evaluate(partOne) #evaluates the simplified line
        return final
    else:
        tokens = tokenize(line) #tokenizes line
        final = evaluate(tokens) #evalautes line
        return final

def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def addNone(line): #This function adds a '@' at the end of the line.
    l = []
    for i in line:
        l.append(i)
    l.append('@')
    return ''.join(l)

def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readDivide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def readNone(line, index): #This function adds a type 'None' for '@'
    token = {'type': 'NONE'}
    return token, index + 1

def tokenize(line): #This function tokenizes functions without '*' and '/'
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def tokenize2(line): #This function tokenizes functions with '*' and '/'
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)
        elif line[index] == '@':
            (token, index) = readNone(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def evaluate(tokens): #This function only evaluates those without '*' and '/'
    answer = 0
    tokens.insert(0, {'type': 'PLUS'})
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer

def evaluate2(tokens): #This function evaluates those with '*' and '/'
    answer = []
    total = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                if tokens[index + 1]['type'] == 'PLUS' or tokens[index + 1]['type'] == 'MINUS':
                    answer.append('+')
                    answer.append(tokens[index]['number'])
                elif tokens[index + 1]['type'] == 'NONE':
                    answer.append('+')
                    answer.append(tokens[index]['number'])
                    break
                else:
                    answer.append('+')
                    total += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                if tokens[index + 1]['type'] == 'MINUS' or tokens[index + 1]['type'] == 'PLUS':
                    answer.append('-')
                    answer.append(tokens[index]['number'])
                elif tokens[index + 1]['type'] == 'NONE':
                    answer.append('-')
                    answer.append(tokens[index]['number'])
                    break
                else:
                    answer.append('-')
                    total += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MULTIPLY':
                if tokens[index + 1]['type'] == 'MULTIPLY' or tokens[index + 1]['type'] == 'DIVIDE':
                    total *= tokens[index]['number']
                elif tokens[index + 1]['type'] == 'NONE':
                    total *= tokens[index]['number']
                    answer.append(total)
                    break
                else:
                    total *= tokens[index]['number']
                    answer.append(total)
                    total = 0
            elif tokens[index - 1]['type'] == 'DIVIDE':
                if tokens[index + 1]['type'] == 'MULTIPLY' or tokens[index + 1]['type'] == 'DIVIDE':
                    total /= tokens[index]['number']
                elif tokens[index + 1]['type'] == 'NONE':
                    total /= tokens[index]['number']
                    answer.append(total)
                    break
                else:
                    total /= tokens[index]['number']
                    answer.append(total)
                    total = 0
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    stringed = [str(i) for i in answer]
    combined = ''.join(stringed)
    withoutBeginning = combined[1:]
    new = tokenize(withoutBeginning)
    return new
        
    
def test(line):
    actualAnswer = start(line)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("4+1*3/1")
    test("4.0+1.1*3.2/1.5")
    test("5.78*6.35/1.3")
    test("7.004*4.098+8")
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ', end="")
    line = input()
    answer = start(line)
    print("answer = %f\n" % answer)
    
    
    
