import pandas

pandas.read_json("tripadvisor.json").to_csv("tripadvisor.csv", encoding='utf-8-sig')