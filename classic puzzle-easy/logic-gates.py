#https://www.codingame.com/ide/puzzle/logic-gates
import sys
import math

# Function to simulate AND Gate
def AND(A, B):
	return A & B;	
# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	
# Function to calculate OR Gate
def OR(A, B):
	return A | B;
# Function to simulate XOR Gate
def XOR(A, B):
	return A ^ B    
# Function to simulate NAND Gate
def NAND(A, B):
	return NOT(AND(A, B))
# Function to simulate NOR Gate
def NOR(A, B):
	return NOT(OR(A, B))
# Function to simulate XNOR Gate
def NXOR(A, B):
	return NOT(XOR(A, B))

n = int(input())
m = int(input())
signal = []
for i in range(n):
    x=input().split()
    signal.append(x[0])
    s=""
    for i in x[1]:
        if i=='-': s+="1"
        else: s+="0"
    signal.append(s)

for i in range(m):
    arb, gate, n1, n2 = input().split()
    a=signal.index(n1)+1
    b=signal.index(n2)+1
    s=""
    
    if gate=="AND":
        for x in range(len(signal[a])):
            if AND(int(signal[a][x]),int(signal[b][x])) == 1:
                s+="-"
            else:
                s+="_"
    if gate=="OR":
        for x in range(len(signal[a])):
            if OR(int(signal[a][x]),int(signal[b][x])) == 1:
                s+="-"
            else:
                s+="_"
    if gate=="XOR":
        for x in range(len(signal[a])):
            if XOR(int(signal[a][x]),int(signal[b][x])) == 1:
                s+="-"
            else:
                s+="_"
    if gate=="NAND":
        for x in range(len(signal[a])):
            if NAND(int(signal[a][x]),int(signal[b][x])) == 1:
                s+="-"
            else:
                s+="_"
    if gate=="NOR":
        for x in range(len(signal[a])):
            if NOR(int(signal[a][x]),int(signal[b][x])) == 1:
                s+="-"
            else:
                s+="_"
    if gate=="NXOR":
        for x in range(len(signal[a])):
            if NXOR(int(signal[a][x]),int(signal[b][x])) == 1:
                s+="-"
            else:
                s+="_"
    print(arb,s)
