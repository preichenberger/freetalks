class Source(object):

    def __init__(self, media_id, link_id=None):
        self.media_id = media_id
        self.link_id = link_id

    @property
    def embed(self):
        raise Exception('Source type not implemented.')

    @property
    def link(self):
        raise Exception('Source type not implemented.')

class BlipTv(Source):

    @property
    def embed(self):
        return '<embed src="http://blip.tv/play/%s" type="application/x-shockwave-flash" ' \
               'width="480" height="350" allowscriptaccess="always" allowfullscreen="true">' \
               '</embed>' % self.media_id

    @property
    def link(self):
        return 'http://blip.tv/file/%s/' % self.link_id

map = {
    'blip.tv': BlipTv,
}

def get(type_, media_id, link_id=None):
    return map.get(type_, Source)(media_id, link_id)
