# -*- coding: utf-8 -*-
"""

mbhPE

Created on Mon Sep 19 13:35:35 2016

@author: mbh
"""

import re
import sqlite3

def penew1():
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS peProblems ')
    cur.execute('CREATE TABLE peProblems (problem TEXT, title TEXT, date TEXT, answer TEXT, time TEXT, languages TEXT, tags TEXT, refs TEXT, notes TEXT)')

    hand = open('ProjectEuler.txt')
    count=0
    for line in hand:
        line = line.rstrip()
#        if re.search('^Problem:.+', line):
#            print(line)
        problem = re.findall('^Problem:+([0-9]*[0-9])', line)
        if len(problem)>0:
            count+=1
            problem=problem[0]
            print()
            print (problem)
            title = re.findall('^Title:+(\S.*)', next(hand))
            print(title)
            if len(title)>0:
                title=title[0]
            date = re.findall('^Date:+(\S.*)', next(hand))
            print(date)
            if len(date)>0:
                date=date[0]
            answer = re.findall('^Answer:+([0-9]*[0-9])', next(hand))
            if len(answer)>0:
                answer=int(answer[0])
            else: answer=0
            time = re.findall('^Time.*:([0-9].*[0-9])', next(hand))
            if len(time)>0:
                time=time[0]
                print(time)
            else:
                time=0
            languages = re.findall('^Languages:+(\S.*)', next(hand))
            if len(languages)>0:
                languages=languages[0]                
            tags = re.findall('^Tags:+(\S.*)', next(hand))
            if len(tags)>0:
                tags=tags[0]
            else:
                tags=''
            references = re.findall('^References:+(\S.*)', next(hand))
            if len(references)>0:
                references=references[0]
                print(references)
            else:
                references=''
            notes = re.findall('^Notes:+(\S.*)', next(hand))
            if len(notes)>0:
                notes=notes[0]
            else:
                notes=''
                
            cur.execute('INSERT INTO peProblems (problem,title,date,answer,time,languages,tags,refs,notes) VALUES (?,?,?,?,?,?,?,?,?)',(problem,title,date,answer,time,languages,tags,references,notes))
            conn.commit()
    print(count)

def penew():
    problem = input('Problem number?\n')
    title = input('Title?\n')
    date=input('Date?\n')
    answer=input('Answer?\n')
    time=input('Running time?\n')
    languages=input('Languages?\n')
    tags=input('Tags?\n')
    refs=input('References?\n')
    notes=input('Notes?\n')
    
    
    fields=[problem,title,date,answer,time,languages,tags,refs,notes]
    
    for field in fields:
        if len(field)==0: field=''
        print (len(field))
        
    
    
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    
    cur.execute('INSERT INTO peProblems (problem,title,date,answer,time,languages,tags,refs,notes) VALUES (?,?,?,?,?,?,?)',(problem,title,date,answer,time,languages,tags,refs,notes,))
    conn.commit()

def pethere(number):
    response={True:'Already in database',False:'Not in database'}
    number=str(number)
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    cur.execute('select count(*) from peProblems where problem = ?',(number,))
    for row in cur:
        cur.close()
        return response[row[0]!=0]
    
#    return response[row[0]!=0]
    
def petags(term):
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT * FROM peProblems WHERE tags LIKE ?',('%'+term+'%',))
#    cur.execute('SELECT * FROM peProblems WHERE tags LIKE ?',(term,))
    for row in cur:
#        print(row)
        print(row[0],row[1],row[4],'ms',row[6])
    cur.close()

def petime(value,gt=True):
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    if gt:
        cur.execute('SELECT * FROM peProblems WHERE time >= ?',(value,))
    else:
        cur.execute('SELECT * FROM peProblems WHERE time < ?',(value,))
    for row in cur:
        print(row[0],row[4],row[1])
    cur.close()
    

def db():
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS peProblems ')
    cur.execute('CREATE TABLE peProblems (problem INTEGER, title TEXT, date TEXT, answer INTEGER, time INTEGER, languages TEXT, tags TEXT, refs TEXT, notes TEXT)')
    conn.close()