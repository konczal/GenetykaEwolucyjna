import sys
import statistics

inF = sys.argv[1]
nSamp = int(sys.argv[4])

#Columns used to filter by DP
#4,7,10,13,16,19,22,25,etc.

Cols = [3+(x*3) for x in range(nSamp)]

a = open(inF, "r")
DPs = []
for line in a:
        raw = line.strip().split()
        C1 =list( raw[i] for i in Cols )
        C = [int(i) for i in C1]
        m = float(sum(C)) / len(C)
        print(str(m))
        DPs.append(m)
a.close()

mm = sum(DPs)/len(DPs)
mm2 = statistics.median(DPs)

print("#Mean DP: " + str(mm))
print("#Median DP: " + str(mm2))
