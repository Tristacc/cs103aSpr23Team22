# cs103aSpr23Team22

PA03

------------------Trista's result--------------------

1. pytest report
   ========================= test session starts ======================================
   platform darwin -- Python 3.9.1, pytest-7.2.1, pluggy-1.0.0
   rootdir: /Users/tristaed/Desktop/cs103aSpr23Team22/PA03
   plugins: anyio-3.6.2
   collected 2 items

test_transaction.py .. [100%]

========================== 2 passed in 0.09s ===========================================

2. pylint report
   My part in tracker.py : Your code has been rated at 6.53/10
   My part in transactions.py : Your code has been rated at 3.64/10(previous run: 0.45/10, +3.18)

------------------end of Trista's result--------------------

---------------------Kaiyu's result-------------------------

1. pytest report
   ============================= test session starts ==================================
   platform darwin -- Python 3.8.10, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
   rootdir: /Users/pkydemac/Desktop/cs103aSpr23Team22/PA03
   plugins: anyio-2.2.0  
   collected 4 items
   test_transaction.py ....[100%]

================================= 4 passed in 0.03s ====================================

2. pylint report
   tracker.py: Your code has been rated at 6.21/10
   transactions.py: Your code has been rated at 2.41/10

------------------end of Kaiyu's result---------------------

---------------------Chenchuhui's result-------------------------

1. pytest report
=========================================== test session starts ========================================================
platform win32 -- Python 3.11.0, pytest-7.2.2, pluggy-1.0.0
rootdir: C:\Users\帅逼胡陈\Documents\Brandeis Spring23\COSI 103A Fundamentals of Software Engineering\cs103aSpr23Team22\PA03
plugins: anyio-3.6.2
collected 6 items

test_transaction.py ......                                                                                                                                 [100%]

============================================= 6 passed in 0.45s ======================================================

2. pylint report
   tracker.py: Your code has been rated at 6.81/10 (previous run: 6.81/10, +0.00)
   transactions.py: Your code has been rated at 4.86/10 (previous run: 4.86/10, +0.00)

------------------end of Chenchuhui's result---------------------


----------------------------Ran's result------------------------------

1. pytest report
===================================================== test session starts =====================================================
platform darwin -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: /Users/ranwei/Desktop/Class/SoftwareEngineering/cs103aSpr23Team22/PA03
plugins: anyio-3.6.2
collected 7 items                                                                                                                                     

test_transaction.py .......                                                                                                                     [100%]

======================================================= 7 passed in 0.14s ======================================================
2. pylint report
   tracker.py: Your code has been rated at 6.79/10
   transactions.py: Your code has been rated at 4.59/10

-----------------------------------end of Ran's result-----------------------------------


---------------------------------- run tracker.py ----------------------------------------
running tracker.py
$ python tracker.py 
usage:
            tracker add [item#] [amount] [category] [date] [description]
            tracker show
            tracker delete [item#]
            tracker summarize-by-date
            tracker summarize-by-month
            tracker summarize-by-year
            tracker summarize-by-category

tracker> show


item#      amount     category   date   description
----------------------------------------------------------------------
2          15         Grocery    2023-04-11      Bread
3          5          Pet        2020-04-15    Dogfood
4          10         Pet        2021-05-12    Catfood
5          5          Sadfood    2020-04-12     Burger
----------------------------------------------------------------------

tracker> add 1 20 Grocery 2023-05-11 Milk
----------------------------------------------------------------------

tracker> show


item#      amount     category   date   description
----------------------------------------------------------------------
2          15         Grocery    2023-04-11      Bread
3          5          Pet        2020-04-15    Dogfood
4          10         Pet        2021-05-12    Catfood
5          5          Sadfood    2020-04-12     Burger
1          20         Grocery    2023-05-11       Milk
----------------------------------------------------------------------

tracker> summarize-by-date


date       item#      amount     category   description
----------------------------------------------------------------------
2020-04-12 5          5             Sadfood     Burger
2020-04-15 3          5                 Pet    Dogfood
2021-05-12 4          10                Pet    Catfood
2023-04-11 2          15            Grocery      Bread
2023-05-11 1          20            Grocery       Milk
----------------------------------------------------------------------

tracker> summarize-by-month


month      item#      amount     category   description
----------------------------------------------------------------------
2020-04    3          5                 Pet    Dogfood
2020-04    5          5             Sadfood     Burger
2021-05    4          10                Pet    Catfood
2023-04    2          15            Grocery      Bread
2023-05    1          20            Grocery       Milk
----------------------------------------------------------------------

tracker> summarize-by-year


year       item#      amount     category   description
----------------------------------------------------------------------
2020       3          5                 Pet    Dogfood
2020       5          5             Sadfood     Burger
2021       4          10                Pet    Catfood
2023       1          20            Grocery       Milk
2023       2          15            Grocery      Bread
----------------------------------------------------------------------

tracker> summarize-by-category


amount     category
----------------------------------------------------------------------
35         Grocery
15         Pet
5          Sadfood
----------------------------------------------------------------------

tracker> show    


item#      amount     category   date   description
----------------------------------------------------------------------
2          15         Grocery    2023-04-11      Bread
3          5          Pet        2020-04-15    Dogfood
4          10         Pet        2021-05-12    Catfood
5          5          Sadfood    2020-04-12     Burger
1          20         Grocery    2023-05-11       Milk
----------------------------------------------------------------------

tracker> delete 1
----------------------------------------------------------------------

tracker> show


item#      amount     category   date   description
----------------------------------------------------------------------
2          15         Grocery    2023-04-11      Bread
3          5          Pet        2020-04-15    Dogfood
4          10         Pet        2021-05-12    Catfood
5          5          Sadfood    2020-04-12     Burger
----------------------------------------------------------------------

tracker> quit
-------------------------------------------------------------
ranwei@Rans-MacBook-Air PA03 % python3 tracker.py  
usage:
            tracker add [item#] [amount] [category] [date] [description]
            tracker show 
            tracker delete [item#]
            tracker summarize-by-date
            tracker summarize-by-month 
            tracker summarize-by-year 
            tracker summarize-by-category 
            
tracker> show
no transactions to print
----------------------------------------------------------------------

tracker> add 1 2 Groceries 2023-09-26 Bread
----------------------------------------------------------------------

tracker> add 2 6 Groceries 2023-10-03 Banana                                   
----------------------------------------------------------------------

tracker> add 3 5 Produce 2023-10-04 Apple
----------------------------------------------------------------------

tracker> select-by-amount-range 3 7


item#      amount     category   date   description
----------------------------------------------------------------------
2          6          Groceries  2023-10-03     Banana
3          5          Produce    2023-10-04      Apple
----------------------------------------------------------------------
