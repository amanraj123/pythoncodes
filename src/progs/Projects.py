from itertools import product

import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='12345')
cur = con.cursor()
cur.execute("create database if not exists items")
cur.execute("use items")
cur.execute("create table if not exists cs(sno int,products varchar(20),cost int)")
sql = "select*from cs"


cur.execute(sql)
res = cur.fetchall()
if res == []:
    cur.execute("insert into cs values(1,'Cake',50")
    cur.execute("insert into cs values(2,'Pastry',20)")
    cur.execute("insert into cs values(3,'Milk',60")
    cur.execute("insert into cs values(4,'Butter',20")
    cur.execute("insert into cs values(1,'Cheeze',30")
    con.commit()

cur.execute("create tables if not exists vip(sno int, varieties varchar(20))")
sql = "select*from vip"
cur.execute(sql)
res = cur.fetchall()
if res == []:
    cur.execute("insert into vip values(1,'Vanilla')")
    cur.execute("insert into vip values(2,'Chocolate')")
    cur.execute("insert into vip values(3,'Strawberry')")
    cur.execute("insert into vip values(4,'Butter_Scotch')")
    con.commit()
cur.execute("create table if not exixts worker(Sno int,Name varchar(20),Salary int)")
sql = "select*from worker"
cur.execute(sql)
res = cur.fetchall()
if res == []:
    cur.execute("insert into worker values(1,'Mukesh',123456)")
    cur.execute("insert into worker values(2,'Ram',1234)")
    cur.execute("insert into worker values(3,'Suresh',23459)")
    cur.execute("insert into worker values(4,'Raju',8987)")
    con.commit()

from datetime import datetime

print("..........................PROJECT................")
print("..........................PROJECT................")
print("..........................PROJECT................")
print("..........................PROJECT................")
print("..........................PROJECT................")
print("..........................PROJECT................")
print("..........................PROJECT................")
print("..........................PROJECT................")

ch = ''
while ch != 'N' or ch != 'n':
    print("\n\nPLEASE CHOOSE\n1 FOR ADMIN \n2 FOR CUSTOMER\n3 for EXIT:\n")

    choice = int(input("Enter your choice:"))
    if choice == 3:
        break
    if choice == 1:
        admin = input("USERNAME:")
        password = int(input("ENTER PASSWORD:"))
        if password == 1234:
            print("**************HELLO SIR, You logged in the systems successfully********.")
            print("__________________________________________________________________")
            print("Press 1 To Add Items in the shop")
            print("Press 2 To See Items in the shop")
            print("Press 3 to update the cost of any item")
            print("Press 4 to add varieties of cakes in the shop")
            print("Press 5 tp add workers in the shop")
            print("Press 6 to see workers")
            print("Press 7 to update salary of any worker:")

            c = int(input('Enter your choice'))
            if c == 1:
                def add():
                    sno = int(input("Enter sno"))
                    product1 = input("enter product name")
                    cost = int(input("Enter the cost"))
                    d1 = (sno, product, cost)
                    s1 = 'insert into cs values(%s,%s,%s)'
                    cur.execute(s1, d1)
                    con.commit()
                    print('______________________________________Items added in the shop________________')


                add()

            elif c == 2:
                def items():
                    print("Items in the shop:")
                    sql = "select*from cs"
                    cur.execute(sql)
                    res = cur.fetchall()
                    t = (['serial_no', 'products', 'cost'])
                    for serial_no, products, cost in res:
                        print(serial_no, ":", "\t", products, ":\t\t", 'cost', cost)


                items()


            elif c == 3:
                def money():
                    sno = input("Enter the sno of product:")
                    n_cost = input("Enter the Rupees to be added:")
                    cur.execute("update cs set cost-cost+" + n_cost + " where sno=" + sno + ';')
                    con.commit()
                    print("TABLE AFTER UPDATION:")
                    sq = "select from cs"
                    cur.execute(sq)
                    res = cur.fetchall()
                    t = (['sno', 'products', 'cost'])
                    for sno, products, cost in res:
                        print(sno, ":", "\t", products, ":", "\t", 'Cost', cost)


                money()

            elif c == 4:
                def variety():
                    sno - input("Enter sno:")
                    varieties = input("Enter variety:")
                    d2 = (sno, varieties)
                    s2 = 'insert into vip values (%s,%s)'
                    cur.execute(s2, d2)
                    con.commit()


                variety()


            elif e == 5:
                def ad():
                    sno = int(input("Enter sno:"))
                    sy = 'insert into worker values (%s, %s,%s)'
                    cur.execute(sy, dx)
                    emp = input("Enter name:")
                    salary = int(input("Enter the salary:"))
                    dx = (sno, emp, salary)
                    sy = 'insert into worker values (%s, %s,%s)'
                    cur.execute(sy, dx)
                    con.commit()
                    print('....................WORKERS IN SHOP.............')


                ad()


            elif c == 6:
                def workers():
                    print("Workers in the shop:")
                    sql = "select from worker"
                    cur.execute(sql)
                    res = cur.fetchall()
                    t = (['serial_no', 'name', 'salary'])
                    for serial_no, name, salary in res:
                        print(serial_no, ":", "\t", name, ":", "\t", "cost", salary)


                workers()

            elif c == 7:
                def up():
                    print("Choose 1 to increse the salary:")
                    print("Choose 2 to decrease:")
                    name = input("Enter the name of EMPLOYEE:")
                    n_salary = input("Enter the Rupees to be added:")
                    sig = int(input("Enter choice(1/2):"))

                    if sig == 1:
                        cur.execute("update worker set salary=salary+" + n_salary + " where name=" + name + ';')
                        con.commit()
                        print("TABLE AFTER UPDATION:")
                        sq = "select*from worker"
                        cur.execute(sq)
                        res = cur.fetchall()
                        t = (['sno', 'name', 'salary'])
                        for sno, name, salary in res:
                            print(sno, ":", "\t", name, ":", "\t", salary)
                    if sig == 2:
                        cur.execute("update worker set salary salary-" + n_salary + " where name=" + nan)
                        con.commit()
                        print("TABLE AFTER UPDATION:")
                        sq = "select*from worker"
                        cur.execute(sq)
                        res - cur.fetchall()
                        t = (['sno', 'name', 'salary'])
                        for sno, name, salary in res:
                            print(sno, ":", "\t", name, ":", "\t", salary)


                up()


            else:
                print("Sorry you have entered the worng choice")
        else:
            print("''''''''''''''''''''''''''''''''WRONG PASSWORD''''''''''''''''")

    elif choice == 2:
        name = input("Enter your name:")
        phone = int(input("Enter your phone number:"))
        print('Press 1 to see the MENU ', sep='......')
        print('Press 2 to order an item')
        c = int(input("Enter your choice:"))
        if c == 1:
            def items():
                print("Items in the shop:")
                sql = "select from es"
                cur.execute(sql)
                res = cur.fetchall()
                t = (['serial_no', 'products', 'cost'])
                for serial_no, products, cost in res:
                    print(serial_no, "", "\t", products, "", "\t", 'cost', cost)


            items()
        elif c == 2:
            print("What do you want to order?")
            sql = "select from cs"
            cur.execute(sql)
            res = cur.fetchall()
            t = (['serial_no', 'products', 'cost'])
            for serial_no, products, cost in res:
                print(serial_no, ":", "\t", products, ":", "\t", 'cost', cost)
                sql = "select sno from es"
                cur.execute(sql)
                res = cur.fetchall()
                print(res)
                l = []
                for i in range(len(res)):
                    l.append(res[i][0])
                d = int(input("Enter your Serial No of the Item to Buy:"))
                if d == 1:
                    def items():
                        print("Which cake do you want?")
                        kl = "select from vip"
                        cur.execute(kl)
                        srh - cur.fetchall()
                        f = (['sno', 'varieties'])
                        for sno, varieties in srh:
                            print(sno, "", "\t\t", varieties)
                        print("Choose which cake do you want?")
                        ck = int(input("Enter choice:"))
                        if ck == 1:
                            print("How much Quantity of Vaniella cake do you want?")
                            qty = int(input("Enter Qty."))
                            print("You have succesfully ordered your cake!!!\t")
                            cur.execute("select*from cs where products='cake'''';")
                            for i in cur:
                                e = i[2]
                                con.commit()
                            print("Total amount:", qty * c)
                            print("\n")
                            print("..............")
                            print("YOUR BILL")
                            print("_________________________")
                            print("Costumer's name:", name)
                            print("Contact no.:", phone)
                            print("Cake type:Vaniella")
                            print("No. of cakes:", qty)
                            print("Total amount:", qty * c)
                            print("@@@@@@@@@@@@THANK YOU FOR ORDERING THE ITEM@")
                            print("\t\t\t\t\t\t\t\t\t\tDate:", datetime.now())
                        if ck == 2:
                            print("How much Quantity of Chocalate cake do you want?")
                            qty = int(input("Enter Qty."))
                            print("You have succesfully ordered your cake!!!\t")
                            cur.execute("select from es where products='cake"";")
                            for i in cur:
                                L = i[2]
                            print("Total amount", qty * L)
                            print("\n")
                            print("....................................")
                            print("YOUR BILL")
                            print("________________________________________________")
                            print("Costumer's name:", name)
                            print("Contact no.:", phone)
                            print("Cake type:Chocalate")
                            print("No. of cakes:", qty)
                            print("Total amount:", qty * L)
                            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Thank you@@@@@@@@@@@@@@@@@@@@@")
                            print("\t\t\t\t\t\t\t\t\t\tDate:", datetime.now())
                        if ck == 3:
                            print("How much Quantity of Strawberry cake do you want?")
                            qty = int(input("Enter Qty."))
                            print("You have succesfully ordered your cake!!!\t")
                            cur.execute("select from es where products 'cake")
                            for i in cur:
                                N = i[2]
                            print("Total amount", qty * N)
                            print("\n")
                            print(".......................................")
                            print("YOUR BILL")
                            print("________________________________")
                            print("Costumer's name:", name)
                            print("Contact no.:", phone)
                            print("Cake type:Strawberry")
                            print("No. of cakes:", qty)
                            print("Total amount:", qty * N)
                            print("@@@@@@ @@@@THANK YOU FOR ORDERING THE ITEM@@@@@@@@@@@@@@@@@@")
                            print("\t\t\t\t\t\tDate:", datetime.now())
                        if ck == 4:
                            print("How much Quantity of Butter_scotch cake do you want?")
                            qty = int(input("Enter Qty."))
                            print("You have succesfully ordered your cake!!!\t:")
                            cur.execute("select*from es where products='cake"':')
                            for i in cur:
                                M = i[2]
                                print("Total amount", qty * M)
                                print("\n")
                                print(".............................")
                                print("YOUR BILL")
                                print("__________________________")
                                print("Costumer's name:", name)
                                print("Contact no.:", phone)
                                print("Cake type:Butter_scotch")
                                print("No. of cakes:", qty)
                                print("Total amount:", qty * M)
                                print("@@@@@@@@@@@@THANK YOU FOR ORDERING THE ITEM*********")
                                print("\t\t\t\t\t\t\t\t\t\tDate:", datetime.now())
                            items()
                        elif d == 2:
                            print("How much pastry do you want:")
                            past = int(input("enter your choice:"))
                            print("You have successfully ordered", past, " pastry")
                            cur.execute("select*from es where products='pastry"";")
                            for i in cur:
                                c = i[2]
                                print("Total amount =", past * c)
                                print("\n")
                                print(".........................")
                                print("YOUR BILL")
                                print("__________________________")
                                print("Costumer's name:", name)
                                print("Contact no.:", phone)
                                print("No. of pastry:", past)
                                print("Total amount:", past * c)
                                print("@@@@@@@@@@@THANK YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
                                print("\t\t\t\t\t\t\t\t\t\tDate:", datetime.now())
                        elif d == 3:
                            print("How much litres of milk do you want?")
                            mlk = int(input("Enter your choice:"))
                            print("You have successfully ordered", mlk, "L of milk.")
                            cur.execute("select from cs where products='milk"";")
                            for i in cur:
                                print("Total amount=", mlk * e)
                                print("\n")
                                print("..................")
                                print("YOUR BILL")
                                print("________________________")
                                print("Costumer's name:", name)
                                print("Contact no.:", phone)
                                print("Quantity of milk:", mlk)
                                print("Total amount", mlk * c)
                                print("@@@@@@@@@@@@THANK YOU FOR ORDERING THE ITEM@@@@")
                                print("\t\t\t\r\r\r\r\e\e\tDate", datetime.now())
                        elif d == 4:
                            print("How many packets (20gm) of butter do you want?")
                            but = int(input("Enter your choice:"))
                            print("You have successfully ordered", but, "packets of butter.")
                            cur.execute("select*from es where products=""butter"";")
                            for i in cur:
                                c = i[2]
                                print("Total amount:", but)
                                print("\n")
                                print("................................")
                                print("YOUR BILL")
                                print("________________________________")
                                print("Costumer's name:", name)
                                print("Contact no.:", phone)
                                print("Quantity of butter:", but)
                                print("Total amount:", but * c)
                                print("@@@@@@@@@@@@THANK YOU FOR ORDERING THE ITEM@@@@@@@@@@@")
                                print("\t\t\t\t\t\t\t\t\t\tDate:", datetime.now())

                        elif d == 5:
                            print("How much cheese(in Kg)do you want?")
                            chs = int(input("Enter your choice:"))
                            print("You have successfully ordered", chs, "Kg of cheese.")
                            cur.execute("select from es where products='cheese"";")
                            for i in cur:
                                c = i[2]
                                print("Total amount:", chs * c)
                                print("\n")
                                print(".........................")
                                print("YOUR BILL")
                                print("_____________________________")
                                print("Costumer's name:", name)
                                print("Contact no.:", phone)
                                print("Quantity of cheese:", chs)
                                print("Total amount:", chs * c)
                                print("@@@@@@ @@@@@@@@@@ THANK YOU FOR ORDERING THE ITEMS@@@@")
                                print("\t t\t\tDate:", datetime.now())
                        elif d in 1:
                            qty = int(input("Enter Qty."))
                            print("You have succesfully ordered your Selected Item!!!\t:")
                            cur.execute("select * from es where sno=" + str(d))
                            for i in cur:
                                L = i[2]
                                print("Total amount", qty * L)
                                print("\n")
                                print(".....................")
                                print("YOUR BILL")
                                print("______________________")
                                print("Costumer's name:", name)
                                print("Contact no.:", phone)
                                print("Quantity:", qty)
                                print("Total amount:", qty * L)
                                print("@@@@@@@@@@@@THANK YOU FOR ORDERING THE ITEM@@@")
                                print("\t\t\t\t t\t\t\t\tDate:", datetime.now())
                        else:
                            print("Wrong Input")

                else:
                    print("\t\t\t\t\t\t*******************************Wrong Password***************")
                    ch = input("DO YOU WANT TO CONTINUE (Y/N)?")
                    if ch == 'n' or ch == "N":
                        exit()
