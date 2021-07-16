import json
import requests
from datetime import datetime

class Covid:
    def __init__(self):
        self.summary_url = "https://api.covid19api.com/summary"
        self.status_url = "https://api.covid19api.com/country/{}"
        self.world_url = "https://api.covid19api.com/world"
   
    def get_summary_cases(self):
        self.cases = {}

        res = requests.get(self.summary_url).json()

        try:
            cases = res["Global"]
        except:
            return None
        date = datetime.strptime(res["Date"], "%Y-%m-%dT%H:%M:%S.%fZ")
        current_date = date.strftime("%d. %b") 

    
    #Getting the heads(keys()) of "Global" key
    #making a new "cases" dict without the last element of the summary (date)            
        headers = ["New Confirmed" , "Total Confirmed" , "New Deaths" , "Total Deaths" , "New Recovered" , "Total Recovered"]
        for key, value in zip(headers, list(cases.values())[:-1]):
                self.cases[key] = value

        return self.cases, current_date

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

    #Creates nested dict with LAST 7 days as keys for queried country 
    def get_country_seven_days(self , slug_name) -> dict:
        res = requests.get(self.status_url.format(slug_name)).json()[-7:]
        dates = {}
        for i,date in enumerate(res):
            dates[res[i]["Date"]] = {"Confirmed":res[i]["Confirmed"], "Deaths":res[i]["Deaths"], "Recovered":res[i]["Recovered"], "Active":res[i]["Active"]}

        return dates
    def get_days_value(self, slug_name, days, value) ->dict:
        res = requests.get(self.status_url.format(slug_name)).json()[-int(days):]
        dates = []
        active = []
        for i,date in enumerate(res):
            time = datetime.strptime(res[i]["Date"], "%Y-%m-%dT%H:%M:%SZ")
            dates.append(time.strftime("%d. %b"))
            active.append(res[i][value])
        return dates, active
    #datetime objects needs to be sorted !
    def get_days_value_world(self, days, value) ->dict:
        res = requests.get(self.world_url).json()[-int(days):]
        res_sorted = sorted(res, key=lambda k: k["Date"])
        dates_world = []
        value_world = []
        for i in range(0, len(res_sorted)):
            time = datetime.strptime(res_sorted[i]["Date"], "%Y-%m-%dT%H:%M:%S.%fZ")
            dates_world.append(time.strftime("%d. %b"))
            value_world.append(res_sorted[i][value])

        
        return dates_world, value_world

            

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
