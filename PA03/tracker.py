
from transactions import Transaction
import sys


def usage():
    print('''usage:
            tracker add [item#] [amount] [category] [date] [description]
            tracker show 
            tracker delete [item#]
            tracker summarize-by-date
            tracker summatize-by-month 
            '''
            )
    
#---------------------------------methods from Trista -----------------------------------
def showTable(items):
    if len(items)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-6s %-5s"%('item#','amount','category','date','description'))
    print('-'*70)
    for item in items:
        values = tuple(item.values()) 
        print("%-10d %-10d %-10s %04s %10s"% ( values[1], values[2], values[3], values[4],"  "+values[5]))
#-----------------------------end of methods from Trista -----------------------------------

#---------------------------------methods from Kaiyu--------------------------------------
def showDate(items, str):
    if len(items)==0:
        print('no tasks to print')
        return
    print('\n')
    if str == "date":
        print("%-10s %-10s %-10s %-10s %-10s"%('date','item#','amount','category','description'))
    elif str == "month":
        print("%-10s %-10s %-10s %-10s %-10s"%('month','item#','amount','category','description'))
    print('-'*70)
    for item in items:
        values = tuple(item.values()) 
        print("%-10s %-10s %-10s %10s %10s"% ( values[1], values[2], values[3], values[4],"  "+values[5]))
#-----------------------------end of methods from Kaiyu------------------------------------

def process_args(arglist):
    
    #---------------------------------methods from Trista -----------------------------------
    tracker = Transaction()
    if arglist==[] or arglist==["menu"]:
        usage()
    elif arglist[0]=="show":
        showTable(tracker.show_transactions())
    elif arglist[0]=='add':
        if len(arglist)!=6:
            print(len(arglist))
            print("more information needed")
            usage()
        else:
            userInput = {'item_num':arglist[1],'amount':arglist[2],'category':arglist[3], 'date':arglist[4],'description':arglist[5]}
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
            process_args(args)
            print('-'*70+'\n')
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*70+'\n')
    
toplevel()