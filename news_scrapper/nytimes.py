from news_scrapper.scrapper import BaseScrapper

class NytScrapper(BaseScrapper):
    NAME = "New York Times"
    def __init__(self):
        # set base url
        self.set_base_url('https://www.nytimes.com')
        
        # set categories
        self.set_categories({
            'technology' : '/international/section/technology',
            'entertainment' : '/spotlight/pop-culture',
            'finance' : '/international/section/business',
            'sports' : '/international/section/sports',
            'fashion' : '/international/section/fashion',
            'health' : '/international/section/health'
        })

        # set article attributes
        self.set_article_attrs(
            {
                'article' : {'css' : 'li.css-18yolpw', 'element' : 'li'},
                'url' : {'css': 'div.css-14ee9cx a[href]', 'element' : 'a'},
                'date' : {'css': 'div.css-agsgss.e15t083i3 > span', 'element' : 'span'},
                'title' : {'css' : '.css-1kv6qi.e15t083i0', 'element' : 'h3'},
                'description' : {'css' : 'p.css-1pga48a.e15t083i1', 'element' : 'p'},
                'img_url' : {'css': 'img.css-rq4mmj[src]', 'element' : 'img'},
            }
        )