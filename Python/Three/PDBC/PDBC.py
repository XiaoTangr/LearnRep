import mysql.connector

DEV = True

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

    def Query(self, Sql, args=None):
        try:
            if args != None:
                self.Cursor.execute(Sql, args)
            else:
                self.Cursor.execute(Sql)
            result = self.Cursor.fetchall()
            return result if len(result) > 0 else 0
        except Exception as e:
            self.Conn.rollback()
            return e

    def Insert(self, Table, cols=None, datas=None):
        """
        插入数据
        *   Table   表名
        *   cols    字段名,[col1, col2, ...]
        *   datas   值，二维列表，二级长度应与cols参数长度对应
        """
        sql = "INSERT INTO `" + Table + "`"
        col = ""
        data_str = ""
        if cols != None:
            if  (len(datas) == 0) or (len(datas[0]) != len(cols)):
                print ("ERR: The data is not equal to the column name or no data is given!")
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
                    trmpdata = str(datas[i][j]) if type(datas[i][j]) != str else datas[i][j]
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
        

    def Update(self, Table, DataBuf,Wheres):
        sql = 'UPDATE `' + Table + '` SET '
        datas =''
        where = Wheres
        if (len(DataBuf[0] ) != len(DataBuf[1])) or (len(DataBuf) > 2):
            print("ERR: DataBuf is wrong!")

        for i in range(len(DataBuf[0])):
            colname = str(DataBuf[0][i]) if type(DataBuf[0][i]) != str else DataBuf[0][i]
            data_str = str(DataBuf[1][i]) if type(DataBuf[1][i]) != str else DataBuf[1][i]
            datas += colname + ' = "' + data_str + '",'
        datas = datas[:-1] 
        sql += datas
        sql += ' WHERE ' + where + ";"
        if DEV :
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


if __name__ == "__main__":
    Conn = DB_Conn("localhost", 3306, "root", "root", "PDBC")
    Conn.CreateCur()
    Conn.Insert("na",["ddd","ddddd"],[["ddd","ddddd"],["ddd","ddddd"]])
    Conn.Update("Table",[["id","name"],[999,"newname"]],"id = 333")