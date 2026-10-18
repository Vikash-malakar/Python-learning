class ApplicationError(Exception):
    """Base exception for the application."""
    pass


class AuthenticationError(ApplicationError):
    pass


class AuthorizationError(ApplicationError):
    pass


class ValidationError(ApplicationError):
    pass


def authenticate(username, password):
    if not username or not password:
        raise ValidationError("Username and password are required.")

    if username != "admin" or password != "secret123":
        raise AuthenticationError("Invalid credentials.")

    return {"username": username, "role": "admin"}


def access_dashboard(user):
    if user["role"] != "admin":
        raise AuthorizationError("Access denied.")

    return "Welcome to Admin Dashboard!"


try:
    user = authenticate("admin", "secret123")
    print(access_dashboard(user))

except ValidationError as error:
    print("Validation:", error)

except AuthenticationError as error:
    print("Authentication:", error)

except AuthorizationError as error:
    print("Authorization:", error)