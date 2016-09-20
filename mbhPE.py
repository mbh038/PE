# -*- coding: utf-8 -*-
"""

mbhPE

Created on Mon Sep 19 13:35:35 2016

@author: mbh
"""

import re
import sqlite3

def pe():
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS peProblems ')
    cur.execute('CREATE TABLE peProblems (problem INTEGER, title TEXT, date TEXT, answer INTEGER, time INTEGER, languages TEXT, tags TEXT, refs TEXT, notes TEXT)')

    hand = open('ProjectEuler.txt')
    count=0
    for line in hand:
        line = line.rstrip()
#        if re.search('^Problem:.+', line):
#            print(line)
        problem = re.findall('^Problem:+([0-9]*[0-9])', line)
        if len(problem)>0:
            count+=1
            problem=int(problem[0])
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
            time = re.findall('^Time.*:([0-9]*[0-9])', next(hand))
            if len(time)>0:
                time=int(time[0])
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



def db():
    conn = sqlite3.connect('mbhPE.sqlite3')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS peProblems ')
    cur.execute('CREATE TABLE peProblems (problem INTEGER, title TEXT, date TEXT, answer INTEGER, time INTEGER, languages TEXT, tags TEXT, refs TEXT, notes TEXT)')
    conn.close()