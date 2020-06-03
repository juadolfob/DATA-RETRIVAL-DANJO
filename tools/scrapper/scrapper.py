# !/usr/bin/python3
# -*- coding: utf-8 -*-

import serpscrap

class scrapper():
    keywords = []
    scrap = []

    def __str__(self):
        return self.scrap

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
            'google_search_url': 'https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr',
            'executable_path': '/tools/chromedriver',
        }
        config.apply(config_new)
        scrap = serpscrap.SerpScrap()
        scrap.init(config=config.get(), keywords=self.keywords)
        self.scrap = scrap.run()

    def remove_from_domain(self, domains):
        if isinstance(domains, str):
            for scrap in self.scrap[:]:
                if scrap["serp_domain"] == domains:
                    self.scrap.remove(scrap)
        elif '__iter__' in dir(domains):
            for domain in domains:
                self.remove_from_domain(domain)
        else:
            raise Exception("Using " + str(type(domains)) + ", but only string or iterables string are allowed")
        return self

    def simple(self):
        return [{'title':result["serp_domain"],'snippet':result["serp_snippet"],'body':result["text_raw"]} for result in self.scrap if "text_raw" in result and result["text_raw"]]