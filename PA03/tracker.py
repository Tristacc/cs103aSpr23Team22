from transactions import Transaction
import sys


def usage():
    print('''usage:
            tracker add [item#] [amount] [category] [date] [description]
            tracker show 
            tracker delete [item#]
            tracker summarize-by-date
            tracker summarize-by-month 
            tracker summarize-by-year 
            tracker summarize-by-category 
            '''
            )

#---------------------------------methods from Trista -----------------------------------
def showTable(items, category: bool):
    if len(items)==0:
        print('no transactions to print')
        return
    print('\n')
    if category:
        print("%-10s %-10s"%('amount','category'))
    else:
        print("%-10s %-10s %-10s %-6s %-5s"%('item#','amount','category','date','description'))
    print('-'*70)
    for item in items:
        values = tuple(item.values())
        if category:
            print("%-10d %-10s"% ( values[1], values[2]))
        else:
            print("%-10d %-10d %-10s %04s %10s"
                  % ( values[1], values[2], values[3], values[4],"  "+values[5]))
#-----------------------------end of methods from Trista -----------------------------------

#---------------------------------methods from Kaiyu--------------------------------------
def showDate(items, str):
    if len(items)==0:
        print('no transactions to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-10s"%(str,'item#','amount','category','description'))
    print('-'*70)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10s %-10s %10s %10s"
              % ( values[1], values[2], values[3], values[4],"  "+values[5]))
#-----------------------------end of methods from Kaiyu------------------------------------

def process_args(arglist):
    #---------------------------------methods from Trista -----------------------------------
    tracker = Transaction()
    if arglist==[] or arglist==["menu"]:
        usage()
    elif arglist[0]=="show":
        showTable(tracker.show_transactions(), False)
    elif arglist[0]=='add':
        if len(arglist)!=6:
            print(len(arglist))
            print("more information needed")
            usage()
        else:
            userInput = {'item_num':arglist[1],'amount':arglist[2],
                         'category':arglist[3], 'date':arglist[4],
                         'description':arglist[5]}
            tracker.add(userInput)
    elif arglist[0] =='delete':
        if len(arglist)!=2:
            print("please enter the item#")
            usage()
        else:
            userInput = {'item_num':arglist[1]}
            tracker.delete(userInput)
    #-----------------------------end of methods from Trista -----------------------------------
    
    #---------------------------------methods from Kaiyu----------------------------------------
    elif arglist[0] == "summarize-by-date":
        showDate(tracker.summarize_by_date(),'date')
    elif arglist[0] == "summarize-by-month":
        showDate(tracker.summarize_by_month(),'month')
    #-----------------------------end of methods from Kaiyu------------------------------------


    #---------------------------------methods from Chenchuhui----------------------------------------
    elif arglist[0] == "summarize-by-year":
        showDate(tracker.summarize_by_year(),'year')
    elif arglist[0] == "summarize-by-category":
        showTable(tracker.summarize_by_category(), True)
    #-----------------------------end of methods from Chenchuhui--------------------------------------

    #--------------------method from Ran---------------------
    elif arglist[0] == "select-by-amount-range":
        if len(arglist)!=3:
            print("please enter the lower and upper bound for amount")
        else:
            showTable(tracker.select_by_amount_range(arglist[1],arglist[2]), False)
    #--------------------end of method from Ran---------------------
        

def toplevel():
    if len(sys.argv)==1:
        usage()
        args = []
        while args!=['']:
            args = input("tracker> ").split(' ')
            if args[0]=='add':
                args = ['add',args[1],args[2],args[3],args[4]," ".join(args[5:])]
            if args[0]=='delete':
                args = ['delete',args[1]]
            #--------------------quit method from Ran---------------------
            if args[0]=='quit':
                return
            #--------------------end of quit method from Ran---------------------
            process_args(args)
            print('-'*70+'\n')
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*70+'\n')

if __name__ == "__main__":
    toplevel()