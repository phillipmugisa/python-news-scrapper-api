from news_scrapper.google_news import GoogleNewsScrapper
from news_scrapper.nytimes import NytScrapper
from news_scrapper.yahoo_news import YahooNewsScrapper

def run_scrapper():
    nyt_scrapper = NytScrapper()
    google_scrapper = GoogleNewsScrapper()
    yahoo_news_scrapper = YahooNewsScrapper()        

    # fetch data

    scrapped_data = []
    for cls in [nyt_scrapper, google_scrapper, yahoo_news_scrapper]:
        try:
            results = cls.run()
            data = {
                "source": cls.get_name(),
                "url": cls.get_base_url(),
                "results": results
            }
            scrapped_data.append(data)
        except Exception as err:
            print(f"Error scraping {cls.get_name()}: {err}")

    return scrapped_data

if __name__ == "__main__":
    scraped_data = run_scrapper()
    print(scraped_data)
