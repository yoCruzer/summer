import threading


class DataSource(object):
    """DataSource"""
    def fetchone(self, sql, values):
        """fetch one row from database.
        """
    def fetchall(self, sql, values):
        """fetch multii rows from database.
        """
    def update(self, sql, values):
        """fetch one row from database.
        """


class DBAPIDataSource(DataSource):
    """A dataSource that implements DBAPI"""

    def __init__(self):
        """init datasource.

        note: datasource must be used as singleton.
        """
        self.thread_local = threading.local()
        self.thread_local.connection = None

    def _connection(self):
        """get connection.

        TO DO: use connection pool.
        """
        if self.thread_local.connection is None:
            self.thread_local.connection = MySQLdb.connect()
        return self.thread_local.connection

    def _cursor(self):
        return self._connection().cursor()


    def fetchone(self, sql, values):
        """fetch one row from database.
        """
        cursor = self._cursor()
        cursor.execute(sql, values)
        return cursor.fetchone()

    def fetchall(self, sql, values):
        """fetch multii rows from database.
        """
        cursor = self._cursor()
        cursor.execute(sql, values)
        return cursor.fetchall()

    def update(self, sql, values):
        """fetch one row from database.
        """
        cursor = self._cursor()
        try:
            cursor.execute(sql, values)
            cursor.commit()
        finally:
            cursor.rollback()
