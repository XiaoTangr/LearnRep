import mysql.connector

import re

DEV = False


class DB_Conn:
    DB_HOST = ''
    DB_PORT = 0
    DB_USER = ''
    DB_PASSWD = ''
    DB_NAME = ''
    Conn = None

    def __init__(self, HOST, PORT, USER, PASSWD, DB_NAME):
        self.DB_HOST = HOST
        self.DB_PORT = PORT
        self.DB_USER = USER
        self.DB_PASSWD = PASSWD
        self.DB_NAME = DB_NAME

        self.Conn = mysql.connector.connect(
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_USER,
            passwd=self.DB_PASSWD,
            db=self.DB_NAME,
            charset='utf8'
        )
        Cursor = None
        self.CreateCur()

    # 创建游标

    def CreateCur(self):
        self.Cursor = self.Conn.cursor()

    def Query(self, Sql):
        """
        Excute query
        :param Sql: Sql @String
        :return: Res@tuple: success, -1: fail, -2: Dev mod
        """
        if DEV:
            print(Sql)
            return -2
        try:
            self.Cursor.execute(Sql)
            result = self.Cursor.fetchall()
            return result if len(result) > 0 else 0
        except Exception as e:
            self.Conn.rollback()
            print(e)
            return -1

    def Insert(self, Table, cols=None, datas=None):
        """
        Insert Datas 
        :param Table    Table Name @String
        :param cols     Col Name that you will insert data into @["col1", "col2",...]
        :param datas    Datas you will insert @[["value11", "value12",...], ["value21", "value22",...],...]
        :return: 1: success, -1: fail, -2: Dev mod
        """
        sql = "INSERT INTO `" + Table + "`"
        col = ""
        data_str = ""
        if cols != None:
            if (len(datas) == 0) or (len(datas[0]) != len(cols)):
                print(
                    "ERR: The data is not equal to the column name or no data is given!")
                return -1
            col += "("
            for i in range(len(cols)):
                tempdata = str(cols[i]) if type(cols[i]) != str else cols[i]
                col += tempdata + ","
            col = col[:-1] + ")"

        if len(datas) > 0:
            for i in range(len(datas)):
                data_str += "("
                for j in range(len(datas[i])):
                    trmpdata = str(datas[i][j]) if type(
                        datas[i][j]) != str else datas[i][j]
                    data_str += "'" + trmpdata + "'" + ","
                data_str = data_str[:-1]
                data_str += "),"
            data_str = data_str[:-1] + ";"
        else:
            print("ERR: datas is empty!")
            return -1
        sql += col + " VALUES " + data_str
        if DEV:
            print(sql)
            return -2
        try:
            self.Cursor.execute(sql)
            self.Conn.commit()
            return 1
        except Exception as e:
            self.Conn.rollback()
            print(e)
            return -1

    def Update(self, Table, DataBuf, Wheres):
        """
        Update data in the table
        :param Table:   table name @String
        :param DataBuf: data buffer @[["col1", "col2",...], ["value1", "value2",...]]
        :param Wheres:  where conditions @String
        :return 1: success, -1: fail, -2: Dev mod
        """
        sql = 'UPDATE `' + Table + '` SET '
        datas = ''
        where = Wheres
        if (len(DataBuf[0]) != len(DataBuf[1])) or (len(DataBuf) > 2):
            print("ERR: DataBuf is wrong!")

        for i in range(len(DataBuf[0])):
            colname = str(DataBuf[0][i]) if type(
                DataBuf[0][i]) != str else DataBuf[0][i]
            data_str = str(DataBuf[1][i]) if type(
                DataBuf[1][i]) != str else DataBuf[1][i]
            datas += colname + ' = "' + data_str + '",'
        datas = datas[:-1]
        sql += datas
        sql += ' WHERE ' + where + ";"
        if DEV:
            print(sql)
            return -2
        try:
            self.Cursor.execute(sql)
            self.Conn.commit()
            return 1
        except Exception as e:
            self.Conn.rollback()
            print(e)
            return -1

    def Delete(self, Table, Wheres):
        """
        Delete data in the table
        :param Table:   table name @String
        :param Wheres:  where conditions @String
        :return 1: success, -1: fail, -2: Dev mod
        """
        sql = 'DELETE FROM `' + Table + '` WHERE ' + Wheres + ";"
        if DEV:
            print(sql)
            return -2
        try:
            self.Cursor.execute(sql)
            self.Conn.commit()
        except Exception as e:
            print(e)
            self.Conn.rollback()
            return -1
# 获取中文字符长度
def count_chinese_characters(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    chinese_characters = re.findall(pattern, text)
    return int(len(chinese_characters))

# 以表格方式打印查询结果
def PrintSheet(LineOne, LineZero=None, DataBuf=(), CellsWidth=15):
    Rows = ''
    LineThin = '|' + '-' * CellsWidth * len(LineOne) + '|'
    LineBold = '|' + '=' * CellsWidth * len(LineOne) + '|'
    print(LineThin)
    if LineZero:
        print('|' + LineZero.center(CellsWidth * len(LineOne) - count_chinese_characters(LineZero)) + '|')
    if (LineZero and LineOne):
        print(LineBold)
    if LineOne:
        for i in range(len(LineOne)):
            if i != len(LineOne) - 1:
                Rows += '|' + LineOne[i].center(CellsWidth)
            else:
                Rows += '|' + \
                    LineOne[i].center(CellsWidth - len(LineOne) + 1) + "|"
        print(Rows)
        Rows = ''
    print(LineBold)
    # print(DataBuf)
    if DataBuf != 0:
        for i in range(len(DataBuf)):
            for j in range(len(DataBuf[i])):
                if j != len(DataBuf[i]) - 1:
                    Rows += '|' + str(DataBuf[i][j]).center(CellsWidth)
                else:
                    Rows += '|' + \
                        str(DataBuf[i][j]).center(
                            CellsWidth - len(DataBuf[i]) + 1) + "|"
            print(Rows)
            Rows = ''
            print('|' + '-' * CellsWidth * len(LineOne) + '|')
    else:
        print('|' + "No Data!".center(CellsWidth * len(LineOne)) + '|')
        print(LineThin)
    print("\n")


if __name__ == "__main__":

    Conn = DB_Conn("localhost", 3306, "root", "root", "PDBC")
    Conn.CreateCur()
    Desc = ("Field", "Type", "Null", "Key", "Default", "Extra")
    PrintSheet(
        DataBuf=Conn.Query("desc `users`"), LineZero="数据表描述", LineOne=Desc, CellsWidth=25)

    # 插入
    Conn.Insert(Table="users", cols=["id", "name"], datas=[
                [1, "insert1"], [2, "insert2",]])
    Conn.Insert(Table="users", datas=[[3, "insert3", 6], [4, "insert4", 15]])
    PrintSheet(DataBuf=Conn.Query("SELECT * FROM `users`"),LineOne=("id", "name", "age"), LineZero="插入四条信息")

    # 更新
    Conn.Update(Table="users", DataBuf=[["name", "age"], [
                "UUUUUU", 999999999]], Wheres="id=1")
    PrintSheet(DataBuf=Conn.Query("SELECT * FROM `users`"),LineOne=("id", "name", "age"), LineZero="更新,id=1的信息改变")

    # 删除
    delId = [1, 2, 3, 4]
    for i in delId:
        Conn.Delete(Table="users", Wheres="id=" + str(i))
    PrintSheet(DataBuf=Conn.Query("SELECT * FROM `users`"),LineOne=("id", "name", "age"), LineZero="删除所有")
