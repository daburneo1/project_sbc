import mysql.connector as mysql
from mysql.connector import Error


class DataBase:
    def __init__(self):
        self.connection = mysql.connect(
            host='localhost',
            user='root',
            password='',
            db='covid19_semantic'
        )

        self.cursor = self.connection.cursor(buffered=True)

        print("Conexion exitosa")

    def get_abstract(self, i):
        try:
            sql = ('SELECT abstract FROM Journal_Article WHERE JournalArticleId = "{}";'.format(i))
            print(sql)
            self.cursor.execute('SELECT abstract FROM Journal_Article WHERE JournalArticleId = "{}";'.format(i))
            result = self.cursor.fetchall()
            return result
        except Error as ex:
            print("Error en la consulta", ex)

    def get_field_study(self, i):
        try:
            sql = ('SELECT fieldStudy FROM field_study WHERE journalArticleId = "{}";'.format(i))
            print(sql)
            self.cursor.execute('SELECT fieldStudy FROM field_study WHERE journalArticleId = "{}";'.format(i))
            result = self.cursor.fetchone()
            return result
        except Error as ex:
            print("Error en la consulta", ex)

    def get_venue(self, i):
        try:
            sql = ('SELECT venue FROM Journal_Article WHERE JournalArticleId = "{}";'.format(i))
            print(sql)
            self.cursor.execute('SELECT venue FROM Journal_Article WHERE JournalArticleId = "{}";'.format(i))
            result = self.cursor.fetchone()
            return result
        except Error as ex:
            print("Error en la consulta", ex)

    def get_article(self, i):
        try:
            sql = ('SELECT * FROM Journal_Article WHERE JournalArticleId = "{}";'.format(i))
            print(sql)
            self.cursor.execute('SELECT * FROM Journal_Article WHERE JournalArticleId = "{}";'.format(i))
            result = self.cursor.fetchone()
            return result
        except Error as ex:
            print("Error en la consulta", ex)


database = DataBase()
