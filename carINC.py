'''

'''
import mysql.connector as mc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

username = str(input('Enter Username ::'))
password = str(input('Enter Password ::'))

mdb = mc.connect(host = 'localhost',user = 'root',passwd = 'shubh',database='cars_inc')
cur = mdb.cursor()

def Company_profit():    
    print('Company_Total_Profit')
    cur.execute("SELECT * FROM company_profit")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Branch_name','Expenses','Earnings','Total'])
    print(val)
    print()
    print('Company earnings')
    print(sum(val['Earnings']))
    print()
    print('Company expenses')
    print(sum(val['Expenses']))
    print()    
    print('Company total proft')
    print(sum(val['Total']))
    print()
    #Update from Ludhiana branch
    cur.execute('Update company_profit set Expenses = (select sum(Expenses) from ldh_branch_profit) where Branch_name = \'Ludhiana\'')          
    mdb.commit()
    cur.execute('Update company_profit set Earnings = (select sum(Earnings) from ldh_branch_profit) where Branch_name = \'Ludhiana\'')          
    mdb.commit()
    cur.execute('Update company_profit set Total = (select sum(Total_profit) from ldh_branch_profit) where Branch_name = \'Ludhiana\'')          
    mdb.commit()
    #Update from Jalandhar branch
    cur.execute('Update company_profit set Expenses = (select sum(Expenses) from jal_branch_profit) where Branch_name = \'Jalandhar\'')          
    mdb.commit()
    cur.execute('Update company_profit set Earnings = (select sum(Earnings) from jal_branch_profit) where Branch_name = \'Jalandhar\'')          
    mdb.commit()
    cur.execute('Update company_profit set Total = (select sum(Total_profit) from jal_branch_profit) where Branch_name = \'Jalandhar\'')          
    mdb.commit()
    #Update from Patiala branch
    cur.execute('Update company_profit set Expenses = (select sum(Expenses) from pat_branch_profit) where Branch_name = \'Patiala\'')          
    mdb.commit()
    cur.execute('Update company_profit set Earnings = (select sum(Earnings) from pat_branch_profit) where Branch_name = \'Patiala\'')          
    mdb.commit()
    cur.execute('Update company_profit set Total = (select sum(Total_profit) from pat_branch_profit) where Branch_name = \'Patiala\'')          
    mdb.commit()
    #Update from Amritsar branch
    cur.execute('Update company_profit set Expenses = (select sum(Expenses) from asr_branch_profit) where Branch_name = \'Amritsar\'')          
    mdb.commit()
    cur.execute('Update company_profit set Earnings = (select sum(Earnings) from asr_branch_profit) where Branch_name = \'Amritsar\'')          
    mdb.commit()
    cur.execute('Update company_profit set Total = (select sum(Total_profit) from asr_branch_profit) where Branch_name = \'Amritsar\'')          
    mdb.commit()
    #Update from Bathinda branch
    cur.execute('Update company_profit set Expenses = (select sum(Expenses) from bth_branch_profit) where Branch_name = \'Bathinda\'')          
    mdb.commit()
    cur.execute('Update company_profit set Earnings = (select sum(Earnings) from bth_branch_profit) where Branch_name = \'Bathinda\'')          
    mdb.commit()
    cur.execute('Update company_profit set Total = (select sum(Total_profit) from bth_branch_profit) where Branch_name = \'Bathinda\'')          
    mdb.commit()
    cur.execute("SELECT total FROM company_profit")
    total = cur.fetchall()
    total = np.array(total)
    total = total.flatten()
    cur.execute("SELECT branch_name FROM company_profit")
    branch = cur.fetchall()
    branch = np.array(branch)
    branch = branch.flatten()
    plt.bar(branch,total)
    plt.xlabel('Branches')
    plt.ylabel('Profits')
    plt.title('Branches profits')
    plt.show()
    print('press 1 To make changes')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Branch_name::'))
            a3 = str(input('Expenses::'))
            a4 = str(input('Earnings::'))
            a5 = str(input('Total::'))
            print()
            cur.execute('insert into company_profit values('+a1+',\''+a2+'\','+a3+','+a4+','+a5+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from company_profit where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Branch_name','\n',
                  'press 3 To update Expenses','\n',
                  'press 4 To update Earnings','\n',
                  'press 5 To update Total','\n',
                  'press 6 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Branch_name::'))
                cur.execute('update company_profit set S_No = '+d1+' where Branch_name = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Branch_name::'))
                d5 = str(input('S_No.::'))
                cur.execute('update company_profit set Branch_name = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Expenses::'))
                d8 = str(input('S_No.::'))
                cur.execute('update company_profit set Expenses = '+d7+' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Earnings::'))
                d11 = str(input('S_No.::'))
                cur.execute('update company_profit set Earnings = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Total::'))
                d14 = str(input('S_No.::'))
                cur.execute('update company_profit set Total = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuCEO()

def Branch_profit_LDH():
    print('Branch_Total_Profit(LDH)')
    cur.execute("SELECT * FROM LDH_Branch_profit")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','Expenses','Earnings','Total'])
    print(val)
    print()
    print('Branch earnings')
    print(sum(val['Earnings']))
    print()
    print('Branch expenses')
    print(sum(val['Expenses']))
    print()    
    print('Branch total proft')
    print(sum(val['Total']))
    print()
    cur.execute("SELECT total_profit FROM ldh_branch_profit;")
    total = cur.fetchall()
    total = np.array(total)
    total = total.flatten()
    cur.execute("SELECT car FROM ldh_branch_profit;")
    car = cur.fetchall()
    car = np.array(car)
    car = car.flatten()
    plt.figure(figsize = (8,5))
    plt.bar(car,total)
    plt.xlabel('Car')
    plt.ylabel('Profits')
    plt.title('Ludhiana Branch')
    plt.show()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('Expenses::'))
            a5 = str(input('Earnings::'))
            a6 = str(input('Total::'))
            print()
            cur.execute('insert into LDH_Branch_profit values('+a1+',\''+a2+'\',\''+a3+'\','+a4+','+a5+','+a6+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from LDH_Branch_profit where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update Expenses ','\n',
                  'press 5 To update Earnings ','\n',
                  'press 6 To update Total','\n',
                  'press 7 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Car::'))
                cur.execute('update LDH_Branch_profit set S_No = '+d1+' where Car = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update LDH_Branch_profit set Company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update LDH_Branch_profit set Car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Expenses::'))
                d11 = str(input('S_No.::'))
                cur.execute('update LDH_Branch_profit set Expenses = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Earnings::'))
                d14 = str(input('S_No.::'))
                cur.execute('update LDH_Branch_profit set Earnings = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                d16 = str(input('Total::'))
                d17 = str(input('S_No.::'))
                cur.execute('update LDH_Branch_profit set Total_profit = '+d16+' where S_No = '+d17+';')
                mdb.commit()
                print()
            elif d == 7:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:    
        print()
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    if username == 'Dennis' and password == 'dennis07':
        MainMenuCEO()
    else:
        MainMenuManager()
        
def Branch_profit_JAL():
    print('Branch_Total_Profit(JAL)')
    cur.execute("SELECT * FROM JAL_Branch_profit")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','Expenses','Earnings','Total'])
    print(val)
    print()
    print('Branch earnings')
    print(sum(val['Earnings']))
    print()
    print('Branch expenses')
    print(sum(val['Expenses']))
    print()    
    print('Branch total proft')
    print(sum(val['Total']))
    print()
    cur.execute("SELECT total_profit FROM jal_branch_profit;")
    total = cur.fetchall()
    total = np.array(total)
    total = total.flatten()
    cur.execute("SELECT car FROM jal_branch_profit;")
    car = cur.fetchall()
    car = np.array(car)
    car = car.flatten()
    plt.figure(figsize = (10,5))
    plt.bar(car,total)
    plt.xlabel('Car')
    plt.ylabel('Profits')
    plt.title('Jalandhar Branch')
    plt.show()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('Expenses::'))
            a5 = str(input('Earnings::'))
            a6 = str(input('Total::'))
            print()
            cur.execute('insert into JAL_Branch_profit values('+a1+',\''+a2+'\',\''+a3+'\','+a4+','+a5+','+a6+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from JAL_Branch_profit where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update Expenses','\n',
                  'press 5 To update Earnings','\n',
                  'press 6 To update Total','\n',
                  'press 7 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Car::'))
                cur.execute('update JAL_Branch_profit set S_No = '+d1+' where Car = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update JAL_Branch_profit set Company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update JAL_Branch_profit set Car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Expenses::'))
                d11 = str(input('S_No.::'))
                cur.execute('update JAL_Branch_profit set Expenses = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Earnings::'))
                d14 = str(input('S_No.::'))
                cur.execute('update JAL_Branch_profit set Earnings = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                d16 = str(input('Total::'))
                d17 = str(input('S_No.::'))
                cur.execute('update JAL_Branch_profit set Total_profit = '+d16+' where S_No = '+d17+';')
                mdb.commit()
                print()
            elif d == 7:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuCEO()

def Branch_profit_PAT():
    print('Branch_Total_Profit(PAT)')
    cur.execute("SELECT * FROM PAT_Branch_profit")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','Expenses','Earnings','Total'])
    print(val)
    print()
    print('Branch earnings')
    print(sum(val['Earnings']))
    print()
    print('Branch expenses')
    print(sum(val['Expenses']))
    print()    
    print('Branch total proft')
    print(sum(val['Total']))
    print()
    cur.execute("SELECT total_profit FROM pat_branch_profit;")
    total = cur.fetchall()
    total = np.array(total)
    total = total.flatten()
    cur.execute("SELECT car FROM pat_branch_profit;")
    car = cur.fetchall()
    car = np.array(car)
    car = car.flatten()
    plt.figure(figsize = (8,5))
    plt.bar(car,total)
    plt.xlabel('Car')
    plt.ylabel('Profit')
    plt.title('Patiala Branch')
    plt.show()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('Expenses::'))
            a5 = str(input('Earnings::'))
            a6 = str(input('Total::'))
            print()
            cur.execute('insert into PAT_Branch_profit values('+a1+',\''+a2+'\',\''+a3+'\','+a4+','+a5+','+a6+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from PAT_Branch_profit where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update Expenses','\n',
                  'press 5 To update Earnings','\n',
                  'press 6 To update Total','\n',
                  'press 7 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Car::'))
                cur.execute('update PAT_Branch_profit set S_No = '+d1+' where Car = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update PAT_Branch_profit set Company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update PAT_Branch_profit set Car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Expenses::'))
                d11 = str(input('S_No.::'))
                cur.execute('update PAT_Branch_profit set Expenses = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Earnings::'))
                d14 = str(input('S_No.::'))
                cur.execute('update PAT_Branch_profit set Earnings = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                d16 = str(input('Total::'))
                d17 = str(input('S_No.::'))
                cur.execute('update PAT_Branch_profit set Total_profit = '+d16+' where S_No = '+d17+';')
                mdb.commit()
                print()
            elif d == 7:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuCEO()

def Branch_profit_ASR():
    print('Branch_Total_Profit(ASR)')
    cur.execute("SELECT * FROM ASR_Branch_profit")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','Expenses','Earnings','Total'])
    print(val)
    print()
    print('Branch earnings')
    print(sum(val['Earnings']))
    print()
    print('Branch expenses')
    print(sum(val['Expenses']))
    print()    
    print('Branch total proft')
    print(sum(val['Total']))
    print()
    cur.execute("SELECT total_profit FROM asr_branch_profit;")
    total = cur.fetchall()
    total = np.array(total)
    total = total.flatten()
    cur.execute("SELECT car FROM asr_branch_profit;")
    car = cur.fetchall()
    car = np.array(car)
    car = car.flatten()
    plt.figure(figsize = (10,5))
    plt.bar(car,total)
    plt.xlabel('Car')
    plt.ylabel('Profit')
    plt.title('Amritsar Branch')
    plt.show()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('Expenses::'))
            a5 = str(input('Earnings::'))
            a6 = str(input('Total::'))
            print()
            cur.execute('insert into ASR_Branch_profit values('+a1+',\''+a2+'\',\''+a3+'\','+a4+','+a5+','+a6+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from ASR_Branch_profit where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update Expenses','\n',
                  'press 5 To update Earnings','\n',
                  'press 6 To update Total','\n',
                  'press 7 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Car::'))
                cur.execute('update ASR_Branch_profit set S_No = '+d1+' where Car = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update ASR_Branch_profit set Company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update ASR_Branch_profit set Car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Expenses::'))
                d11 = str(input('S_No.::'))
                cur.execute('update ASR_Branch_profit set Expenses = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Earnings::'))
                d14 = str(input('S_No.::'))
                cur.execute('update ASR_Branch_profit set Earnings = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print(val)
                print()
            elif d == 6:
                d16 = str(input('Total::'))
                d17 = str(input('S_No.::'))
                cur.execute('update ASR_Branch_profit set Total_profit = '+d16+' where S_No = '+d17+';')
                mdb.commit()
                print()
            elif d == 7:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuCEO()

def Branch_profit_BTH():
    print('Branch_Total_Profit(BTH)')
    cur.execute("SELECT * FROM BTH_Branch_profit")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','Expenses','Earnings','Total'])
    print(val)
    print()
    print('Branch earnings')
    print(sum(val['Earnings']))
    print()
    print('Branch expenses')
    print(sum(val['Expenses']))
    print()    
    print('Branch total proft')
    print(sum(val['Total']))
    print()
    cur.execute("SELECT total_profit FROM bth_branch_profit;")
    total = cur.fetchall()
    total = np.array(total)
    total = total.flatten()
    cur.execute("SELECT car FROM bth_branch_profit;")
    car = cur.fetchall()
    car = np.array(car)
    car = car.flatten()
    plt.figure(figsize = (9,5))
    plt.bar(car,total)
    plt.xlabel('Car')
    plt.ylabel('Profit')
    plt.title('Bathinda Branch')
    plt.show()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('Expenses::'))
            a5 = str(input('Earnings::'))
            a6 = str(input('Total::'))
            print()
            cur.execute('insert into BTH_Branch_profit values('+a1+',\''+a2+'\',\''+a3+'\','+a4+','+a5+','+a6+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from BTH_Branch_profit where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update Expenses','\n',
                  'press 5 To update Earnings','\n',
                  'press 6 To update Total','\n',
                  'press 7 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Car::'))
                cur.execute('update BTH_Branch_profit set S_No = '+d1+' where Car = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update BTH_Branch_profit set Company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update BTH_Branch_profit set Car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Expenses::'))
                d11 = str(input('S_No.::'))
                cur.execute('update BTH_Branch_profit set Expenses = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Earnings::'))
                d14 = str(input('S_No.::'))
                cur.execute('update BTH_Branch_profit set Earnings = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                d16 = str(input('Total::'))
                d17 = str(input('S_No.::'))
                cur.execute('update BTH_Branch_profit set Total_profit = '+d16+' where S_No = '+d17+';')
                mdb.commit()
                print()
            elif d == 7:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuCEO()

def Employee_Status():
    print('Employee Status')
    cur.execute("SELECT * FROM employee_status")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Name','Expenses','Earnings','Total'])
    print(val)
    print()
    print('Employees earnings')
    print(sum(val['Earnings']))
    print()
    print('Employees expenses')
    print(sum(val['Expenses']))
    print()    
    print('Employees total proft')
    print(sum(val['Total']))
    print()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Name::'))
            a3 = str(input('Expenses::'))
            a4 = str(input('Earnings::'))
            a5 = str(input('Total::'))
            print()
            cur.execute('insert into employee_status values('+a1+',\''+a2+'\','+a3+','+a4+','+a5+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from employee_status where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Name','\n',
                  'press 3 To update Expenses','\n',
                  'press 4 To update Earnings','\n',
                  'press 5 To update Total','\n',
                  'press 6 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Name::'))
                cur.execute('update employee_status set S_No = '+d1+' where Name = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Name::'))
                d5 = str(input('S_No.::'))
                cur.execute('update employee_status set Name = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Expenses::'))
                d8 = str(input('S_No.::'))
                cur.execute('update employee_status set Expenses = '+d7+' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Earnings::'))
                d11 = str(input('S_No.::'))
                cur.execute('update employee_status set Earnings = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Total::'))
                d14 = str(input('S_No.::'))
                cur.execute('update employee_status set Total = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuManager()
    
def Purchases():
    print('Purchases')
    cur.execute("SELECT * FROM purchases")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','Seller_Name','Contact','Price'])
    print(val)
    print()
    print('Expenditure made')
    print(sum(val['Price']))
    print()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('Seller_name::'))
            a5 = str(input('Contact::'))
            a6 = str(input('Price::'))
            print()
            cur.execute('insert into purchases values('+a1+',\''+a2+'\',\''+a3+'\',\''+a4+'\','+a5+','+a6+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from purchases where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update Seller_name','\n',
                  'press 5 To update Contact','\n',
                  'press 6 To update Price','\n',
                  'press 7 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Contact::'))
                cur.execute('update purchases set S_No = '+d1+' where Contact = '+d2+';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update purchases set company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update purchases set car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Seller_name::'))
                d11 = str(input('S_No.::'))
                cur.execute('update purchases set seller_name = \''+d10+'\' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Contact::'))
                d14 = str(input('S_No.::'))
                cur.execute('update purchases set Contact = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                d16 = str(input('Price::'))
                d17 = str(input('S_No.::'))
                cur.execute('update purchases set price = '+d16+' where S_No = '+d17+';')
                mdb.commit()
                print()
            elif d == 7:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuEmployee()

def Sales():
    print('Sales')
    cur.execute("SELECT * FROM sales")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','Purchaser','Contact','Price'])
    print(val)
    print()
    print('Profit from selling')
    print(sum(val['Price']))
    print()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('Purchaser::'))
            a5 = str(input('Contact::'))
            a6 = str(input('Price::'))
            print()
            cur.execute('insert into Sales values('+a1+',\''+a2+'\',\''+a3+'\',\''+a4+'\','+a5+','+a6+');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from sales where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update Purchaser','\n',
                  'press 5 To update Contact','\n',
                  'press 6 To update Price','\n',
                  'press 7 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Contact::'))
                cur.execute('update sales set S_No = '+d1+' where contact = '+d2+';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update sales set company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update sales set car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('Purchaser::'))
                d11 = str(input('S_No.::'))
                cur.execute('update sales set purchaser = \''+d10+'\' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                d13 = str(input('Contact::'))
                d14 = str(input('S_No.::'))
                cur.execute('update sales set Contact = '+d13+' where S_No = '+d14+';')
                mdb.commit()
                print()
            elif d == 6:
                d16 = str(input('Price::'))
                d17 = str(input('S_No.::'))
                cur.execute('update sales set price = '+d16+' where S_No = '+d17+';')
                mdb.commit()
                print()
            elif d == 7:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuEmployee()

def Stock():
    print('Stock')
    cur.execute("SELECT * FROM stock")
    val = cur.fetchall()
    val = pd.DataFrame(val , columns = ['S_No','Company','Car','No_of_cars'])
    print(val)
    print()
    print('Total No of cars available')
    print(sum(val['No_of_cars']))
    print()
    print('press 1 To make changes','\n')
    print('press 2 To exit')
    A = int(input('Enter::'))
    if A == 1:
        print('press 1 To add value','\n',
              'press 2 To delete value','\n',
              'press 3 To update value','\n',
              'press 4 To Exit')
        B = int(input('Enter::'))           #adding values(rows)
        if B == 1:
            a1 = str(input('S_No.::'))
            a2 = str(input('Company::'))
            a3 = str(input('Car::'))
            a4 = str(input('No_of_cars::'))
            print()
            cur.execute('insert into Stock values('+a1+',\''+a2+'\',\''+a3+'\',\''+a4+'\');')
            mdb.commit()
            print()
        elif B == 2:                        #deleting values(rows)
            b1 = str(input('S_No::'))
            cur.execute('delete from stock where S_No = '+b1+';')
            mdb.commit()
            print()
        elif B == 3:                        #updating values
            print('press 1 To update S_No','\n',
                  'press 2 To update Company','\n',
                  'press 3 To update Car','\n',
                  'press 4 To update No_of_cars','\n',
                  'press 5 To exit')
            d = int(input('Enter::'))
            if d == 1:
                d1 = str(input('S_No.::'))
                d2 = str(input('Car::'))
                cur.execute('update stock set S_No = '+d1+' where car = \''+d2+'\';')
                mdb.commit()
                print()
            elif d == 2:
                d4 = str(input('Company::'))
                d5 = str(input('S_No.::'))
                cur.execute('update stock set company = \''+d4+'\' where S_No = '+d5+';')
                mdb.commit()
                print()
            elif d == 3:
                d7 = str(input('Car::'))
                d8 = str(input('S_No.::'))
                cur.execute('update stock set car = \''+d7+'\' where S_No = '+d8+';')
                mdb.commit()
                print()
            elif d == 4:
                d10 = str(input('No_of_cars::'))
                d11 = str(input('S_No.::'))
                cur.execute('update stock set No_of_cars = '+d10+' where S_No = '+d11+';')
                mdb.commit()
                print()
            elif d == 5:
                print()
            else:
                print('Invalid input')
        elif B == 4:
            print()
        else:
            print('Invalid input')
    elif A == 2:
        print()        
    else:
        print('Invalid input')
    input('Press Enter to return to Main menu')
    MainMenuEmployee()    
    
if username=='Dennis' and password=='dennis07':             #CEO ID
    print('\n','CARS_INC')
    print('\n','Welcome Sir','\n')
    def MainMenuCEO():
        print('Enter 1 to see Company Total Profit','\n')
        print('Enter 2 to see Branch Profit','\n')
        print('Enter 3 to exit')
        while True:
            try:
                C = int(input('Enter::'))
                print()
                if C == 1:
                    Company_profit()
                    break
                elif C == 2:
                    print('Branches','\n',
                          'Jalandhar','\n',
                          'Patiala','\n',
                          'Ludhiana','\n',
                          'Amritsar','\n',
                          'Bathinda')
                    brn = str(input('Enter Branch name::'))
                    if brn == 'Jalandhar':
                        Branch_profit_JAL()
                    elif brn == 'Patiala':
                        Branch_profit_PAT()
                    elif brn == 'Ludhiana':
                        Branch_profit_LDH()
                    elif brn == 'Amritsar':
                        Branch_profit_ASR()
                    elif brn == 'Bathinda':
                        Branch_profit_BTH()
                    else:
                        print('Invalid Input')
                    break
                elif C == 3:
                    print()
                    break
                else:
                    print('Invalid input')
                    MainMenuCEO()
            except ValueError:
                print('Invalid input. Try again')
        exit
    MainMenuCEO()

elif username == 'Keith' and password == 'keith27':       #Branch manager ID
    print('\n','CARS_INC')
    print('\n','Welcome Keith','\n')
    def MainMenuManager():
        print('Enter 1 to see Employee Status','\n')
        print('Enter 2 to see Branch Profit','\n')
        print('Enter 3 to exit','\n')
        while True:
            try:
                M = int(input('Enter::'))
                print()
                if M == 1:
                    Employee_Status()
                    break
                elif M == 2:
                    Branch_profit_LDH()
                    break
                elif M == 3:
                    print()
                    break
                else:
                    print('Invalid input')
                    MainMenuManager()
            except ValueError:
                print('Invalid input. Try again')
        exit
    MainMenuManager()

elif username == 'Ryan' and password == 'ryan16':         #Branch employee ID
    print('\n','CARS_INC')
    print('\n','Welcome Ryan','\n')
    def MainMenuEmployee():
        print('Enter 1 to see Purchases','\n')
        print('Enter 2 to see Stock','\n')
        print('Enter 3 to see Sales','\n')
        print('Enter 4 to exit')
        while True:
            try:    
                E = int(input('Enter::'))
                if E == 1:
                    Purchases()
                    break
                elif E == 2:
                    Stock()
                    break
                elif E == 3:
                    Sales()
                    break
                elif E == 4:
                    print()
                    break
                else:
                    print('Invalid input. Try again')
                    MainMenuEmployee()
            except ValueError:
                print('Invalid input. Try again')
        exit
    MainMenuEmployee()
else:
    print('Invalid username or password')
