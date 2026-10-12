from classes.activity import Activity
from classes.eta_calculator import ETACalculator
from classes.metro_graph import MetroGraph
from classes.suggestion import (
	Suggestion,
	suggest_midpoint_activity,
)
from classes.user_request import UserRequest
from utilities.midpoint_utils import (
	load_activities,
	load_metro_graph,
	load_user_requests,
)

def main(
	activities: list[Activity],
	user_requests: list[UserRequest],
	metro_graph: MetroGraph,
):
	# Create ETA Calculator entrypoint.
	eta_calculator = ETACalculator(metro_graph)

	# Search over each user's search requests,
	# finding a suggestion for each one.
	print('Finding suggested activities...\n')
	for request in user_requests:
		suggestion = suggest_midpoint_activity(
			request.user1_location,
			request.user2_location,
			activities,
			eta_calculator,
		)
		print_request_details(request, suggestion)

def print_request_details(
	request: UserRequest,
	suggestion: Suggestion | None,
):
	if suggestion is None:
		# Print a warning that no suggestion was found for the request.
		print(f'No suggestion generated for user: {request.user_id}')
	else:
		# Print details about this request's suggested activity.
		print(f'Suggested activity for user: {request.user_id}')
		suggestion.print_details()
	print()

if __name__ == '__main__':
	metro_graph = load_metro_graph()
	user_requests = load_user_requests()
	activities = load_activities()

	main(activities, user_requests,  metro_graph)
