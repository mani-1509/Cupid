from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from .love_aura import VisionAPI
from .lang_macher import LangMacher
from .game import GAMES
import random

routes = Blueprint('routes', __name__)
vision_api = VisionAPI()
lang_macher = LangMacher()

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/love_aura')
def love_aura():
    return render_template('love_aura.html')

@routes.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

# Love Aura routes

@routes.route('/process', methods=['POST'])
def process_image():
    try:
        image_url = None
        
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                image_url = vision_api.upload_to_cloudinary(file)
                
        elif 'image_url' in request.form:
            image_url = request.form.get('image_url')
            
        if not image_url:
            return jsonify({"error": "No valid image provided"}), 400

        analysis_result = vision_api.analyze_image(image_url)
        
        return jsonify({
            "response": analysis_result,
            "image_url": image_url
        })

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
    
# Game routes

@routes.route('/game')
def game():
    return render_template('game_index.html', games=GAMES)

@routes.route('/play/<game_id>')
def play_game(game_id):
    if game_id not in GAMES:
        return "Game not found!", 404
    return render_template('game.html', game=GAMES[game_id])

@routes.route('/api/score', methods=['POST'])
def update_score():
    data = request.json
    game_id = data.get('game_id')
    score = data.get('score')
    
    if game_id not in GAMES:
        return jsonify({'error': 'Invalid game'}), 400
        
    game = GAMES[game_id]
    victory = False
    message = ""
    
    if game_id == 'ice_breaker' and score >= game['blocks_needed']:
        victory = True
        message = random.choice(game['messages'])
    elif game_id == 'heart_catcher' and score >= game['hearts_needed']:
        victory = True
        message = random.choice(game['messages'])
        
    return jsonify({
        'victory': victory,
        'message': message
    })

# Love Language Matcher routes

@routes.route('/quiz')
def quiz():
    return render_template('quiz.html' , question=LangMacher.INITIAL_QUESTION)

@routes.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    conversation = request.json.get("conversation", [])
    
    # Add user's message to the conversation
    conversation.append({"role": "user", "content": user_input})
    
    # Get AI response
    ai_message, updated_conversation = lang_macher.chat(user_input, conversation)
    
    return jsonify({
        "response": ai_message,
        "conversation": updated_conversation
    })
