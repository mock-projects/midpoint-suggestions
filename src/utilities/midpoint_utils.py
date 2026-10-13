import csv
import os

from classes.activity import Activity
from classes.metro_graph import MetroGraph, Station
from classes.midpoint_request import MidpointRequest
from classes.user import User

def filter_activities_for_request(
	activities: list[Activity],
	request: MidpointRequest,
) -> list[Activity]:
	'''
	Filters activities given a request object.
	If those filters are too harsh, it returns any
	activities that have a matching activity category.
	'''
	# Fallback filter includes all activities of a matching category.
	fallback = [
		activity for activity in activities
		if activity.category == request.category
	]

	# Full filter includes all user request preferences.
	filtered = [
		activity for activity in fallback
		if activity.price_tier <= request.price_tier
		and activity.duration <= request.duration
		and activity.rating >= request.rating
	]

	return filtered if filtered else fallback

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

def load_midpoint_requests(
	larger_groups: bool = False,
) -> dict[str, MidpointRequest]:
	'''Loads midpoint data from the default file location.'''
	requests_by_id = {}
	users_by_id = load_users()

	file = 'midpoint-requests.csv'
	if larger_groups: file = 'group-midpoint-requests.csv'

	with open(os.path.join('src', 'data', file)) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			owner = users_by_id[row['owner_id']]

			# Load each participant and their selected location.
			user_locations: dict[User, tuple[float, float]] = {}
			participant_iterator = 1
			while f'participant{participant_iterator}_id' in row:
				# Get participant ID and location ID for this ordinal.
				participant_id = row[f'participant{participant_iterator}_id']
				location_id = row[f'location{participant_iterator}_id']
				# Get the user, and set their location.
				user = users_by_id[participant_id]
				user_locations[user] = user.locations[location_id]
				# Increment the iterator value.
				participant_iterator += 1

			requests_by_id[row['request_id']] = MidpointRequest(
				# Set core request data.
				request_id=row['request_id'],
				category=row['category'],
				rating=float(row['rating']),
				price_tier=float(row['price_tier']),
				duration=float(row['duration']),
				# Load and set specific user details.
				owner=owner,
				user_locations=user_locations,
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
