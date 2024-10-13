class DatabaseResultCache:
    def __init__(self, func):
        self.func = func
        self.cache_name = f"_{func.__name__}_cache"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if not hasattr(instance, self.cache_name):
            print(f"Fetching data from database for {self.func.__name__}...")
            # Perform the expensive database query and cache the result
            result = self.func(instance)
            setattr(instance, self.cache_name, result)
        return getattr(instance, self.cache_name)

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    # Simulate a database query with the descriptor caching
    @DatabaseResultCache
    def fetch_user_data(self):
        # Simulate a slow database call
        import time
        time.sleep(2)
        return {"id": self.user_id, "name": f"Person_{self.user_id}", "email": f"Person_{self.user_id}@gmail.com"}


user = User(1)
# First time fetching data will hit the database (simulated)
print(user.fetch_user_data)

# Second time, it fetches the cached result instantly
print(user.fetch_user_data)