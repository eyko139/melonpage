from flask import request, redirect, url_for, render_template
from . import covid
from .covi import Covid

covid_obj = Covid()

@covid.route("/stats", methods=["GET", "POST"])
def stats():
    if request.method == "POST":
        selected_country = request.form["country_select"]
        country_date = covid_obj.get_status_of_one(selected_country)

        return redirect(url_for("covid.country",
                                country_name=selected_country,
                                date=country_date["Date"]
                            ))


    summary_cases = covid_obj.get_summary_cases()
    countries_avail = covid_obj.get_countries()


    return render_template("covid/stats.html", 
                            cases = summary_cases, 
                            country = countries_avail)
                            

@covid.route("/stats/<country_name>/<date>", methods=["GET", "POST"])
def country(country_name, date):
    cases = covid_obj.get_status_of_one(country_name)
    dates = covid_obj.get_country_dates(country_name)
    obs = covid_obj.get_country_on_date(country_name, date)
    if request.method == "POST":
        selected_date = request.form["country_date"]
        return redirect(url_for("covid.country",
                                country_name=country_name,
                                date=selected_date))

    return render_template("covid/country.html", country = country_name,
                            cases = obs,
                            dates = dates)
