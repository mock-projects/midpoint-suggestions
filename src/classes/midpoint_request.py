from classes.user import User

class MidpointRequest:
	'''Represents a request received by the application to find a midpoint activity between two users.'''

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
		user1: User,
		user2: User,
		user1_location: tuple[float, float],
		user2_location: tuple[float, float],
	):
		# Core request data
		self.request_id = request_id
		self.category = category
		self.rating = rating
		self.price_tier = price_tier
		self.duration = duration
		# Entity relationships
		self.owner = owner
		self.user1 = user1
		self.user2 = user2
		self.user1_location = user1_location
		self.user2_location = user2_location

	def __repr__(self):
		return f'MidpointRequest<{self.request_id}>'
