import math
capacitors =[0.0000047,0.00001,0.000015,0.000022,0.000033,0.000047,0.000068,0.0001,0.00015,0.00022,0.00033,0.00047,0.00068,.0001,.00015,.00022,.00033,.00047,.00068,.0010,.0015,.0022,.0033,.0047,.0068,.0100,.0220,.0470,.068,.1,.22,.47,2.2,4.7,10,47]
resistors=[100,150,180,220,270,330,390,470,560,680,820,1000,2200,2700,3300,3900,4700,5600,6800,8200,10000,12000,15000,18000,22000,27000,33000,39000,47000,56000,68000,82000,100000,120000,150000,180000,220000,270000,330000,390000,470000,560000,680000,820000,1000000]
highFreqDiff=[]
lowFreqDiff=[]
highFrequency= 900
lowFrequency=700
fileOne=open("highCut.txt","w")
fileTwo=open("lowCut.txt","w")
highValue=(1/(highFrequency*math.pi*2))*(10**(6))
lowValue=(1/(lowFrequency*math.pi*2))*(10**(6))

fileOne.write(str(highValue) +"\n")
fileTwo.write(str(lowValue)+"\n")
numberOfCap=len(capacitors)
numberOfRes=len(resistors)

for cap in range(0,numberOfCap):
    for res in range(0,numberOfRes):
                number = capacitors[cap]*resistors[res]
                freq = 1/(number*(10**-6)*2*math.pi)
                highDiff=highFrequency-freq
                lowDiff=lowFrequency-freq
                if number>(highValue-10) and number<(highValue+10):
                        outPut = "Frequency diff: "+ str(highDiff)+" Value: "+str(number)+" Cap 1: " + str(capacitors[cap])+ " Res 1: "+str(resistors[res])+"\n"
                        highFreqDiff.append(highDiff)
                        fileOne.write(outPut)
                if number>(lowValue-10) and number<(lowValue+10):
                        outPut = "Frequency diff: "+ str(lowDiff)+" Value: "+str(number)+" Cap 1: " + str(capacitors[cap])+ " Res 1: "+str(resistors[res])+"\n"
                        lowFreqDiff.append(lowDiff)
                        fileTwo.write(outPut)
fileOne.close()
fileTwo.close()
