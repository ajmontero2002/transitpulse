import requests
from datetime import datetime
from google.transit import gtfs_realtime_pb2

FEED_URL = "https://cdn.mbta.com/realtime/VehiclePositions.pb"

def fetch_feed(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    return feed

def main():
    feed = fetch_feed(FEED_URL)
    print(f"Vehicles in feed: {len(feed.entity)}")

    
    for entity in feed.entity[:5]:
        if not entity.HasField('vehicle'):
            continue
        v = entity.vehicle
        route = v.trip.route_id
        vehicle_id = v.vehicle.id
        lat = v.position.latitude
        lon = v.position.longitude
        time = datetime.fromtimestamp(v.timestamp)
        
        print(f"Vehicle ID: {vehicle_id}, Route: {route}, Position: ({lat}, {lon}), Time: {time}")


if __name__ == "__main__":
    main()
