
from transactions import Transaction
import sys


def usage():
    print('''usage:
            tracker add [item#] [amount] [category] [date] [description]
            tracker show 
            tracker delete [item#]
            menu
            '''
            )
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

def process_args(arglist):
    
    #---------------------------------methods from Trista -----------------------------------
    tracker = Transaction()
    if arglist==[] or arglist==["menu"]:
        usage()
    elif arglist[0]=="show":
        showTable(tracker.showTransactions())
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