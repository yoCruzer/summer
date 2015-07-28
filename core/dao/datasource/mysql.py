from . import DBAPIDataSource
import MySQLdb


class MysqlDataSource(DBAPIDataSource):
    """DataSource"""
    def _new_connection(self):
        """create a new connection.

        TO DO: use connection pool.
        """
        return MySQLdb.connect()
