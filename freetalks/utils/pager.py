LIMIT = 10

class Pager(object):

    def __init__(self, query, request):
        self.query = query
        self.request = request

        try:
            limit = int(request.get('limit', LIMIT))
        except:
            limit = LIMIT

        try:
            page = int(request.get('page', 0))
        except Exception, error:
            page = 0

        self.limit = limit if limit > 0 and limit < 100 else 10
        self.page = page if page > 0 else page
        self.offset = self.page * self.limit

    @property
    def objects(self):
        if not hasattr(self, '_objects'):
            objects = self.query.fetch(self.limit+1, self.offset)
            self._has_next = len(objects) > self.limit
            self._objects = objects[:self.limit] if self._has_next else objects
        return self._objects

    @property
    def has_previous(self):
        return self.offset > 0

    @property
    def has_next(self):
        if not hasattr(self, '_has_next'):
            self.objects
        return self._has_next

    @property
    def previous_url(self):
        if self.has_previous:
            page = self.page - 1
            if page > 0:
                return '%s?page=%s&limit=%s' % (self.request.path, page, self.limit)
            elif self.limit != LIMIT:
                return '%s?limit=%s' % (self.request.path, self.limit)
            else:
                return self.request.path

    @property
    def next_url(self):
        if self.has_next:
            return '%s?page=%s&limit=%s' % (self.request.path, self.page+1, self.limit)

    def __iter__(self):
        return self.objects.__iter__()

    def __nonzero__(self):
        return bool(self.objects)

    def next(self):
        return self.objects.next()
