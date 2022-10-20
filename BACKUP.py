import csv
from os import system
from time import sleep

def menu():
        while True:
                print('1.reserve ticket\n2.view booked ticket\n3.cancel ticket\n4. Train Schedule\n5. Log Out ')
                ch1=int(input('enter your choice'))
                if ch1==1:
                        reserve()
                elif ch1==2:
                        view()
                elif ch1==3:
                        cancel()
                elif ch1==4:
                        schedule()
                elif ch1==5:
                        logout()
                else:
                        print('wrong option')
        if check==False:
            print("Try again")

def menu1():
        while True:
                print('1. Update Train Schedule\n2. Add New Train Info')
                ch1=int(input('enter your choice'))
                if ch1==1:
                        updateschedule()
                elif ch1==2:
                    trainadd()
                else:
                    print("wrong option")
                


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
                                # Adding variables to be used later in another function as global
                                global accountname
                                accountname = username
                                c=True
                                break
                        if password!=l[i][1]:
                                print('--------  wrong password  ---------')
                                c=False
                                main()
                else:
                    print('name not found')
                if c==True:
                    print("Please wait.....")
                    sleep(3)
                    system('cls')
                    menu()
       
           
def logout():
    print("Logging out from your account")
    print("Please Wait....")
    sleep(3)
    system('cls')
    main()





c=1256940
def reserve():
    check=False
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
                        elif ch==2:
                            pri=i[5]
                        tn=i[1]
                        time=i[2]
                        dep=i[3]
                        ari=i[4]
                        user=accountname
                        c=c+1
                x=[c,tno,nm,tn,time,dep,ari,pri,user]
                w.writerow(x)
                print(" ===== RESERVATION SUCCESSFUL =====")
            '''if check==False:
                with open('ticketavail.csv','r',newline='') as file:
                    reader=csv.reader(file)
                l=list(reader)
                for i in l:
                    if i[0]==tno:
                        ticket=(i[1])
                        ticket=ticket-1
                        data=[ticket]
                        l.remove(i[1])
                        l.insert(1,data)
                    with open('ticketavail.csv','w',newline='') as file:
                        w=csv.writer(file)
                        w.writerows(l)'''
                        

        

def view():
    check=False
    with open('tickets.csv','r',newline='')as file:
        r=csv.reader(file)
        l=list(r)
        n=input('enter reserved name:')
        for i in l:
            if n==i[2]:
                if accountname==i[8]:
                        print('\tTicket Number\tTrain Number\tPassenger Name\tTrain Name\tTime\tDeparture Station\tArrival Station\tFare')
                        print('\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6],'\t',i[7])
                        check=True
                if check==False:
                    print("This ticket doesn't exist / was not booked from your account. You cannot view it !")
            


def schedule():
    check=False
    with open('traininfo.csv','r',newline='')as file:
        r=csv.reader(file)
        l=list(r)
        print('\tTrain Number\tTrain Name\tTrain time\tDeparture Station\tArrival Station\tnon-ac price\tAc Price')
        for i in l:   
            print('\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6])
            

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
        if check==False:
            print("Name not found")
        if check==True:
            with open('tickets.csv','w',newline='')as f:
                w=csv.writer(f)
                w.writerows(l)
                print('ticket canceled sucessfully\nthankyou\nvisit again')

def updateschedule():
        check=False
        nm=input('Enter train number to be modified')
        with open('traininfo.csv','r',newline='') as f2:
                reader=csv.reader(f2)
                l=list(reader)
                for i in l:
                    if nm==i[0]:
                        train=input('Enter enter Train Name')
                        time=input('Enter Train Time')
                        dep=input('Enter departure station')
                        arv=input('enter arival station')
                        nonac=input('enter the non-ac price')
                        ac=input('enter the ac price')
                        n=l.index(i)
                        data=[nm,train,time,dep,arv,nonac,ac]
                        l.remove(i)
                        l.insert(n,data)
                        check=True
                
                if check==False:
                    print('not found')
                else:
                    with open('traininfo.csv','w',newline='') as file:
                        w=csv.writer(file)
                        w.writerows(l)
                        print('modified record')
            
def trainadd():
    while True:
        with open('traininfo.csv','a',newline='') as file:
            writer=csv.writer(file)
            trainno=input('Enter The Train Number : ')
            trainname=input('Enter The Train Name : ')
            traintime=input('Enter The Train Time : ')
            traaindep=input('Enter The Departure Station Name : ')
            trainarriv=input('Enter The Train Arrival Station : ')
            acprice=input('Enter AC PRICE : ')
            nonac=input('Enter Non-Ac Price : ')
            writer.writerow([trainno,trainname,traintime,traaindep,trainarriv,traaindep,nonac,acprice])
        print('Train Information Successfully Added ! ')
        break
        


def admin():
        with open('admin.csv','r') as file:
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
                                    c=False
                                    break
            else:
                print('name not found')
            if c==True:
                    menu1()
       



def main():
    print('1.Sign Up\n2. Login\n3. Login As Admin\n4. Quit ')
    ch=int(input('enter your choice'))
    if ch==1:
           signup()
    if ch==2:
            login()
    if ch==3:
            admin()
    if ch==4:
        quit()
    else:
        print("wrong choice")

main()


