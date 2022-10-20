import csv

def signup():
    
        with open('railway.csv','a',newline='') as file:
            writer=csv.writer(file)
            username=input('Enter Username for the new account')
            password=input('Enter the password for the new account ')
            while True:
                checkpass=input("Enter the password once again")
                if password==checkpass:
                    writer.writerow([username,password])
                    print('________________________________________')
                    print('Signed Up / Account created successfully!')
                    print('________________________________________')
                    break
                else:
                    print("-----  Incorrect Password  --------")


def login():
    with open('railway.csv','r') as file:
        r=csv.reader(file)
        l=list(r)
        c=False
        username=input("enter name")
        for i in range(len(l)):
            if l[i][0]==username:
                password=input('enter password')
                if password==l[i][1]:
                     print('____________________________')
                     print("      login sucessfully    ")
                     print('____________________________')
                     c=True
                     break
                if password!=l[i][1]:
                    print('--------  wrong password  ---------')
                    c=True
                    break
        if c==False:
            print('name not found')
    
        
       
           

c=1256940
def reserve():
    x=[]
    with open('traininfo.csv','r',newline='')as file:
        r=csv.reader(file)
        l=list(r)
    with open('tickets.csv','a',newline='')as f1:
            w=csv.writer(f1)
            n=int(input('enter the number of tickets: '))
            global c
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
                print(" ===== RESERVATION SUCCESSFUL =====")
        

def view():
    check=False
    with open('tickets.csv','r',newline='')as file:
        r=csv.reader(file)
        l=list(r)
        n=input('enter your  name:')
        for i in l:
            if n==i[2]:
                print('\tTicket Number\tTrain Number\tPassenger Name\tTrain Name\tTime\tDeparture Station\tArrival Station\tFare')
                print('\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7])
                check=True
        if check==False:
            print('name not found')
        


def schedule():
    check=False
    with open('traininfo.csv','r',newline='')as file:
        r=csv.reader(file)
        l=list(r)
        print(l)


def cancel():
    check=False
    with open('tickets.csv','r',newline='')as file:
        r=csv.reader(file)
        l=list(r)
        n=input('enter your reserved name:')
        for i in l:
            if n==i[2]:
                l.remove(i)
                check=True
        if check==True:
            with open('tickets.csv','w',newline='')as f:
                w=csv.writer(f)
                w.writerows(l)
                print('ticket canceled sucessfully\nthankyou\nvisit again')
        





check=False
print('1.Sign Up\n2. Login')
ch=int(input('enter your choice'))
if ch==1:
        signup()
if ch==2:
        login()
        check=True
        if check==False:
            print("Try again")






















    

