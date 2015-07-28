import logging

_logger = logging.getLogger(__name__)

class DAO(object):
    """Base Data Access Object."""

    _datasource = None

    _mapper = None

    _table = None

    _primary_key = 'id'

    def _mapping(self, iterable, mapping=None):
        return self._mapper(*iterable)

    def _fetchone(self, sql, values):
        return self.__class__._datasource.fetchone(sql, values)

    def _fetchall(self, sql, values):
        return self.__class__._datasource.fetchall(sql, values)

    def _select_one(self, sql, values=None):
        _logger.debug('sql={sql}, values={values}'.format(sql=sql, values=values))
        return self._mapping(self._fetchone(sql, values))

    def _select_all(self, sql, values=None):
        return map(self._mapping, self._fetchall(sql, values))

    def _insert(self, sql, values):
        self._update(sql, values)

    def _update(self, sql, values):
        self.__class__._datasource.update(sql, values)

    def _delete(self, sql, values):
        self._update(sql, values)

    def find(self, id):
        """Find by primary key."""
        return self._select_one('''
            select
                *
            from
                {table}
            where
                {primary_key} = %s
        '''.format(table=self.__class__._table,
            primary_key=self.__class__._primary_key), [id])
