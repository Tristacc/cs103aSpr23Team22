import pytest
import sqlite3
import os
from transactions import Transaction

#---------------------------------test from Trista -----------------------------------
@pytest.fixture
def transaction():
    transaction = Transaction()
    return transaction

@pytest.fixture
def sample_item():
    sample_item = {
        'item_num': 1,
        'amount': 50,
        'category': 'Groceries',
        'date': '2023-02-05',
        'description': 'Bread and milk'
    }
    return sample_item

# prepare -- clear table
def clearTable():
    con= sqlite3.connect(os.getcwd()+'/tracker.db')
    cur = con.cursor() 
    cur.execute("DELETE FROM transactions")
    con.commit()
    con.close()

# get number of data in the table
def num_data():
    con= sqlite3.connect(os.getcwd()+'/tracker.db')
    cur = con.cursor() 
    cur.execute("SELECT COUNT(*) FROM transactions")
    count = cur.fetchone()[0]
    con.close()
    return count

def test_add(transaction, sample_item):
    clearTable()
    initial_num = num_data()
    #add one data
    transaction.add(sample_item)
    count =  num_data()
    assert count == initial_num + 1

def test_delete(transaction):
    userInput = {'item_num':1}
    transaction.delete(userInput)
    count =  num_data()
    assert count == 0

#----------------------------end of test from Trista -----------------------------------

#---------------------------------test from Kaiyu---------------------------------------

sample_item1 = {
    'item_num': 1,
    'amount': 50,
    'category': 'Groceries',
    'date': '2023-02-05',
    'description': 'Bread and milk'
}
sample_item2 = {
    'item_num': 2,
    'amount': 30,
    'category': 'Vegetables',
    'date': '2023-02-05',
    'description': 'Tomatoes'
}
sample_item3 = {
    'item_num': 2,
    'amount': 20,
    'category': 'Vegetables',
    'date': '2023-02-05',
    'description': 'Tomatoes'
}
sample_item4 = {
    'item_num': 1,
    'amount': 50,
    'category': 'Groceries',
    'date': '2023-02-25',
    'description': 'Bread and milk'
}
sample_item5 = {
    'item_num': 3,
    'amount': 1,
    'category': 'Electronic',
    'date': '2023-03-03',
    'description': 'Earphones'
}

def test_summarize_by_date(transaction):
    clearTable()
    transaction.add(sample_item1)
    transaction.add(sample_item2)
    transaction.add(sample_item3)
    transaction.add(sample_item4)
    transaction.add(sample_item5)
    count = len(transaction.summarize_by_date())
    assert count == 4
    clearTable()

def test_summarize_by_month(transaction):
    clearTable()
    transaction.add(sample_item1)
    transaction.add(sample_item2)
    transaction.add(sample_item3)
    transaction.add(sample_item4)
    transaction.add(sample_item5)
    count = len(transaction.summarize_by_month())
    assert count == 3
    clearTable()

#----------------------------end of test from Kaiyu-------------------------------------

#---------------------------- test from Chenchuhui -------------------------------------

@pytest.fixture
def item_list():
    return [{
        'item_num': 1,
        'amount': 50,
        'category': 'Groceries',
        'date': '2023-02-05',
        'description': 'Bread and milk'
    }, {
        'item_num': 1,
        'amount': 40,
        'category': 'Groceries',
        'date': '2023-01-05',
        'description': 'Bread and milk'
    }, {
        'item_num': 2,
        'amount': 30,
        'category': 'Groceries',
        'date': '2023-03-05',
        'description': 'Bacon'
    }, {
        'item_num': 3,
        'amount': 10,
        'category': 'Groceries',
        'date': '2023-03-05',
        'description': 'Eggs'
    }]

def test_summarize_by_year(transaction, item_list):
    clearTable()
    for i in item_list:
        transaction.add(i)
    output = transaction.summarize_by_year()
    assert output[0]["item_num"] == 1
    assert output[0]["amount"] == 90
    assert output[1]["item_num"] == 2
    assert output[1]["amount"] == 30
    assert output[2]["item_num"] == 3
    assert output[2]["amount"] == 10

def test_summarize_by_category(transaction, item_list):
    clearTable()
    for i in item_list:
        transaction.add(i)
    output = transaction.summarize_by_category()
    assert output[0]["amount"] == 130
    assert output[0]["category"] == "Groceries"
    clearTable()

#---------------------------- end of test from Chenchuhui -------------------------------------