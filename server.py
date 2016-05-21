from bottle import route, run, template
import calendar
import datetime


@route('/')
@route('/<year:int>/<month:int>/')
def index(year=None, month=None):
    if not year:
        year = int(datetime.date.today().year)
        month = int(datetime.date.today().month)
    cal_year = calendar.HTMLCalendar()

    if month == 12:
        pyear = year
        pmonth = month - 1
        nyear = year + 1
        nmonth = 1
    elif month == 1:
        pyear = year - 1
        pmonth = 12
        nyear = year
        nmonth = month + 1
    else:
        pyear = year
        pmonth = month - 1
        nyear = year
        nmonth = month + 1
    end = template('<br><a href="/{{pyear}}/{{pmonth}}/">Prev</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                   '<a href="/{{nyear}}/{{nmonth}}/">Next</a>', pyear=pyear, pmonth=pmonth, nyear=nyear, nmonth=nmonth)
    return cal_year.formatmonth(year, month) + end

@route('/<year:int>/')
def index(year):
    cal_year = calendar.HTMLCalendar()
    end = template('<br><a href="/{{pyear}}/">Prev</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                   '<a href="/{{nyear}}/">Next</a>', pyear=year-1, nyear=year+1)
    return cal_year.formatyear(year) + end

if __name__ == "__main__":
    run(debug=True, reloader=True)