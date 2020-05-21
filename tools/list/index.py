#!/usr/bin/env python
class Index(dict):
    def __init__(self, *args, **kw):
        super(Index, self).__init__(*args, **kw)
        self.itemlist = super(Index, self).keys()
        self.__validate()

    def __setitem__(self, key, value):
        self.itemlist.append(key)

    def __iter__(self):
        return iter(self.itemlist)

    def keys(self):
        return self.itemlist

    def values(self):
        return [self[key] for key in self]

    def add(self, dict):
        self.update({key: self.get(key, 0) + dict.get(key, 0) for key in set(self) | set(dict)})
        return self

    def update(self, dict):
        super(Index, self).update(dict)
        self.__validate()
        return self

    def __validate(self):
        for value in self.values():
            if not type(value) is int:
                raise TypeError("Using " + str(type(value)) + ", but only integers are allowed")

    def itervalues(self):
        return (self[key] for key in self)