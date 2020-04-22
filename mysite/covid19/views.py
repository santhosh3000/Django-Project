import base64
import io
import urllib
import matplotlib.pyplot as plt
import requests

from django.shortcuts import render

def chart(request):
    dates = range(1,52)
    sweden = []
    denmark = []

    swedenRequest = requests.get('https://api.covid19api.com/country/sweden/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-21T00:00:00Z')
    denmarkRequest = requests.get('https://api.covid19api.com/country/norway/status/confirmed?from=2020-03-01T00:00:00Z&to=2020-04-21T00:00:00Z')

    swedenData = swedenRequest.json()
    denmarkData = denmarkRequest.json()

    for i in range(51):
        sweden.append(swedenData[i]['Cases'])
        denmark.append(denmarkData[i]['Cases'])


    # plot the data
    plt.title("Sweden vs Denmark Total Covid-19 Cases")

    plt.plot(dates, sweden, color = 'gold')
    plt.plot(dates, denmark, color = 'firebrick')

    plt.legend(["Sweden", "Denmark"])

    plt.xlabel('March 1$^{st}$, 2020 to April 21$^{st}$, 2020')
    plt.ylabel('# of Confirmed Cases')


    # generate figure and send it to the html template
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})
