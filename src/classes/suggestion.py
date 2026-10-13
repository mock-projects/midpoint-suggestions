import math

from classes.activity import Activity
from classes.eta_calculator import ETACalculator
from classes.midpoint_request import MidpointRequest
from classes.user import User
from utilities.midpoint_utils import filter_activities_for_request

class Suggestion:
	'''
	A suggestion is an activity recommended
	based on a given user midpoint request.
	'''

	def __init__(
		self,
		activity: Activity,
		etas: dict[User, float]
	):
		self.activity = activity
		self.etas = etas
		self.users = [*etas.keys()]

	def print_details(self):
		print(f'Suggested activity: {self.activity}')
		for user, eta in self.etas.items():
			print(f'Distance from {user}: {eta}')

def suggest_midpoint_activity(
	eta_calculator: ETACalculator,
	request: MidpointRequest,
	activities: list[Activity],
) -> Suggestion | None:
	'''
	Returns a suggested activity that's
	somewhere between the users' locations.
	'''
	activities = filter_activities_for_request(activities, request)

	# Suggest the activity with best distance score.
	best_activity: Activity | None = None
	best_distance_score = math.inf
	for activity in activities:
		# Obtain the distances from the users to the activity.
		# (This is NOT the ETA, which is expensive to get)
		distances = [
			ETACalculator.haversine(location, activity.coordinates)
			for location in request.user_locations.values()
		]

		# Squaring both ETAs will prefer locations closer to the midpoint of the two users.
		# Calculate a distance score by averaging the squared user distances.
		# To make the number more "realistic", we'll also take the square root at the end.
		distance_score = math.sqrt(
			sum((distance ** 2) for distance in distances) / len(distances)
		)

		# If this combined eta score is lower, then it is better!
		if best_activity == None or distance_score < best_distance_score:
			best_activity = activity
			best_distance_score = distance_score

	if best_activity == None: return None

	# Calculate ETAs to the "best" location.
	etas = {
		user: eta_calculator.calculate_eta(location, best_activity.coordinates)
		for [user, location] in request.user_locations.items()
	}

	# Return a new instance of a activity suggestion.
	return Suggestion(best_activity, etas)
