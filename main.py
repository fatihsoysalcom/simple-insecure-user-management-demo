import hashlib
import os

# This example demonstrates a *naive* and *insecure* approach to user management
# to highlight the complexities and security risks that modern SaaS solutions mitigate.
# DO NOT use this code in production.

class User:
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password
        self.is_active = True # Simple flag, no email verification etc.

# Simulate a database
# In a real application, this would be a persistent database.
# Here, it's an in-memory dictionary for simplicity.
users_db = {} # Stores username -> User object

def hash_password_insecurely(password):
    """
    Simulates a basic, insecure password hashing.
    In a real system, you would use strong, salted, adaptive hashing algorithms
    like bcrypt, scrypt, or Argon2. This simple SHA256 without salt is
    demonstrating a common pitfall of DIY security.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(username, password):
    """
    Registers a new user with a basic, insecure password hashing.
    This function lacks many features a real system needs:
    - Password strength policies
    - Email verification
    - Uniqueness checks (beyond username)
    - Rate limiting for registrations
    - Protection against enumeration attacks
    """
    if username in users_db:
        print(f"Error: User '{username}' already exists.")
        return None

    # --- ARTICLE CONCEPT ILLUSTRATION START ---
    # This is where a DIY system starts to accumulate technical debt and security risks.
    # A SaaS solution would handle all these complexities securely and robustly,
    # including proper password hashing, strength policies, and uniqueness checks.
    hashed_password = hash_password_insecurely(password) # Insecure hashing for demonstration
    new_user = User(username, hashed_password)
    users_db[username] = new_user
    print(f"User '{username}' registered successfully (insecurely stored).")
    # --- ARTICLE CONCEPT ILLUSTRATION END ---
    return new_user

def login_user(username, password):
    """
    Attempts to log in a user.
    This function lacks:
    - Account lockout after multiple failed attempts
    - Two-factor authentication (2FA)
    - Session management
    - Robust error messages to prevent user enumeration
    """
    user = users_db.get(username)
    if not user:
        print(f"Login failed: User '{username}' not found.")
        return None

    # --- ARTICLE CONCEPT ILLUSTRATION START ---
    # Comparing a simple hash is insufficient for modern security standards.
    # A SaaS solution would provide robust authentication mechanisms, including
    # secure password verification, 2FA, and account lockout policies.
    if user.hashed_password == hash_password_insecurely(password): # Insecure comparison
        print(f"Login successful for '{username}'. Welcome!")
        return user
    else:
        print(f"Login failed: Incorrect password for '{username}'.")
    # --- ARTICLE CONCEPT ILLUSTRATION END ---
    return None

def main():
    print("--- Simple Insecure User Management Demo ---")
    print("This example shows a *basic* and *insecure* DIY user management system.")
    print("It highlights the complexities and security pitfalls that SaaS solutions address.")
    print("-------------------------------------------\n")

    # Demonstrate registration
    print("Attempting to register users:")
    register_user("alice", "password123")
    register_user("bob", "securepass")
    register_user("alice", "anotherpass") # Attempt to register existing user
    print("\n")

    # Demonstrate login
    print("Attempting to log in users:")
    login_user("alice", "password123") # Correct password
    login_user("bob", "wrongpass")    # Incorrect password
    login_user("charlie", "anypass")  # Non-existent user
    login_user("bob", "securepass")   # Correct password
    print("\n")

    print("--- End of Demo ---")
    print("Notice the lack of features like password reset, MFA, social login,")
    print("and the insecure storage/comparison of passwords. A real system")
    print("requires much more, which is why SaaS solutions are recommended.")

if __name__ == "__main__":
    main()
