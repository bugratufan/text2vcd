import sys, os

identifier = 33
filepath = sys.argv[-1]
filename, fileExtension = os.path.splitext(filepath)
word_count = 32

if(fileExtension != ".txt"):
    print(fileExtension)
    exit("Error! File extension is not compatible.")

targetFileName = filename + ".vcd"


f = open(filepath, 'r')
fo = open(targetFileName, 'w')
lines = f.readlines()
f.close()

header = '''
$date
    No Date.
$end
$version
    txt2vcd V1.0
$end
$comment
    Any comment text.
$end
$timescale 1ps $end
$scope module logic $end\n
'''
header += "$var wire 1 "+chr(identifier)+" clk $end\n"
for a in range(word_count):
    header += "$var wire 8 "+chr(a+identifier+1)+" probe_"+str(a)+" $end\n"

header += "$upscope $end\n"
header += "$enddefinitions $end\n"
header += "$dumpvars\n"
header += "b0 "+chr(identifier)+"\n"
for a in range(word_count):
    header += "b00000000 "+chr(a+identifier+1)+"\n"
header += "$end\n"

time_counter = 0
line_counter = 0
print(len(lines))
while line_counter+32 < len(lines):
    header += "#"+str(time_counter*8000)+"\n"
    header += "b1 !\n"
    for a in range(32):
        header += "b"+format(int(lines[line_counter],16), '08b') + " " +chr(a+identifier+1)+"\n"
        line_counter = line_counter + 1;
    header += "#"+str(time_counter*8000+4000)+"\n"
    header += "b0 !\n"
    time_counter = time_counter + 1;
    print(line_counter)

fo.write(header)
fo.close()
