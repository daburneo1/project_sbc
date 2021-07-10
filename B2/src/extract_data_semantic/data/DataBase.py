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

    def insert_journal(self, article):
        try:

            print("INSERT INTO Journal_Article (journalArticleId, abstract, doi, isOpenAccess, numCiting, paperId, title,"
                "venue, url, year) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (0, article.get_abstract(),
                                                                            article.get_doi(), article.get_isOpenAccess(),
                                                                            article.get_numCiting(), article.get_paperId(),
                                                                            article.get_title(), article.get_venue(),
                                                                            article.get_url(), article.get_year()))

            self.cursor.execute("INSERT INTO Journal_Article (journalArticleId, abstract, doi, isOpenAccess, numCiting, paperId, title,"
                "venue, url, year) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);", (0, article.get_abstract(),
                                                                            article.get_doi(), article.get_isOpenAccess(),
                                                                            article.get_numCiting(), article.get_paperId(),
                                                                            article.get_title(), article.get_venue(),
                                                                            article.get_url(), article.get_year()))
            self.connection.commit()

        except Error as ex:
            print("Error en la carga de journal_article", ex)

    def get_id_journal(self, article):
        try:
            sql = ('SELECT journalArticleId FROM Journal_Article WHERE paperId = "{}";'.format(article.get_paperId()))
            print(sql)
            self.cursor.execute('SELECT journalArticleId FROM Journal_Article WHERE paperId = "{}";'.format(article.get_paperId()))
            id = self.cursor.fetchone()
            print('id1 %s'% id)
            id = int(id[0])
            print('id2 %s'% id)
            return id

        except Error as ex:
            print("Error en la consulta", ex)

    def insert_authors(self, article, id):
        try:
            authors_list = article.get_authors()
            for author in authors_list:
                print('INSERT INTO Author (name, url, influentialCitationCount, id, journalArticleId) VALUES ("{}","{}",{},{},{});'
                .format(author.get_name(), author.get_url(), author.get_influentialCitationCount(), author.get_authorId(), int(id)))

                self.cursor.execute('INSERT INTO Author (name, url, influentialCitationCount, id, journalArticleId) VALUES ("{}","{}",{},{},{});'
                .format(author.get_name(), author.get_url(), author.get_influentialCitationCount(), author.get_authorId(), int(id)))
                self.connection.commit()

                id_author = self.get_author(author)
                self.insert_aliases(author, id_author)

        except Error as ex:
            print("Error en la carga de autores", ex)

    def insert_references(self, article, id):
        try:
            references_list = article.get_references()
            for reference in references_list:
                print('INSERT INTO reference (doi, title, year, isInfluential, journalArticleId) VALUES ("{}","{}","{}","{}","{}");'
                    .format(reference.get_doi(), reference.get_title(), reference.get_year(), reference.get_isInfluential(), int(id)))

                self.cursor.execute('INSERT INTO reference (doi, title, year, isInfluential, journalArticleId) VALUES ("{}","{}","{}","{}","{}");'
                    .format(reference.get_doi(), reference.get_title(), reference.get_year(), reference.get_isInfluential(), int(id)))
                self.connection.commit()

        except Error as ex:
            print("Error en la carga de referencias",ex)


    def get_author(self, author):
        try:
            sql = ('SELECT idAuthor FROM Author WHERE id = "{}";'.format(author.get_authorId()))
            print(sql)
            self.cursor.execute('SELECT idAuthor FROM Author WHERE id = "{}";'.format(author.get_authorId()))
            id = self.cursor.fetchone()
            id = int(id[0])
            return id

        except Error as ex:
            print("Error en la consulta author", ex)


    def insert_aliases(self, author, id):
        try:
            aliases_list = author.get_aliases()
            for alias in aliases_list:
                print('INSERT IGNORE INTO Alias (alias, idAuthor) VALUES ("{}",{});'
                                    .format(alias, id))

                self.cursor.execute('INSERT IGNORE INTO Alias (alias, idAuthor) VALUES ("{}",{});'
                                    .format(alias, id))
                self.connection.commit()
        except Error as ex:
            print("Error en la carga de alias", ex)

    def insert_fieldsOfStudy(self, article, id):
        try:
            fields_list = article.get_fieldsOfStudy()
            for field in fields_list:
                if field != None:
                    print("INSERT INTO Field_Study (fieldStudy, journalArticleId) VALUES "
                                        "('{}',{});".format(field, id))

                    self.cursor.execute('INSERT INTO Field_Study (fieldStudy, journalArticleId) VALUES '
                                    '("{}",{});'.format(field, id))
                    self.connection.commit()
        except Error as ex:
            print("Error en la carga de FieldsOfStudy", ex)

    def find_article(self, article):
        try:
            sql = ("SELECT journalArticleId FROM Journal_Article WHERE paperId = '{}';".format(article.get_paperId()))
            print(sql)
            self.cursor.execute("SELECT journalArticleId FROM Journal_Article WHERE paperId = '{}';".format(article.get_paperId()))
            exist = self.cursor.fetchone()
            if(exist is None):
                return True
            else:
                return False
        except Error as ex:
            print("Error en la consulta find", ex)

    def insert_topics(self, article, id):
        try:
            topics_list = article.get_topics()
            for field in topics_list:
                if field != None:
                    print("INSERT INTO Topics (topic, journalArticleId) VALUES "
                                        "('{}',{});".format(field, id))

                    self.cursor.execute("INSERT INTO Topics (topic, journalArticleId) VALUES "
                                        "('{}',{});".format(field, id))
                    self.connection.commit()
        except Error as ex:
            print("Error en la carga de Topics", ex)

database = DataBase()