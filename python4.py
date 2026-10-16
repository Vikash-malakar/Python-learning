import time

class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name

    def __enter__(self):
        print(f"Connecting to {self.database_name}...")
        self.connection = {"status": "connected"}
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection["status"] = "closed"
        print("Database connection closed.")

        if exc_type:
            print("Error:", exc_value)

        return False


with DatabaseConnection("StudentDB") as db:
    print("Connection:", db)
    print("Executing database operation...")
    time.sleep(1)