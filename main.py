import mysql.connector 
my_database = mysql.connector.connect(host = 'localhost' , user = 'root' , password = 'Up63!8970' , database  = 'bank_manag_sys_proj1')

def OpenAcc():
    n = input("Enter the Full Name - ")
    acc = input("Enter the Account Number - ")
    dob = input("Enter the date of birth - ")
    addr = input("Enter the Address - ")
    cn = input("Enter the Phone Number - ")
    ob = int(input("Enter the Opening Balance - "))
    data_account = ( n , acc , dob , addr , cn , ob )
    data_amount = ( n , acc , ob ) 

    sql_account = 'insert into account values (n , acc, dob , addr , cn , ob )'
    sql_amount = 'Insert into amount values(n , acc,ob )'

    my_database.cursor()
    x_account = (sql_account , data_account)
    x_amount = (sql_amount , sql_amount)

    my_database.commit()
    print("DATA ENTERED SUCCESSFULLY ... ")

    main()

def DepositAmt():
    amount = input("Enter the amount you want to deposit : ")
    acc = input("Enter the Account Number : ")
    quer1 = 'select balance from amount where AccNum = %s'
    data1 = (acc , )
    x = mydb.cursor()
    x.execute(quer1 , data1)
    result1 = x.fetchone()
    f_result = result1[0] + amount
    sql_update_amt = ('update amount set balance where AccNum = %s')
    result2 = (f_result , acc)
    x.execute(sql_update_amt , result2)
    my_database.commit()
    main()

def WithdrawAmt():
    amount = input("Enter the amount you want to withdraw : ")
    acc = input("Enter the Account Number : ")
    quer1 = 'select balance from amount where AccNum = %s'
    data1 = (acc , )
    x = mydb.cursor()
    x.execute(quer1 , data1)
    result1 = x.fetchone()
    f_result = result1[0] - amount
    sql_update_amt = ('update amount set balance where AccNum = %s')
    result2 = (f_result , acc)
    x.execute(sql_update_amt , result2)
    my_database.commit()
    main()

def BalEnq():
    acc = input("Enter the Account Number : ")
    a = 'select * from amount where AccNum = %s'
    data = (acc, )
    x = my_database.cursor()
    x.execute(acc, data)
    result = x.fetchone()
    print("Balance for the account :" , ac , "is " , result[-1])
    main()

def DispCustDe():
    acc = input("Enter the Account Number : ")
    a = 'select * from account where AccNum = %s'
    data = (acc, )
    x = my_database.cursor()
    x.execute(acc, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def CloseAcc():
    acc = input("Enter the Account Number : ")
    sql1 = 'delete from account where AccNum =%s'
    sql2 = 'delete from amount where AccNum = %s'
    data = (acc , )
    x = my_database.cursor()
    x.execute(sql1 , data)
    x.execute(sql2 , data)
    my_database.commit()


def main():
    
    print( '''
    1.  OPEN NEW ACCOUNT 
    2.  DEPOSIT AMOUNT 
    3.  WITHDRAW AMOUNT 
    4.  BALANCE ENQUIRY
    5.  DISPLAY CUSTOMER DETAILS
    6.  CLOSE A ACCOUNT''')

    Choice = input(" Dear Customer , Enter the task you want to perform -- ")

    if (Choice == '1'):
        OpenAcc()

    elif ( Choice == '2'):
        DepsoitAmt()
    
    elif ( Choice == '3'):
        WithdrawAmt()

    elif (Choice=='4' ):
        BalEnq()

    elif( Choice == '5'):
        DispCustDe()

    elif (Choice == '6'):
        CloseAcc()

    else : 
        print("Invalid Entry , Please try again .. ")
        main()

main()