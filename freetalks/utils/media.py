class Source(object):

    SEP='\0'

    def __init__(self, type, media_id, link_id=None):
        self.type = type
        self.media_id = media_id
        self.link_id = link_id

    @staticmethod
    def init(data):
        return Source(*data.split(Source.SEP))

    def data(self):
        data = [self.type, self.media_id]
        if self.link_id:
            data.append(self.link_id)
        return self.SEP.join(data)

    def __str__(self):
        return '%s: %s' % (self.type, self.media_id)

    def __unicode__(self):
        return unicode(self.__str__())

    @property
    def embed(self):
        if hasattr(self, '%s_embed' % self.type):
            return getattr(self, '%s_embed' % self.type)()
        return None

    @property
    def link(self):
        if hasattr(self, '%s_link' % self.type):
            return getattr(self, '%s_link' % self.type)()
        return None

    def validate(self):
        if not hasattr(self, '%s_embed' % self.type):
            raise ValueError('unknown type: %s' % self.type)
        if not isinstance(self.type, basestring):
            raise ValueError('type must be a string')
        if not isinstance(self.media_id, basestring):
            raise ValueError('media_id must be a string')
        if self.link_id is not None and not isinstance(self.link_id, basestring):
            raise ValueError('link_id must be None or a string')
        return True

    def bliptv_embed(self):
        return '<embed src="http://blip.tv/play/%s" type="application/x-shockwave-flash" ' \
               'width="480" height="350" allowscriptaccess="always" allowfullscreen="true" wmode="transparent">' \
               '</embed>' % self.media_id

    def bliptv_link(self):
        return 'http://blip.tv/file/%s/' % self.link_id

    def ted_embed(self):
        return """
            <object width="446" height="326">
                <param name="movie" value="http://video.ted.com/assets/player/swf/EmbedPlayer.swf"></param>
                <param name="allowFullScreen" value="true" /><param name="allowScriptAccess" value="always"/>
                <param name="wmode" value="transparent"></param>
                <param name="bgColor" value="#ffffff"></param>
                <param name="flashvars" value="vu=http://video.ted.com/talks/dynamic/%s-medium.flv&su=http://images.ted.com/images/ted/tedindex/embed-posters/GeroMisenboeck-2010G.embed_thumbnail.jpg&vw=432&vh=240&ap=0&ti=1000&introDuration=15330&adDuration=4000&postAdDuration=830&adKeys=talk=gero_miesenboeck;year=2010;theme=a_taste_of_tedglobal_2010;theme=unconventional_explanations;theme=new_on_ted_com;theme=how_the_mind_works;event=TEDGlobal+2010;&preAdTag=tconf.ted/embed;tile=1;sz=512x288;" />
                <embed src="http://video.ted.com/assets/player/swf/EmbedPlayer.swf" pluginspace="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" wmode="transparent" bgColor="#ffffff" width="446" height="326" allowFullScreen="true" allowScriptAccess="always" flashvars="vu=http://video.ted.com/talks/dynamic/%s-medium.flv&su=http://images.ted.com/images/ted/tedindex/embed-posters/GeroMisenboeck-2010G.embed_thumbnail.jpg&vw=432&vh=240&ap=0&ti=1000&introDuration=15330&adDuration=4000&postAdDuration=830&adKeys=talk=gero_miesenboeck;year=2010;theme=a_taste_of_tedglobal_2010;theme=unconventional_explanations;theme=new_on_ted_com;theme=how_the_mind_works;event=TEDGlobal+2010;"></embed>
                </object>""" % (self.media_id, self.media_id)

    def ted_link(self):
        return 'http://www.ted.com/talks/%s.html' % self.link_id

    def vimeo_embed(self):
        return '<iframe src="http://player.vimeo.com/video/%s" width="480" height="270" frameborder="0"></iframe>' \
        % self.media_id

    def vimeo_link(self):
        return 'http://vimeo.com/%s' % self.media_id

    def youtube_embed(self):
        return '<object width="640" height="385">' \
               '<param name="movie" value="http://www.youtube.com/v/%s?fs=1&amp;hl=en_US"></param>' \
               '<param name="allowFullScreen" value="true"></param>' \
               '<param name="allowscriptaccess" value="always"></param>' \
               '<embed src="http://www.youtube.com/v/%s?fs=1&amp;hl=en_US" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="640" height="385" wmode="transparent"></embed>' \
               '</object>' % (self.media_id, self.media_id)

    def youtube_link(self):
        return 'http://www.youtube.com/watch?v=%s' % self.media_id
