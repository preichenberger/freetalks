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

class Ted(Source):

    @property
    def embed(self):
        return """
            <object width="446" height="326">
                <param name="movie" value="http://video.ted.com/assets/player/swf/EmbedPlayer.swf"></param>
                <param name="allowFullScreen" value="true" /><param name="allowScriptAccess" value="always"/>
                <param name="wmode" value="transparent"></param>
                <param name="bgColor" value="#ffffff"></param>
                <param name="flashvars" value="vu=http://video.ted.com/talks/dynamic/%s-medium.flv&su=http://images.ted.com/images/ted/tedindex/embed-posters/GeroMisenboeck-2010G.embed_thumbnail.jpg&vw=432&vh=240&ap=0&ti=1000&introDuration=15330&adDuration=4000&postAdDuration=830&adKeys=talk=gero_miesenboeck;year=2010;theme=a_taste_of_tedglobal_2010;theme=unconventional_explanations;theme=new_on_ted_com;theme=how_the_mind_works;event=TEDGlobal+2010;&preAdTag=tconf.ted/embed;tile=1;sz=512x288;" />
                <embed src="http://video.ted.com/assets/player/swf/EmbedPlayer.swf" pluginspace="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" wmode="transparent" bgColor="#ffffff" width="446" height="326" allowFullScreen="true" allowScriptAccess="always" flashvars="vu=http://video.ted.com/talks/dynamic/%s-medium.flv&su=http://images.ted.com/images/ted/tedindex/embed-posters/GeroMisenboeck-2010G.embed_thumbnail.jpg&vw=432&vh=240&ap=0&ti=1000&introDuration=15330&adDuration=4000&postAdDuration=830&adKeys=talk=gero_miesenboeck;year=2010;theme=a_taste_of_tedglobal_2010;theme=unconventional_explanations;theme=new_on_ted_com;theme=how_the_mind_works;event=TEDGlobal+2010;"></embed>
                </object>""" % (self.media_id, self.media_id)

    @property
    def link(self):
        return 'http://www.ted.com/talks/%s.html' % self.link_id

class Vimeo(Source):

    @property
    def embed(self):
        return '<iframe src="http://player.vimeo.com/video/%s" width="480" height="270" frameborder="0"></iframe>' \
        % self.media_id

    @property
    def link(self):
        return 'http://vimeo.com/%s' % self.link_id

class YouTube(Source):

    @property
    def embed(self):
        return '<object width="640" height="385">' \
               '<param name="movie" value="http://www.youtube.com/v/%s?fs=1&amp;hl=en_US"></param>' \
               '<param name="allowFullScreen" value="true"></param>' \
               '<param name="allowscriptaccess" value="always"></param>' \
               '<embed src="http://www.youtube.com/v/%s?fs=1&amp;hl=en_US" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="640" height="385"></embed>' \
               '</object>' % (self.media_id, self.media_id)

    @property
    def link(self):
        return 'http://www.youtube.com/watch?v=%s' % self.link_id

map = {
    'blip.tv': BlipTv,
    'ted': Ted,
    'vimeo': Vimeo,
    'youtube': YouTube,
}

def get(type_, media_id, link_id=None):
    return map.get(type_, Source)(media_id, link_id)
