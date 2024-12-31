# Community Discovery Bot

A chatbot that helps users discover events, activities, and community gatherings based on their interests and location.

## Features

- Natural language query processing
- Personalized event recommendations
- Location-based discovery
- User preference learning
- Event API integration

## Prerequisites

- Python 3.8+
- Pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/arikaleeswaran/community-discovery-bot.git
cd community-discovery-bot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys:
   - Copy `config/config.py` and rename to `config/local_config.py`
   - Add your Eventbrite API key in `local_config.py`

## Running the Application

1. Initialize the database:
```bash
python -m app.database
```

2. Start the server:
```bash
python run.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### POST /webhook
Process user messages and return event recommendations.

Request body:
```json
{
    "user_id": "123",
    "message": "Find me art events in New York"
}
```

## Development

- Add new routes in `app/routes.py`
- Database models in `app/database.py`
- Services in `app/services/`

## Testing

Run tests with:
```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request
