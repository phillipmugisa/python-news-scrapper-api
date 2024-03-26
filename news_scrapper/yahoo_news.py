from news_scrapper.scrapper import BaseScrapper

class YahooNewsScrapper(BaseScrapper):
    NAME = "Yahoo News"
    def __init__(self):
        # set base url
        self.set_base_url('https://www.yahoo.com')

        # query parameters
        self.country = 'US'
        
        # set categories
        self.set_categories({
            'technology' : 'https://finance.yahoo.com/tech',
            'entertainment' : 'https://www.yahoo.com/entertainment',
            'finance' : 'https://finance.yahoo.com',
            'sports' : 'https://sports.yahoo.com'
        })

        # set article attributes
        self.set_article_attrs(
            {
                'article' : {'css' : 'li.js-stream-content', 'element' : 'li'},
                'url' : {'css' : 'h3 a', 'element' : 'a'},
                'description' : {'css' : 'p', 'element' : 'p'},
                'title' : {'css' : 'h3 a', 'element' : 'a'},
                'img_url' : {'css': 'img[src]', 'element' : 'img'},
            }
        )

    def get_fetch_url(self, category):
        return self.get_category_link(category)

    def get_article_link(self, element, category=None):
        return '{}{}'.format(self.get_fetch_url(category), element.get('href', None))