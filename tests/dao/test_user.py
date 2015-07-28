from unittest import TestCase
from core.dao.datasource import DataSource
from core.dao.user import User as UserDao
from core.vo.user import User

class FakeUserDateSource(DataSource):
    def fetchone(self, sql, values):
        return (1, 'macbin', 'ning', 'macbinn@logtome.com', 'nibcam', 123456789)

    def fetchall(self, sql, values):
        return [
            (1, 'macbin', 'ning', 'macbinn@logtome.com', 'nibcam', 123456789),
            (1, 'macbin', 'ning', 'macbinn@logtome.com', 'nibcam', 123456789),
            (1, 'macbin', 'ning', 'macbinn@logtome.com', 'nibcam', 123456789),
            ]


UserDao._datasource = FakeUserDateSource()
user_dao = UserDao()

class TestUser(TestCase):
    def test_query_by_id(self):
        print user_dao.query_user_by_id(1)

    def test_find(self):
        print user_dao.find(1)

    def test_query_user_by_email(self):
        print user_dao.query_user_by_email('macbinn@logtome.com')

    def test_query_users(self):
        print user_dao.query_users()

    def test_insert_user(self):
        user_dao.insert_user(User(first_name='macbin', last_name='ning'))

    def test_update_user(self):
        user_dao.update_user(User(id=1, first_name='macbin', last_name='ning'))

    def test_delete_user(self):
        user_dao.delete_user(1)
