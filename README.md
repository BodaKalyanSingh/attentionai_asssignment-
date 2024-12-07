One-Day Tour Planning Assistant
🚀 Overview
The One-Day Tour Planning Assistant is a conversational AI-based application that helps users create a comprehensive one-day itinerary for exploring a city based on their preferences. The assistant dynamically adapts to user inputs, remembers preferences, and provides optimized travel plans.

🌟 Features
Personalized Itineraries: Creates city-specific plans based on user preferences like interests, budget, and time constraints.
Memory Integration: Remembers user preferences across sessions using graph-based memory storage.
Dynamic Updates: Adjusts itineraries seamlessly based on evolving user inputs.
Weather Recommendations: Provides weather forecasts and suggests activities accordingly.
Persona Support: Handles multiple user personas for personalized interactions.
Optimized Path Generation: Suggests travel routes and modes based on budget and convenience.
Visual Map (Optional): Displays a map with points of interest.
News Integration: Fetches activity updates in the area affecting the itinerary.
🛠️ Technology Stack
Backend:
FastAPI for microservices and API handling.
Neo4j for graph-based memory storage.
LLM (via Transformers/Ollama/vLLM) for conversational intelligence and itinerary generation.
Frontend:
Streamlit for an interactive chat-based user interface.
Additional Tools:
OpenWeather API for weather forecasts.
Google Maps API for map generation (optional).
📦 Project Structure
csharp
Copy code
├── backend/
│   ├── main.py         # FastAPI server
│   ├── agents/
│   │   ├── itinerary_agent.py
│   │   ├── weather_agent.py
│   │   ├── memory_agent.py
│   │   └── optimization_agent.py
│   └── utils/
│       ├── database.py
│       ├── weather_api.py
│       └── maps_api.py
├── frontend/
│   ├── app.py          # Streamlit application
│   ├── static/
│   │   ├── styles.css
│   │   └── assets/
│   └── templates/
│       └── index.html
├── data/
│   └── initial_graph_data.json  # Initial Neo4j graph data
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── LICENSE            # Licensing information
🛠️ Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/one-day-tour-planning-assistant.git
cd one-day-tour-planning-assistant
2. Install Dependencies
Create a virtual environment and install the required dependencies:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Setup Neo4j Database
Install Neo4j locally or use the cloud version.
Import the initial graph data from data/initial_graph_data.json.
Configure the database connection in backend/utils/database.py.
4. Run the Backend
Start the FastAPI server:

bash
Copy code
cd backend
uvicorn main:app --reload
5. Launch the Frontend
Run the Streamlit application:

bash
Copy code
cd frontend
streamlit run app.py

Chat Interface
Itinerary Suggestions
🤖 LLM Agents
Implemented Agents:
User Interaction Agent: Handles user queries and collects preferences.
Itinerary Generation Agent: Creates an initial travel plan.
Optimization Agent: Refines paths based on constraints.# attentionai_asssignment-
