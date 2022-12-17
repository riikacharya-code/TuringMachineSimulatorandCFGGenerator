from random import random
import sys

if len(sys.argv) != 3:
    print("Usage: %s -f" % sys.argv[0])
    exit()

# Sources:
# https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index#:~:text=As%20strings%20are%20immutable%20in,value%20at%20the%20desired%20index.&text=You%20can%20quickly%20(and%20obviously,%22slices%22%20of%20the%20original.

# list to hold all lines of turing machine encoding
turing_machine_encoding = []

# filters out all the comments in the txt and gets rid of '\n' characters
for line in open(sys.argv[1], "r").readlines():
    if (line.rstrip() != ''):
        turing_machine_encoding.append(line.rstrip())

# input string
input = sys.argv[2]

# if one of these are true, 
accept = False
reject = False

# determines if there was any move made including a move to the same state
# if this is not true by the end, input was rejected
moved = False

current_state = turing_machine_encoding[0][0:2]
char = ''

# line index
i = 0
# character index of input
j = 0

print(input[0:j] + '[' + current_state + ']' + input[j:])

while (not accept) and (not reject):
    
    if current_state == turing_machine_encoding[i][0:2]:
        
        if input[j] ==turing_machine_encoding[i][3]:
            
            # indicates there was a move made during this cycle
            moved = True
            
            # writes at index j
            input = input[0:j] + turing_machine_encoding[i][5] + input[j+1:]
            
            # moves depending on which sign
            if turing_machine_encoding[i][7] == '>':
                j += 1
            else:
                j -= 1
            
            # current state is state at end
            current_state = turing_machine_encoding[i][9:]
            
            # accept gets true if the current state is ACCEPT
            if current_state == "ACCEPT":
                accept = True
        
            print(input[0:j] + '[' + current_state + ']' + input[j:])
            
        # expands the tape if need be
        if (j < 0):
            input = '_' + input
            j = 0
            
        if (j >= len(input)):
            input += '_'

    
    #increment line index or return it to 0
    i += 1
    
    if (i >= len(turing_machine_encoding)):
        i = 0
        
        # if no moves during this cycle, reject
        if (not moved):
            reject = True
            current_state = "REJECT"
            print(input[0:j] + '[' + current_state + ']' + input[j:])
        
        moved = False


# prints if it accepts or rejects
if accept:
    print("Accept")
else:
    print("Reject")