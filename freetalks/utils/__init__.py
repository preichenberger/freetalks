import re

SERIES_NAME = r'[a-zA-Z]{1}[a-zA-Z0-9_-]*'

SERIES_NAME_RE = re.compile(SERIES_NAME)
SLUGIFY_STRIP_RE = re.compile(r'[^\w\s-]')
SLUGIFY_HYPHENATE_RE = re.compile(r'[-\s]+')

def slugify(value):
    """
    Trent Mick
    New BSD License
    http://code.activestate.com/recipes/577257-slugify-make-a-string-usable-in-a-url-or-filename/

    From Django's "django/template/defaultfilters.py".
    """
    import unicodedata
    if not isinstance(value, unicode):
        value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(SLUGIFY_STRIP_RE.sub('', value).strip().lower())
    return SLUGIFY_HYPHENATE_RE.sub('-', value)
