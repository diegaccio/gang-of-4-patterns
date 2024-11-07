
# Proxy Pattern

The **Proxy Pattern** is a structural design pattern that provides a surrogate or placeholder for another object to control access to it. It can be used for various purposes, such as lazy initialization, access control, logging, or remote access. The proxy class implements the same interface as the real subject and forwards requests to it.

Here’s an example of the Proxy Pattern in Python. In this example, we create a `RemoteDatabaseProxy` class to simulate access control and logging for a database.

### Example of the Proxy Pattern in Python

```python
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
```

### Explanation

1. **Database (Subject Interface)**: Defines the interface that both the `RealDatabase` and the `RemoteDatabaseProxy` will implement.
  
2. **RealDatabase (Real Subject)**: Implements the actual logic for requesting data.
  
3. **RemoteDatabaseProxy (Proxy)**: Controls access to the `RealDatabase`. It checks the user’s role, logging access and returning data only if the user has sufficient permissions.

4. **Client Usage**: When a client with the role `'admin'` requests data, the proxy allows access and logs the event. For a client with the role `'guest'`, access is denied.

### Output

Running this code produces:

```
Proxy: Logging access to the real database.
Data from the real database.
Access Denied: Insufficient permissions.
```

### Benefits of the Proxy Pattern

- **Access Control**: Can enforce permissions to control access.
- **Lazy Initialization**: Can delay object creation until it’s needed, saving resources.
- **Logging and Caching**: Adds additional functionality like logging or caching without modifying the real subject.

### Try it yourself

Here’s the working implementation of the Proxy Pattern in [Python](src/proxy.py)
