from pattern.web import URL, extension, SearchEngine, plaintext, Spider, Bing, Google 
from pattern.en import parse, tag, pprint, Text

class WebPageParser:
    def __init__(self, url_string='http://www.amazon.com/gp/product/0761147489/'):
        raw_html = URL(url_string).download()
        #strip content
        self.clean_text = plaintext(raw_html) 
        print self.clean_text
        
    def analyze(self):
        text = Text(self.clean_text)
        for sentence in text:
            print '-----SENTENCE'+str(sentence.string)
            print sentence.subjects
            print sentence.verbs
            for word in sentence:
                print word.string
                print word.lemma
                print word.type
                print word.chunk
                    

class GoogleSearch:
    def __init__(self, query=''):
        engine = Google(license=None, throttle=0.5, language=None)
        c=0        
        for i in range(1,5):
            results = engine.search(query, start=i)
            for result in results:
                c+=1
                print c
                print result.url+':'+result.title
                print repr(plaintext(result.text))
                print "" 
                                                
class WebSpider(Spider):
    def run(self):
        while not self.done:
            self.crawl(method=3, cached=False, throttle=1)
        
    def follow(self, link):
        #print 'follow:'+link.url+' '+link.text
        return True 
    
    def visit(self, link, source=None):
        print 'visited:', repr(link.url), 'from:', link.referrer
        clean_text = self.sanitize(plaintext(source))
        print clean_text
        
    def fail(self, link):
        print 'failed:', repr(link.url)
        
        
    def sanitize(self, clean_text):
        #remove stop words
        
        #lower case
        
        #stemming
        
        #lemmatize 
        
        
        return clean_text
        