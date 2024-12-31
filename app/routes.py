from flask import request, jsonify
from . import services.event_service as event_service
from . import services.user_service as user_service

def init_routes(app):
    @app.route('/webhook', methods=['POST'])
    def webhook():
        data = request.get_json()
        user_id = data['user_id']
        message = data['message']
        return jsonify({'response': process_message(message, user_id)})

    def process_message(message, user_id):
        location = "New York"  # Extract from message using Rasa
        interests = ["music", "art"]  # Extract from message using Rasa
        user_service.update_preferences(user_id, interests)
        events = event_service.fetch_events(location, interests)
        return f"Here are some events based on your interests: {events}"
