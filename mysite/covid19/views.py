import base64
import io
import urllib
import matplotlib.pyplot as plt
import requests
from django.shortcuts import render

def chart(request):
    days = range(1,52)
    sweden = []
    norway = []

    swedenRequest = requests.get('https://api.covid19api.com/country/sweden/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-21T00:00:00Z') # March 1 - April 21
    norwayRequest = requests.get('https://api.covid19api.com/country/norway/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-21T00:00:00Z') # March 1 - April 21

    swedenData = swedenRequest.json()
    norwayData = norwayRequest.json()

    for i in range(51):
        sweden.append(swedenData[i]['Cases'])
        norway.append(norwayData[i]['Cases'])

    # plotting data
    plt.title("Sweden vs Norway Total Covid-19 Cases")
    plt.legend(["Sweden", "Norway"])
    plt.plot(days, sweden, color = 'gold')
    plt.plot(days, norway, color = 'firebrick')
    plt.ylabel('# of Confirmed Cases')
    plt.xlabel('March 1$^{st}$, 2020 to April 21$^{st}$, 2020')

    # generate figure and send it to the html template
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})
