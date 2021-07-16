from flask import request, redirect, url_for, render_template, flash
from . import covid
from .covi import Covid
from datetime import datetime
covid_obj = Covid()
from matplotlib import pyplot as plt

@covid.route("/stats", methods=["GET", "POST"])
def stats():
    summary_cases, current_date = covid_obj.get_summary_cases()
    countries_avail = covid_obj.get_countries()
    dates_world, values_world = covid_obj.get_days_value_world(7, "TotalConfirmed")
    queried_value = "Newly Confirmed Cases"
    nr_days = 7

    if request.method == "POST":
        if "country_select" in request.form:
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
        if "world-value-select" in request.form:
            nr_days = request.form["world-days-select"]
            queried_value = request.form["world-value-select"]
            dates_world, values_world = covid_obj.get_days_value_world(nr_days, queried_value)
            return render_template("covid/stats.html", cases = summary_cases, country= countries_avail,dates_world = dates_world, values_world = values_world, nr_days = nr_days, queried_value = queried_value)


    return render_template("covid/stats.html", 
                            cases = summary_cases, 
                            country = countries_avail,
                            dates_world = dates_world,
                            values_world = values_world,
                            queried_value = queried_value,
                            nr_days = nr_days,
                            current_date = current_date)
                            

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

@covid.route("/numbers/<country_name>/<days>/<value>", methods=["GET"])
def numbers(country_name, days, value):
    dates, values = covid_obj.get_days_value(country_name, days, value)
    return render_template("covid/numbers.html", dates = dates, values=values, country=country_name, value=value, days = days)

@covid.route("/world/<days>/<value>", methods=["GET"])
def world(days, value):
    dates_world, values_world = covid_obj.get_days_value_world(days, value)
    return render_template("covid/world.html", dates_world=dates_world, values_world=values_world, days = days, value = value)
