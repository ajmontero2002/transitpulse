import requests
from datetime import datetime
from google.transit import gtfs_realtime_pb2
from db import init_db, save_vehicles

FEED_URL = "https://cdn.mbta.com/realtime/VehiclePositions.pb"

def fetch_feed(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    return feed

def main():
    init_db()
    feed = fetch_feed(FEED_URL)

    rows = []
    for entity in feed.entity:
        if not entity.HasField("vehicle"):
            continue
        v = entity.vehicle
        rows.append((
            v.vehicle.id,
            v.trip.route_id,
            v.position.latitude,
            v.position.longitude,
            v.timestamp,
        ))
    save_vehicles(rows)
    print(f"Saved {len(rows)} vehicles to the database")


if __name__ == "__main__":
    main()
