from news_scrapper.scrapper import BaseScrapper

class GoogleNewsScrapper(BaseScrapper):
    NAME = "Google News"
    def __init__(self):
        # set base url
        self.set_base_url('https://news.google.com/topics')

        # query parameters
        self.country = 'US'
        
        # set categories
        self.set_categories({
            'technology' : '/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKVlJ5Z0FQAQ',
            'entertainment' : '/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKVlJ5Z0FQAQ',
            'finance' : '/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKVlJ5Z0FQAQ',
            'sports' : '/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKVlJ5Z0FQAQ',
            'health' : '/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE'
        })

        # set article attributes
        self.set_article_attrs(
            {
                'article' : {'css' : 'article.IBr9hb', 'element' : 'article'},
                'url' : {'css': '.WwrzSb', 'element' : 'a'},
                'date' : {'css': '.hvbAAd', 'element' : 'time'},
                'title' : {'css' : '.gPFEn', 'element' : 'a'},
                'img_url' : {'css': 'img.Quavad', 'element' : 'img'},
            }
        )

    def get_date(self, element):
        return element.datetime
        
    def get_article_link(self, element, category=None):
        return 'https://news.google.com{}'.format(element.get('href', None)[1:])