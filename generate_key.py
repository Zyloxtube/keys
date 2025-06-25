import json
import random
import string
from datetime import datetime

def generate_key(length=16):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def save_key_to_json(key, filename='key.json'):
    data = {"key": key, "date": str(datetime.now().date())}
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    new_key = generate_key()
    print(f"Generated Key for {datetime.now().date()}: {new_key}")
    save_key_to_json(new_key)
