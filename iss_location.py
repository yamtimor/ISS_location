import requests
import json
import gmplot
import pandas

url = 'https://api.wheretheiss.at/v1/satellites/25544'
res = requests.get(url)
iss_json = res.json()


# print(iss_json)

def main():
    # extracting the coordinates from the json
    attractions_lats = iss_json['latitude']
    attractions_lngs = iss_json['longitude']

    # map creation and mark the iss on map
    gmap1 = gmplot.GoogleMapPlotter(attractions_lats,
                                attractions_lngs, 1)

    attractions_lats, attractions_lngs = zip(*[
    (iss_json['latitude'], iss_json['longitude'])])


    gmap1.scatter(attractions_lats, attractions_lngs, color='#3B0B39', size=40, marker=False)

    gmap1.scatter(attractions_lats, attractions_lngs, 'cornflowerblue', edge_width = 3.0)
    gmap1.draw( "C:\\Users\\yamti\\Desktop\\ISS\\gmap1.html" )

main()
