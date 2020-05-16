#!/usr/bin/env bash

rm scraped_json/rice.json
scrapy crawl rice -o scraped_json/rice.json

./json_to_csv.py
