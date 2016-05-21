from bottle import route, run, template
import calendar
import datetime


@route('/')
def index():
    cal_year = calendar.HTMLCalendar()
    return cal_year.formatmonth(datetime.date.today().year, datetime.date.today().month)

@route('/<year:int>/<month:int>/')
def index(year, month):
    cal_year = calendar.HTMLCalendar()
    return cal_year.formatmonth(year, month)

@route('/<year:int>/')
def index(year):
    cal_year = calendar.HTMLCalendar()
    return cal_year.formatyear(year)

if __name__ == "__main__":
    run(debug=True, reloader=True)