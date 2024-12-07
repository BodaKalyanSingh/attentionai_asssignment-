

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from llm_utils import get_llm_response
from weather_utils import get_weather
from memory_utils import save_memory_to_file  # Import from your custom memory utility

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

class UserPreferences(BaseModel):
    user_name: str
    city: str
    start_time: str
    end_time: str
    budget: float
    interests: list

@app.post("/generate_itinerary")
async def generate_itinerary(preferences: UserPreferences):
    try:
        # Validate interests
        if not preferences.interests:
            raise HTTPException(status_code=400, detail="Interests cannot be empty")
        
        # Save user preferences to file
        save_memory_to_file(preferences.user_name, {
            "city": preferences.city,
            "interests": preferences.interests,
            "budget": preferences.budget
        })
        
        # Generate a response using the LLM
        llm_response = get_llm_response(
            f"Plan a one-day itinerary in {preferences.city} considering the interests: {preferences.interests}"
        )
        if not llm_response:
            raise HTTPException(status_code=500, detail="Failed to generate itinerary")
        
        # Get weather information for the city
        weather_info = get_weather(preferences.city)
        if not weather_info:
            weather_info = "Weather information unavailable"
        
        return {
            "itinerary": llm_response,
            "weather": weather_info
        }
    except ValueError as ve:
        logging.error("Value error: %s", str(ve))
        raise HTTPException(status_code=400, detail="Invalid input")
    except Exception as e:
        logging.exception("Unexpected error")
        raise HTTPException(status_code=500, detail="Internal server error occurred")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
