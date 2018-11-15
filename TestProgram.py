import time

dataToLog = []
log = open('logging.txt','w')


for num in range(1,100000):
    status = True
    if(num > 1):
        for i in range(2,num):
            if(num%i==0):
                status = False
                break
    else:
        status = False
    if(status == True):
        dataToLog.append((num,'Y',time.perf_counter()))
    else:
        dataToLog.append((num,'N',time.perf_counter()))

for num,status,time in dataToLog:
    log.writelines(str(num)+','+str(time)+','+status+'\n')

log.writelines('Total time used: '+str(dataToLog[-1][2]-dataToLog[0][2]))