 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
from pprint import pprint
import serpscrap

class scrapper():
    keywords=[]
    scrap=[]
    def __init__(self,keywords):
        self.keywords=keywords
        self.scrap()
    
    def scrap(self):
        config = serpscrap.Config()
        config.set('scrape_urls', True)
        
        scrap = serpscrap.SerpScrap()
        scrap.init(config=config.get(), keywords=self.keywords)
        self.scrap = scrap.run()
    
    def simple_scrap(self):
        keys=['serp_domain', 'serp_snippet','serp_title','text_raw']
        filter_scrap=[]
        for result in self.scrap:
            filter_scrap.append({key: result[key] for key in set(keys).intersection(result.keys())})
            
        body_keys=['serp_domain', 'serp_snippet','text_raw']
        for i,filter_result in enumerate(filter_scrap):
            
            filter_scrap[i]["title"] = filter_result.pop("serp_title")
            print(filter_scrap[i].keys())
            filter_scrap[i]["body"]={filter_result.pop(key) for key in set(body_keys).intersection(filter_result.keys())}

        
        return filter_scrap
    
scrape=scrapper(['coronavirus'])
result=scrape.simple_scrap()
pprint(result)
