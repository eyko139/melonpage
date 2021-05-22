import json
import requests
from datetime import datetime

class Covid:
    def __init__(self):
        self.summary_url = "https://api.covid19api.com/summary"
        self.status_url = "https://api.covid19api.com/country/{}"
   
    def get_summary_cases(self):
        self.cases = {}

        res = requests.get(self.summary_url).json()

        try:
            cases = res["Global"]
        except:
            return None
    
    #Getting the heads(keys()) of "Global" key
    #making a new "cases" dict without the last element of the summary (date)            
        headers = ["New Confirmed" , "Total Confirmed" , "New Deaths" , "Total Deaths" , "New Recovered" , "Total Recovered"]
        for key, value in zip(headers, list(cases.values())[:-1]):
                self.cases[key] = value

        return self.cases

    def get_countries(self):
        res = requests.get('https://api.covid19api.com/countries').json()
        
        self.countries = {}

        for response in res:
            self.countries[response["Country"]] = response["Slug"]
        return dict(sorted(self.countries.items(), key = lambda x: x[1]))

    def get_status_of_one(self , slug_name) -> dict:
        res = requests.get(self.status_url.format(slug_name)).json()[-1]

        self.cases = {}

        for i in ['Confirmed' , 'Deaths' , 'Recovered' , 'Active', "Date"]:
            self.cases[i] = res[i]
        
        return self.cases
   #Finding the json entry of the corresponding country on the requested time
   #and prettifying the timestamp into datetime obj
    def get_country_on_date(self, slug_name, date):
        res = requests.get(self.status_url.format(slug_name)).json()
        for obs in res:
            if obs["Date"] == date:
                date_found = obs
                pretty_time = datetime.strptime(date_found["Date"], "%Y-%m-%dT%H:%M:%SZ")
                date_found["Date"] = pretty_time.strftime("%d. %b %Y")


        self.cases = {}
        for i in ['Confirmed' , 'Deaths' , 'Recovered' , 'Active', "Date"]:
                self.cases[i] = date_found[i]
                
        return self.cases
    def get_country_dates(self, slug_name):
        res = requests.get(self.status_url.format(slug_name)).json()
        date_list = []
        for obs in res:
            #cant prettyfiy date here, gets parsed to the view fucntion
            pretty_time = datetime.strptime(obs["Date"], "%Y-%m-%dT%H:%M:%SZ")
            obs["Date"] = pretty_time.strftime("%d. %b %Y")
            date_list.append(obs["Date"])

        return date_list[::-1]







# x = Covid()
# x.get_summary_cases()
# print(x.get_countries())
# print(x.get_status_of_one("yemen"))
