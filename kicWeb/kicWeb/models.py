# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:16:11 2021

@author: andya
"""

#DAO 라고 생각하면 된다고

import cx_Oracle

connection = cx_Oracle.connect('kic','1234','localhost/xe')


def List():
    cursor = connection.cursor()
    sql = "select * from ( select rownum rnum, a.* " + \
        "from (select * from board order by num desc) a)" + \
            "where rnum between 1 and 10"
    cursor.execute(sql)
    #setDic(cursor)
    return setDic(cursor)

# cursor를 보내서 딕셔너리로 만드는 작업이라고 생각    
def setDic(cursor):
    columnNames = [col[0].lower() for col in cursor.description]
    print(columnNames)
    dic = []
    for record in cursor:
        dic.append(dict(zip(columnNames, record)))
    return dic
     

def Content(num):
    print(num)
    cursor = connection.cursor()
    sql = "select * from board where num=:num"
    cursor.execute(sql, num=num)
    #content=cursor.fetchone()
    return setDic(cursor)

def Write(board):
    cursor = connection.cursor()
    sql =(" insert into board (num, name, subject, content, regdate, "+
          "readcnt, ref, reflevel, refstep) " +
          "values (boardseq.nextval,:name, :subject, :content, sysdate, " +
          "0, 0, 0, 0)" )
    cursor.execute(sql, board)
    connection.commit()







