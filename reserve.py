import csv
global c
def reserve():
    x=[]
    with open('traininfo.csv','r',newline='')as file:
        r=csv.reader(file)
        l=list(r)
    with open('tickets.csv','a',newline='')as f1:
            w=csv.writer(f1)
            n=int(input('enter the number of tickets: '))
            c=1256940
            for i in range(n):
                nm=input('enter your name: ')
                tno=int(input('enter the train no: '))
                for i in l:
                    if tno==int(i[0]):
                        print('1.AC class\n2.NON-AC class')
                        ch=int(input('enter your choice'))
                        if ch==1:
                            pri=i[6]
                        if ch==2:
                            pri=i[5]
                        tn=i[1]
                        time=i[2]
                        dep=i[3]
                        ari=i[4]
                        c=c+1
                x=[c,tno,nm,tn,time,dep,ari,pri]
                w.writerow(x)
        
   

 
            
            
reserve()
