 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
from pprint import pprint
import serpscrap


class scrapper():
    keywords = []
    scrap = []

    def __init__(self, keywords):
        self.keywords = keywords
        self.scrap()
    
    def scrap(self):
        config = serpscrap.Config()
        config_new = {
           'cachedir': '/tmp/.serpscrap/',
           'clean_cache_after': 100,
           'database_name': '/tmp/serpscrap',
           'do_caching': True,
           'num_pages_for_keyword': 1,
           'scrape_urls': True,
           'search_engines': ['google'],
           'google_search_url': 'https://www.google.com/search?gl=us&hl=en',
           'executable_path': '/usr/local/bin/chromedriver',
        }
        config.apply(config_new)
        scrap = serpscrap.SerpScrap()
        scrap.init(config=config.get(), keywords=self.keywords)
        self.scrap = scrap.run()
    
    def simple(self):
        keys = ['serp_domain', 'serp_snippet', 'serp_title', 'text_raw']
        filter_scrap = []
        for result in self.scrap:
            filter_scrap.append({key: result[key] for key in set(keys).intersection(result.keys())})
        body_keys = ['serp_domain', 'serp_snippet', 'text_raw']
        for i, filter_result in enumerate(filter_scrap):
            filter_scrap[i]["title"] = filter_result.pop("serp_title")
            filter_scrap[i]["body"] = "".join([filter_result.pop(key) for key in set(body_keys).intersection(filter_result.keys())])
        return filter_scrap

