class User:
	'''Represents one person's account in the system.'''

	def __init__(
		self,
		user_id: str,
		locations: dict[str, tuple[float, float]] | None = None,
	):
		self.user_id = user_id
		self.locations = locations or {}

	def __repr__(self):
		return f'User<{self.user_id}>'
