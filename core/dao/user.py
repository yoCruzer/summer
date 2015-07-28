from . import DAO
from ..vo import user

class User(DAO):

    _mapper = user.User

    _table = 'user'

    def query_user_by_id(self, id):
        return self._select_one('''
            select
                *
            from
                user
            where
                id = %s
        ''', [id])

    def query_user_by_email(self, email):
        return self._select_one('''
            select
                *
            from
                user
            where
                email = %s
        ''', [email])

    def query_users(self):
        return self._select_all('''
            select
                *
            from
                user
        ''')

    def insert_user(self, user):
        return self._insert('''
            insert into
                user
            (
                first_name,
                last_name,
                email,
                password,
            )
            values
            (
                {first_name},
                {last_name},
                {email},
                {password},
            )
        ''', user)

    def update_user(self, user):
        return self._update('''
            update
                user
            set
            (
                first_name = {first_name},
                last_name = {last_name},
                email = {email},
                password = {password},
            )
            where
                id = %s
        ''', user)

    def delete_user(self, id):
        return self._delete('''
            delete from
                user
            where
                id = %s
        ''', [id])
