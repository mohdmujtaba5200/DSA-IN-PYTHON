from typing import List, Optional


class User:
    """Represents an individual user profile in the system."""

    def __init__(self, username: str, name: str, email: str) -> None:
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(username='{self.username}', name='{self.name}', email='{self.email}')"

    def __str__(self) -> str:
        return self.__repr__()


class UserDatabase:
    """In-memory User Database using an unindexed array list storage."""

    def __init__(self) -> None:
        self.users: List[User] = []

    def insert(self, user: User) -> None:
        """Inserts a new user maintaining sorted username order."""
        for i, existing_user in enumerate(self.users):
            if existing_user.username == user.username:
                raise ValueError(f"User with username '{user.username}' already exists.")
            if existing_user.username > user.username:
                self.users.insert(i, user)
                return
        self.users.append(user)

    def find(self, username: str) -> Optional[User]:
        """Finds and returns a user by username via linear search."""
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update(self, username: str, name: Optional[str] = None, email: Optional[str] = None) -> bool:
        """Updates user details for a given username."""
        user = self.find(username)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            return True
        return False

    def list_all(self) -> List[User]:
        """Returns all users currently in the database."""
        return self.users


# Simple manual test runs
if __name__ == "__main__":
    db = UserDatabase()
    
    # Create sample users
    aakash = User("aakash", "Aakash Rai", "aakash@example.com")
    biraj = User("biraj", "Biraj Das", "biraj@example.com")
    hemanth = User("hemanth", "Hemanth Jain", "hemanth@example.com")

    # Test insertions
    db.insert(aakash)
    db.insert(hemanth)
    db.insert(biraj)  # Inserts in sorted position automatically

    print("All users in DB:", db.list_all())
    print("Find 'biraj':", db.find("biraj"))
    
    # Test update
    db.update("aakash", name="Aakash R. Updated")
    print("Updated 'aakash':", db.find("aakash"))