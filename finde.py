

# RESOLVE ISSUE First 10-digit prime in consecutive digits of e


from decimal import Context
import math

original = str(Context(prec=300).exp(1)) 
print(original)

count =2
while True:
    tempTen = int(original[count:count+10]) 
    if tempTen%6==1 or tempTen%6==5:
        currentHigh = abs(int(math.sqrt(tempTen)))
        for i in range(2, currentHigh+1):
            if tempTen%i==0:  
                count = count+1
                break 
            elif i!=currentHigh:
                continue
            else:
                print("this is our number", tempTen)
                exit()              
    else:
        count = count+1
