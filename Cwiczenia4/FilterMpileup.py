import sys

inF = sys.argv[1]
minT = int(sys.argv[2])
maxT = int(sys.argv[3])
nSamp = int(sys.argv[4])

#Columns used to filter by DP
#4,7,10,13,16,19,22,25,etc.

Cols = [3+(x*3) for x in range(nSamp)]

a = open(inF, "r")
for line in a:
        raw = line.strip().split()
        C1 =list( raw[i] for i in Cols )
        C = [int(i) for i in C1]
        m = float(sum(C)) / len(C)
        if m > minT:
                if m < maxT:
                        print(line.strip())
a.close()
