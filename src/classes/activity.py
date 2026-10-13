class Activity:
	'''Represents a possible activity that might be suggested to users.'''

	def __init__(
		self,
		activity_id: str,
		name: str,
		category: str,
		coordinates: tuple[float, float],
		rating: float,
		price_tier: float,
		duration: float,
	):
		self.activity_id = activity_id
		self.name = name
		self.category = category
		self.coordinates = coordinates
		self.rating = rating
		self.price_tier = price_tier
		self.duration = duration

	def __repr__(self):
		return f'Activity<{self.name}>'
