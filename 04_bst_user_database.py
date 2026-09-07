"""
04_bst_user_database.py
Implementation of an optimized O(log N) User Management System using Binary Search Trees (BST).
Course: Data Structures and Algorithms in Python (Jovian)
"""

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


class BSTNode:
    """Node structure for building the Binary Search Tree."""
    
    def __init__(self, key: str, value: Optional[User] = None) -> None:
        self.key = key
        self.value = value
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    def __repr__(self) -> str:
        return f"BSTNode(key='{self.key}')"


def insert(node: Optional[BSTNode], key: str, value: User) -> BSTNode:
    """Inserts a user into the BST maintaining O(log N) structural order."""
    if node is None:
        return BSTNode(key, value)
    
    if key < node.key:
        node.left = insert(node.left, key, value)
    elif key > node.key:
        node.right = insert(node.right, key, value)
    else:
        node.value = value  # Update value if key already exists
        
    return node


def find(node: Optional[BSTNode], key: str) -> Optional[BSTNode]:
    """Searches for a node by username key in O(log N) average time."""
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    return find(node.right, key)


def list_all(node: Optional[BSTNode]) -> List[User]:
    """Performs In-Order Traversal to return users in alphabetically sorted order."""
    if node is None:
        return []
    return list_all(node.left) + ([node.value] if node.value else []) + list_all(node.right)


def tree_height(node: Optional[BSTNode]) -> int:
    """Calculates the max depth/height of the tree."""
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


class BSTUserDatabase:
    """Optimized User Database backed by a Binary Search Tree."""
    
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None

    def insert(self, user: User) -> None:
        """Inserts or updates a user profile."""
        self.root = insert(self.root, user.username, user)

    def find(self, username: str) -> Optional[User]:
        """Finds a user profile by username."""
        node = find(self.root, username)
        return node.value if node else None

    def list_all(self) -> List[User]:
        """Returns all users sorted by username."""
        return list_all(self.root)

    def height(self) -> int:
        """Returns tree depth to measure balance efficiency."""
        return tree_height(self.root)


if __name__ == "__main__":
    db = BSTUserDatabase()
    
    # Test Data
    u1 = User("aaron", "Aaron Swartz", "aaron@example.com")
    u2 = User("birgitta", "Birgitta Jónsdóttir", "birgitta@example.com")
    u3 = User("clara", "Clara Oswald", "clara@example.com")
    
    # Insert Nodes
    db.insert(u2)
    db.insert(u1)
    db.insert(u3)
    
    # Sanity Checks
    print("Database Tree Height:", db.height())
    print("Sorted User List:", db.list_all())
    print("Lookup 'aaron':", db.find("aaron"))