identifier = 33
filepath = sys.argv[-1]
filename, fileExtension = os.path.splitext(filepath)


if(fileExtension != ".txt"):
    print(fileExtension)
    exit("Error! File extension is not compatible.")

targetFileName = filename + ".hex"
logFileName = filename + ".log"


f = open(filepath, 'r')
fo = open(targetFileName, 'w')
flog = open(logFileName, 'w')
lines = f.readlines()
f.close()
