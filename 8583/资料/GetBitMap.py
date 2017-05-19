
NumStr=str(input("Input the bit map with HEX format\r\n"))
NumStr=NumStr.replace(' ','')
BitMap=int(NumStr,base=16)
Iterater=1;Iterater<<=64
for i in range(0,65):
    if Iterater & BitMap:print(i,end=",")
    Iterater >>= 1







