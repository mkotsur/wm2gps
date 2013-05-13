import xml.etree.ElementTree as ET
import urllib, sys, os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/gpxpy")

import gpxpy, gpxpy.gpx


url = "http://api.wikimapia.org/?function=box&bbox=" + sys.argv[1] + "&key=225F1176-F8C948A8-9334FE28-F51181B6-17749F78-D35641D3-789AD3AA-D7D26C75&count=10000&disable=polygon"

xmlContent = urllib.urlopen(url, 'r').read()
tree = ET.fromstring(xmlContent)
gpx = gpxpy.gpx.GPX()

for place in tree.findall('place'):
  location = place.find('location')
  gpx.waypoints.append(gpxpy.gpx.GPXWaypoint(location.find('lat').text, location.find("lon").text, name = place.find('name').text))
  
print gpx.to_xml()