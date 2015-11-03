__author__ = 'cjoakim'

import xml.sax


class BaseHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.heirarchy = list()
        self.completed = False
        self.curr_text = ''

    def endDocument(self):
        self.completed = True

    def characters(self, chars):
        print(chars)
        if self.curr_text:
            self.curr_text = self.curr_text + chars
        else:
            self.curr_text = chars

    def reset_text(self):
        self.curr_text = ''

    def current_path(self):
        return '|'.join(self.heirarchy)


