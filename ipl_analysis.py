data = [['GT', 20, 1, 1, 0, 0, 1],['LSG', 18, 1, 0, 0, 1, 1],['RR', 16, 1, 0, 1, 0, 0],['DC', 14, 1, 1, 0, 1, 0],['RCB', 14, 0, 1, 1, 0, 0],['KKR', 12, 0, 1, 1, 0, 1],['PBKS', 12, 0, 1, 0, 1, 0],['SRH', 12, 1, 0, 0, 0, 0],['CSK', 8, 0, 0, 1, 0, 1],['MI', 6, 0, 1, 0, 1, 1]]

sum=0
Teamcount=0

#Two consecutive losses 
for j in range (0,10):
    for i in range (2,6):
        if data[j][i] == 0:
            if data[j][i]==data[j][i+1]:
                sum = sum + data[j][1]
                Teamcount=Teamcount+1
                print(data[j][0] ,"has two consecutive loses") 
                break
print("\n Average of teams that has two consecutive losses:", sum/Teamcount ,"\n")

sum=0
Teamcount=0

#Two consecutive Wins
for j in range (0,10):
    for i in range (2,6):
        if data[j][i] == 1:
            if data[j][i]==data[j][i+1]:
                sum = sum + data[j][1]
                Teamcount=Teamcount+1
                print(data[j][0] ,"has two consecutive Wins") 
                break
print("\n Average of teams that has two consecutive Wins:", sum/Teamcount ,"\n")

sum=0
Teamcount=0

#Three consecutive loses 
for j in range (0,10):
    for i in range (2,5):
        if data[j][i] == 0:
            if data[j][i]==data[j][i+1] and data[j][i+1]==data[j][i+2]:
                sum = sum + data[j][1]
                Teamcount=Teamcount+1
                print(data[j][0] ,"has three consecutive loses") 
                break
print("\n Average of teams that has three consecutive losses:", sum/Teamcount, "\n")

sum=0
Teamcount=0

#Three consecutive Wins 
for j in range (0,10):
    for i in range (2,5):
        if data[j][i] == 1:
            if data[j][i]==data[j][i+1] and data[j][i+1]==data[j][i+2]:
                sum = sum + data[j][1]
                Teamcount=Teamcount+1
                print(data[j][0] ,"has three consecutive Wins") 
                break
                
    if Teamcount==0:
        print("\n No Teams have won Thrice consecutively \n")
        break
    else:
        print("\n Average of teams that has three consecutive Wins:", sum/Teamcount, "\n")
        
sum=0
Teamcount=0

#Four consecutive loses 
for j in range (0,10):
    for i in range (2,4):
        if data[j][i] == 0:
            if data[j][i]==data[j][i+1] and data[j][i+1]==data[j][i+2]:
                if data[j][i+2]==data[j][i+3]:
                    sum = sum + data[j][1]
                    Teamcount=Teamcount+1
                    print(data[j][0] ,"has Four consecutive loses") 
                    break
print("\n Average of teams that has three consecutive Wins:", sum/Teamcount, "\n")    
sum=0
Teamcount=0

#Four consecutive Wins 
for j in range (0,10):
    for i in range (2,4):
        if data[j][i] == 1:
            if data[j][i]==data[j][i+1] and data[j][i+1]==data[j][i+2]:  
                if data[j][i+2]==data[j][i+3]:
                    sum = sum + data[j][1]
                    Teamcount=Teamcount+1
                    print(data[j][0] ,"has Four consecutive Wins") 
                    break
                
    if Teamcount==0:
        print("\n No Teams have won four times consecutively \n")
        break
    else:
        print("\n Average of teams that has four consecutive Wins:", sum/Teamcount, "\n")
