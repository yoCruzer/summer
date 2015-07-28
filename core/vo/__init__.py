class VO(object):
    """Base Vaule Object.
    """

    _properties = tuple()

    _hidden = tuple()

    def __init__(self, *args, **kwargs):
        """Base init function.
        
        setattr from _properties
        """
        if kwargs:
            for name in self.__class__._properties:
                setattr(self, name, kwargs.get(name))
        else:
            for index, name in enumerate(self.__class__._properties):
                setattr(self, name, args[index])

    def __iter__(self):
        """Implement iterator.

        yield attr_name, attr_value
        """
        for name in self.__class__._properties:
            yield name, getattr(self, name)

    def __repr__(self):
        return '<{name} {properties}>'.format(
                name=self.__class__.__name__,
                properties=', '.join(
                    '{k}={v}'.format(k=k, v=repr(v)) for k, v in self))

    def __json__(self):
        """Implement JSON encoding.

        return a dict with attr_name, attr_value pairs
            except attr_name in _hidden
        """
        return {k: v for k, v in self if k not in self._hidden}
