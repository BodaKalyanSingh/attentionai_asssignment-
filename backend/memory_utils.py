import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def save_memory_to_file(user_name, preferences):
    try:
        # Load existing data
        try:
            with open("user_memory.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        # Update data with new preferences
        data[user_name] = preferences

        # Save updated data
        with open("user_memory.json", "w") as file:
            json.dump(data, file, indent=4)
        logging.info("User preferences saved successfully.")
    except Exception as e:
        logging.error("Error saving user preferences: %s", str(e))
