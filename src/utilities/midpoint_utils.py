import csv
import os

from classes.activity import Activity
from classes.metro_graph import MetroGraph, Station
from classes.midpoint_request import MidpointRequest
from classes.user import User

def load_activities() -> dict[str, Activity]:
	'''Loads activities from the default activities data file location.'''
	activities_by_id = {}
	with open(os.path.join('src', 'data', 'activities.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			activities_by_id[row['activity_id']] = Activity(
				activity_id=row['activity_id'],
				name=row['name'],
				category=row['category'],
				coordinates=(
					float(row['latitude']),
					float(row['longitude'])
				),
				rating=float(row['rating']),
				price_tier=float(row['price_tier']),
				duration=float(row['duration']),
			)

	return activities_by_id

def load_users() -> dict[str, User]:
	'''Loads users from the default user data file location.'''
	users_by_id: dict[str, User] = {}
	with open(os.path.join('src', 'data', 'users.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			user_id = row['user_id']
			user = users_by_id.get(user_id)

			# If the user doesn't exist yet, create one.
			if user is None:
				user = User(user_id)
				users_by_id[user_id] = user

			# Save location data.
			# A user can have multiple saved locations.
			user.locations[row['location_id']] = (
				float(row['latitude']),
				float(row['longitude']),
			)

	return users_by_id

def load_midpoint_requests() -> dict[str, MidpointRequest]:
	'''Loads midpoint data from the default file location.'''
	requests_by_id = {}
	users_by_id = load_users()

	with open(os.path.join('src', 'data', 'midpoint-requests.csv')) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			owner = users_by_id[row['owner_id']]
			user1 = users_by_id[row['participant1_id']]
			user2 = users_by_id[row['participant2_id']]

			requests_by_id[row['request_id']] = MidpointRequest(
				# Set core request data.
				request_id=row['request_id'],
				category=row['category'],
				rating=float(row['rating']),
				price_tier=float(row['price_tier']),
				duration=float(row['duration']),
				# Load and set specific user details.
				owner=owner,
				user1=user1,
				user2=user2,
				user1_location=user1.locations[row['location1_id']],
				user2_location=user2.locations[row['location2_id']],
			)

	return requests_by_id

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
				raise KeyError(
					f'Stations {start_station} and/or ' +
					f'{end_station} not found in the graph.'
				)

	return graph
