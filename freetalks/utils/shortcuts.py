def get_by_id(type, id):
    if isinstance(id, basestring):
        if not id.isdigit():
            return None
        id = int(id)
    return type.get_by_id(id)
