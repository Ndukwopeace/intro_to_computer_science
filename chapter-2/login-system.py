DEFAULT_USERNAME = "peace"
DEFAULT_PASSWORD = "myPassword"


# Welcome text
welcome_text = r""".____                 .__           ________ ____ ___.___ 
|    |    ____   ____ |__| ____    /  _____/|    |   \   |
|    |   /  _ \ / ___\|  |/    \  /   \  ___|    |   /   |
|    |__(  <_> ) /_/  >  |   |  \ \    \_\  \    |  /|   |
|_______ \____/\___  /|__|___|  /  \______  /______/ |___|
        \/    /_____/         \/          \/              """

# Print the welcome text
print(welcome_text)

# User inputs
user_username = input("Input your username: ")
user_password = input("Input your password: ")


# Conditional statements
if user_username == DEFAULT_USERNAME and user_password == DEFAULT_PASSWORD:
    print(f"Welcome {user_username}")
else:
    print("invalid credentials")