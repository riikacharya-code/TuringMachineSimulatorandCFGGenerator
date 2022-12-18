import sys

#https://blog.finxter.com/how-to-execute-a-file-with-arguments-in-python/#:~:text=In%20summary%2C%20the%20steps%20to%20execute%20a%20file,pass%20it%20the%20argument%20list%20as%20a%20parameter
#https://www.tutorialkart.com/python/python-read-file-as-string/#:~:text=Python%20%E2%80%93%20Read%20File%20as%20String%201%20Open,calling%20close%20%28%29%20method%20on%20the%20file%20object.


if len(sys.argv) != 2:
    print("Usage: %s -f" % sys.argv[0])
    exit()
    
cfg = open(sys.argv[1], "r")

data = cfg.read()

print(data)





