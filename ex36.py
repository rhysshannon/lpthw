from sys import exit

#activity - watcher list - need to work on this. 
def watchers():
    watchers_notify = input("Notify Account Watchers: y or n: ")
    if watchers_notify == 'y':
        print("note sent to account watchers")
        flag = input("flag order to managment: y or n?")
        if flag == 'y':
            print(""" who needs to be notified?:
            Enter:
            am - all account managers
            sm - sales management
            sd - sales director
            deals - deals desk
            pur - purchasing
            ship - warehouse
            cloud - cloud
            services - services
            credit - accounts receivable
            lead - leadership team
            exec - David Gage 
            exit - """)
            flag_who = input(":> ")
            if flag_who == "exit":
                prompt = input("Press any key to return to Start Menu")

            else:    
                print("you entered: "+flag_who+" type exit?")
                flag_who = input(":> ")
        elif flag == 'n':
            prompt = input("Press any key to return to Start Menu")

    else:
        prompt = input("Press any key to return to Start Menu")
    start_menu()
#activity - confirm
# def confirm():
 #   while confirm != 'y' or 'yes':
  #      print("please confirm work is completed by entering y or yes")
   #     confirm = input("> ")
    #    if confirm == 'y' or 'yes':
     #       start_menu()
      #  else:
       #     exit(0)
#activity = escelate
#call - to log a call - define function
def call():
    print("Please enter the following information as prompted:")
    call_account = input("Reseller: ")
    call_contact = input("Contact: ")
    call_actions = input("Actions: ")
    call_entry = ("NEW RECORD---\n""Account: "+ call_account+"\n"+"Contact: "+call_contact+"\n"+"Actions: "+call_actions+"\n")
    print(call_entry)
    call_file = open('ex36_calldb.txt','a+')
    call_file.write(call_entry)
    prompt_c = input()
    call_file.close()
    start_menu()    
#meeting - to log a meeting

 #   anote - to add an account note - done 
def anote():
    print("Please enter the following information as prompted:")
    anote_account = input("Reseller: ")
    anote_subject = input("Subject: ")
    anote_details = input("details: ")
    anote_entry = ("NEW RECORD---\nAccount: "+anote_account+"\n"+"Subject: "+anote_subject+"\n"+"Details: "+anote_details+"\n")
    anote_file = open('ex36_anotedb.txt','a+')
    anote_file.write(anote_entry)
    ptompt_an = input()
    anote_file.close()
    start_menu()
    
  #  order - to work on an order
#def order():
   # forcast -Forecast a deal
def forecast():
    print("Please enter the following information as prompted:")
    forecast_account = input("Reseller: ")
    forecast_dealname = input(" Deal Name: ")
    forecast_closedate = input("date to close: ")
    forecast_contact = input("Contact: ")
    forecast_vendor = input("Vendor: ")
    forecast_value = input("Value: $ ")
    forcast_GP = input("GP%: ")+"%"
    forecast_entry = ("NEW RECORD---\n"+forecast_dealname+" | Account: "+ forecast_account+" | "+"Contact: "+forecast_contact+"\n"+"Vendor: "+forecast_vendor+" | "+ forecast_value+ " @ "+ forcast_GP+"\n")
    forecast_file = open('ex36_forecastdb.txt','a+')
    forecast_file.write(forecast_entry)
    prompt_c = input()
    forecast_file.close()
    start_menu()    

   # commits - enter your commit forecast
def commits():
    print("Are you confiming the month(m) or quarter(q)")
    commits_month_quarter = input(">:")
    if commits_month_quarter == 'month' or "m":
        print("Enter Month:")
        commits_month = input(":> ")
        print("What is the revenue for "+ commits_month+"? ")
        commits_month_revenue = int(input(":>"))
        print("What is the GP?")
        commits_month_gp = int(input(":> "))
        print("confiming..."+ commits_month)
        print(f"Revenue: {commits_month_revenue} and GP of {commits_month_gp}%")
        commits_gp_value = (commits_month_revenue * commits_month_gp) / 100
        print(f"$ {str(commits_gp_value)}")
        prompt = input("press any key when ready to go back to start menu")
        start_menu()
    elif commits_month_quarter == "quarter" or "q":
        print("Enter Quarter:")
        commits_quarter = input(":> ")
        print("What is the revenue for "+ commits_month+"? ")
        commits_quarter_revenue = input(":>")
        print("What is the GP?")
        commits_quarter_gp = input(":> ")
        print("confiming..."+ commits_quarter)
        print(f"Revenue: {commits_quarter_revenue} and GP of {commits_quarter_gp}%")
        prompt = input("press any key when ready to go back to start menu")
        start_menu()
    else:
        prompt = input("press any key to return to start menu")
        start_menu()
#define list menu: this works really well. 
def list_menu():
    print(""" Review all items here by typing in the list name:
    call - call list 
    anote - account notes\n """ )
    choice = input(":> ")
    if choice == "call":
        calldb_list = open('ex36_calldb.txt','r')
        print(calldb_list.read())
        prompt = input("press anything when done")
        calldb_list.close()
    if choice == "anote":
        anote_listdb = open('ex36_anotedb.txt','r')
        print(anote_listdb.read())
        prompt = input("press anything when done")
        anote_listdb.close()
    if choice == "forecast":
        forecast_listdb = open('ex36_forecastdb.txt','r')
        print(forecast_listdb.read())
        prompt = input("press anything when done")
        forecast_listdb.close()
    else:
        print("close")
    prompt = input("return to start. press anything")
    start_menu()
    

#define start menu:
def start_menu():
    print(""" Hi I am Plonky Bear and I am here to help!
    type the following to do something:
    call - to log a call
    meeting - to log a meeting
    anote - to add an account note
    order - to work on an order
    forecast - Forecast a deal. 
    commits - enter your commit forecast
    list - takes you to list menu
    exit - Say bye to Plonky Bear
    """)
    choice = input("> ")

    if choice == "call":
        call()
    
    elif choice == "meeting":
        meeting()
    
    elif choice == "anote":
        anote()
    
    elif choice == "order":
        order()
    
    elif choice == "forecast":
        forecast()
    
    elif choice == "commits":
        commits()
    
    elif choice == "exit":
        exit(0)
    
    elif choice =="list":
        list_menu()

    
    else:
        print("try again moron \n\n")
    start_menu()



#start menu
start_menu()

