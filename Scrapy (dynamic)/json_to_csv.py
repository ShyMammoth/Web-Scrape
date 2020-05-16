#!/usr/bin/env python

import pandas
import os
import re

mypath = os.getcwd() 
scraped = []

# Store absolute paths of scraped files in a list
for file in os.listdir("scraped_json"):
    filename = os.path.join(mypath, "scraped_json")
    scraped.append(os.path.join(filename, file))

# Create absolute path of processed files
output = os.path.join(mypath, "converted_csv")

print("Files converted:\n")
for i in scraped:
    filename = repr(i)
    filename = re.findall(r'(\w*).json', filename)[1] # Resistent in formatting batches of .json to .csv
    pandas.read_json(i).to_csv(os.path.join(output, "{}.csv".format(filename)), encoding='utf-8-sig')
    print(filename)
print("\nJob completed")
