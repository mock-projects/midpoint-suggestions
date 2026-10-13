from classes.activity import Activity
from classes.eta_calculator import ETACalculator
from classes.midpoint_request import MidpointRequest

class Suggestion:
	'''
	A suggestion is an activity recommended
	based on a given user midpoint request.
	'''

	def __init__(self, activity: Activity, user1_eta: float, user2_eta: float):
		self.activity = activity
		self.user1_eta = user1_eta
		self.user2_eta = user2_eta

	def print_details(self):
		print(f'Suggested activity: {self.activity}')
		print(f'Distance from User 1: {self.user1_eta} minutes')
		print(f'Distance from User 2: {self.user2_eta} minutes')

def suggest_midpoint_activity(
	eta_calculator: ETACalculator,
	request: MidpointRequest,
	activities: list[Activity],
) -> Suggestion | None:
	'''Returns a suggested activity that's somewhere between the users' locations.'''
	# TODO
	pass
