from abc import ABC, abstractmethod

# Subject Interface
class Database(ABC):
    @abstractmethod
    def request_data(self):
        pass

# Real Subject
class RealDatabase(Database):
    def request_data(self):
        return "Data from the real database."

# Proxy Class
class RemoteDatabaseProxy(Database):
    def __init__(self, user_role):
        self._real_database = RealDatabase()
        self._user_role = user_role

    def request_data(self):
        # Access control: Only allow if the user role is 'admin'
        if self._user_role == 'admin':
            print("Proxy: Logging access to the real database.")
            return self._real_database.request_data()
        else:
            return "Access Denied: Insufficient permissions."

# Usage
if __name__ == "__main__":
    # Client with 'admin' role
    admin_client = RemoteDatabaseProxy(user_role="admin")
    print(admin_client.request_data())

    # Client with 'guest' role
    guest_client = RemoteDatabaseProxy(user_role="guest")
    print(guest_client.request_data())