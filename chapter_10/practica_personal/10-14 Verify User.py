from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        usuario = json.loads(contents)
        return usuario
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    ciudad = input("where do you live? ")
    usuario = {}
    usuario['username'] = username
    usuario['ciudad'] = ciudad
    contents = json.dumps(usuario)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    usuario = get_stored_username(path)
    if usuario:
        username2 = input("What is your name? ")
        if usuario['username'] == username2:
            print(f"Welcome back, {usuario['username']} from {usuario['ciudad']}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user()
