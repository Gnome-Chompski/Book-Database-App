# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 15:31:52 2017

@author: Dante

Backend of database program. Stores all the function relating to making changes within
the database table. The program can add, view, search, delete and update entries.
Needs to be supplied to the Frontend part of the program.
"""

import sqlite3

def connect():
    '''
    - books.db an existing database
    checks to see if there is a table called books within the database if not, it is created
    '''
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    close(conn)

def add(title,author,year,isbn):
    '''
    all parameters of type str
    - title - title of book
    - author - author of book
    - year - year of publication
    - isbn - ISBN of book
    
    adds tuples information to the table to the corresponding attribute
    '''
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    close(conn)
    view()

def view():
    '''
    Brings the entire table from the database
    '''
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    '''
    params of type str, empty if not specified
    - title - title of book
    - author - author of book
    - year - year of publication
    - isbn - ISBN of book
    
    Brings all the rows that matches to one or more of the specified params
    '''
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    '''
    - id int variable
    
    deletes row corresponding to the supplied primary key which is the row number
    '''
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    close(conn)

def update(id,title,author,year,isbn):
    '''
    - id - int, primary key of table
    - title - str, title of book
    - author - str, author of book
    - year - str, publication year
    - isbn - str, ISBN of book
    
    Finds desired row to update via primary key, rest of params supplied are the new entry at the position.
    '''
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    close(conn)
    
def close(conn):
    conn.commit()
    conn.close()

connect()
