# -*- coding: utf-8 -*-
"""Shape mixins, mostly to validate data."""
from __future__ import print_function, division, absolute_import, unicode_literals


class Data1DMixin(object):
    """Validate 1 dimensional data."""
    def __init__(self, data, *args, **kwargs):
        if not len(data):
            raise ValueError('Data must not be empty.')
        super(Data1DMixin, self).__init__(data, *args, **kwargs)


class Data2DMixin(object):
    """Validate 2 dimensional data."""
    def __init__(self, data, *args, **kwargs):
        if len(data) != 2:
            msg = 'Data must be 2-dimensional, but it contains {} datasets.'
            raise ValueError(msg.format(len(data)))
        super(Data2DMixin, self).__init__(data, *args, **kwargs)


class Data4DMixin(object):
    """Validate 4 dimensional data."""
    def __init__(self, data, *args, **kwargs):
        if len(data) != 4:
            msg = 'Data must be 4-dimensional, but it contains {} datasets.'
            raise ValueError(msg.format(len(data)))
        super(Data4DMixin, self).__init__(data, *args, **kwargs)


class DataNDMixin(object):
    """Validate n dimensional data."""
    def __init__(self, data, *args, **kwargs):
        if not len(data):
            raise ValueError('Data must not be empty.')
        if not all(map(lambda x: hasattr(x, '__iter__'), data)):
            raise ValueError('All data items must be a sequence type (e.g. a list).')
        super(DataNDMixin, self).__init__(data, *args, **kwargs)


class SameLengthDatasetMixin(object):
    """Make sure that each dataset in multi dimensional data has the same
    length."""
    def __init__(self, data, *args, **kwargs):
        if len(data) < 2:
            raise ValueError('Data must contain at least 2 datasets.')
        lengths = map(len, data)
        if len(set(lengths)) != 1:
            raise ValueError('All datasets in data must be of the same length.')
        super(SameLengthDatasetMixin, self).__init__(data, *args, **kwargs)