from flask import request, redirect, url_for, render_template, flash
from . import covid
from .covi import Covid
from datetime import datetime
covid_obj = Covid()

@covid.route("/stats", methods=["GET", "POST"])
def stats():
    if request.method == "POST":
        try:
            selected_country = request.form["country_select"]
            country_date = covid_obj.get_status_of_one(selected_country)

            return redirect(url_for("covid.country",
                                country_name=selected_country,
                                date=country_date["Date"]
                            ))
        except:
            selected_country = request.form["country_select"]
            flash("Sorry no data for " + selected_country, "error")
            return redirect(url_for("covid.stats"))


    summary_cases = covid_obj.get_summary_cases()
    countries_avail = covid_obj.get_countries()


    return render_template("covid/stats.html", 
                            cases = summary_cases, 
                            country = countries_avail)
                            

@covid.route("/stats/<country_name>/<date>", methods=["GET", "POST"])
def country(country_name, date):
    try:
        cases = covid_obj.get_status_of_one(country_name)
        dates = covid_obj.get_country_dates(country_name)
        obs = covid_obj.get_country_on_date(country_name, date)
        if request.method == "POST":
            selected_date = request.form["country_date"]
            unprettyfy_time = datetime.strptime(selected_date, "%d. %b %Y")
            selected_date = datetime.strftime(unprettyfy_time, "%Y-%m-%dT%H:%M:%SZ")
            return redirect(url_for("covid.country",
                                    country_name=country_name,
                                date=selected_date))
    except:
        return redirect(url_for("covid.stats"))

    return render_template("covid/country.html", country = country_name,
                            cases = obs,
                            dates = dates)
