from classes.user import User

class MidpointRequest:
	'''
	Represents a request received by the application
	to find a midpoint activity between users.
	'''

	def __init__(
		self,
		# Core request data
		request_id: str,
		category: str,
		rating: float,
		price_tier: float,
		duration: float,
		# Entity relationships
		owner: User,
		user_locations: dict[User, tuple[float, float]]
	):
		# Core request data
		self.request_id = request_id
		self.category = category
		self.rating = rating
		self.price_tier = price_tier
		self.duration = duration
		# Entity relationships
		self.owner = owner
		self.user_locations = user_locations

	def __repr__(self):
		return f'MidpointRequest<{self.request_id}>'

	@property
	def users(self):
		return [*self.user_locations.keys()]
