import csv
import os

from classes.activity import Activity
from classes.metro_graph import MetroGraph, Station
from classes.user_request import UserRequest

def load_metro_graph() -> MetroGraph:
	'''Loads metro stations and connections from disk to create metro map.'''
	graph = MetroGraph()

	# Load stations into metro graph
	with open(os.path.join('src', 'data', 'metro-stations.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			name = row['station']
			coordinates = float(row['latitude']), float(row['longitude'])
			station = Station(name, coordinates)
			graph.add_station(station)

	# Load station connections into graph
	with open(os.path.join('src', 'data', 'metro-timetable.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			start_station = row['start']
			end_station = row['end']
			time = float(row['time_between_stops'])
			if start_station in graph.stations and end_station in graph.stations:
				graph.add_connection(start_station, end_station, time)
			else:
				raise Exception(
					f'Stations {start_station} and/or {end_station} not found in the graph.'
				)

	return graph

def load_user_requests() -> list[UserRequest]:
	user_requests = []
	with open(os.path.join('src', 'data', 'user-requests.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			user_requests.append(
				UserRequest(
					user_id=row['owner_id'],
					user1_location=(
						float(row['l1_latitude']),
						float(row['l1_longitude']),
					),
					user2_location=(
						float(row['l2_latitude']),
						float(row['l2_longitude']),
					),
					activity_type=row['category'],
					rating=float(row['rating']),
					price_category=float(row['price_tier']),
					time_needed=float(row['duration']),
				)
			)
	return user_requests

def load_activities() -> list[Activity]:
	activities = []
	with open(os.path.join('src', 'data', 'activities.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			activities.append(
				Activity(
					name=row['name'],
					coordinates=(float(row['latitude']), float(row['longitude'])),
					activity_type=row['category'],
					rating=float(row['rating']),
					price_category=float(row['price_tier']),
					time_needed=float(row['duration']),
				)
			)
	return activities
