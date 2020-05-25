HZK16_1_0 = open("HZK_16_1_0.txt","w")
HZK16_1_1 = open("HZK_16_1_1.txt","w")
HZK16_1_2 = open("HZK_16_1_2.txt","w")
HZK16_1_3 = open("HZK_16_1_3.txt","w")
HZK16_1_0.write("v2.0 raw\n\n")
HZK16_1_1.write("v2.0 raw\n\n")
HZK16_1_2.write("v2.0 raw\n\n")
HZK16_1_3.write("v2.0 raw\n\n")
with open("HZK16_1.txt") as f:
    lines = f.readlines()
    linecnt = len(lines)
    partLineCnt = 4096
    for i in range(partLineCnt):
        HZK16_1_0.write(lines[i])
        HZK16_1_1.write(lines[i+partLineCnt])
    for line in lines[2*partLineCnt:]:
        HZK16_1_2.write(line)
HZK16_1_0.close()
HZK16_1_1.close()
HZK16_1_2.close()
HZK16_1_3.close()