from classes.activity import Activity
from classes.eta_calculator import ETACalculator
from classes.metro_graph import MetroGraph
from classes.midpoint_request import MidpointRequest
from classes.suggestion import (
	Suggestion,
	suggest_midpoint_activity,
)
from utilities.midpoint_utils import (
	load_activities,
	load_metro_graph,
	load_midpoint_requests,
)

def main(
	activities: list[Activity],
	midpoint_requests: list[MidpointRequest],
	metro_graph: MetroGraph,
):
	# Create ETA Calculator entrypoint.
	eta_calculator = ETACalculator(metro_graph)

	# Search over each user's search requests,
	# finding a suggestion for each one.
	print('Finding suggested activities...\n')
	for request in midpoint_requests:
		suggestion = suggest_midpoint_activity(
			eta_calculator,
			request,
			activities,
		)
		print_request_details(request, suggestion)

def print_request_details(
	request: MidpointRequest,
	suggestion: Suggestion | None,
):
	print(f'Results for request: {request}')
	if suggestion is None:
		# Print a warning that no suggestion was found for the request.
		print('No suggestion generated for this request.')
	else:
		# Print details about this request's suggested activity.
		suggestion.print_details()
	print()

if __name__ == '__main__':
	metro_graph = load_metro_graph()
	midpoint_requests = [
		*load_midpoint_requests().values(),
		*load_midpoint_requests(larger_groups=True).values(),
	]
	activities = [*load_activities().values()]

	main(activities, midpoint_requests,  metro_graph)
