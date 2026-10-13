from classes.activity import Activity
from classes.eta_calculator import ETACalculator
from classes.midpoint_request import MidpointRequest
from classes.user import User

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
	'''Returns a suggested activity that's somewhere between the users' locations.'''
	# TODO
	pass
