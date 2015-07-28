from . import VO
from datetime import datetime

class User(VO):
    _properties = (
        'id',
        'first_name',
        'last_name',
        'email',
        'password',
        'create_time',
    )

    _hidden = (
        'password',
    )

    def create_at(self):
        """Converting int to datetime.

        TO DO: need cache result, maybe @property works.
        """
        return datetime.fromtimestamp(self.create_time)
