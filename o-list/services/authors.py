class Service:
    """Manage Author's operations"""

    def __init__(self, repository) -> None:
        """Class iniatilizer method"""
        self.repository = repository

    def get_all(self) -> list:
        """Get all operation"""
        return self.repository.get_all()

    def create(self):
        """Create operation"""
