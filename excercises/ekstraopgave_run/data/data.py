import gpxpy


gpx_file = open('C:\Users\Tec\Python-og-DataAnalyse-1\exercises\ekstraopgave_run\activity_7403521010.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

def main():
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

    for waypoint in gpx.waypoints:
        print('waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))

    for route in gpx.routes:
        print('Route:')
        for point in route.points:
            print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))





if __name__ == "__main__":
    main()



print('GPX:', gpx.to_xml())
