'''from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Page for entering food name and setting a timer
@app.route('/set_timer', methods=['GET', 'POST'])
def set_timer():
    if request.method == 'POST':
        food_name = request.form['food_name']
        cooking_time = int(request.form['cooking_time'])  # in minutes
        return redirect(url_for('timer', food_name=food_name, cooking_time=cooking_time))
    return render_template('timer_input.html')

# Timer page with an analog timer (JavaScript will handle countdown)
@app.route('/timer')
def timer():
    food_name = request.args.get('food_name')
    cooking_time = int(request.args.get('cooking_time'))
    
    # Render the timer page with the food name and cooking time
    return render_template('timer.html', food_name=food_name, cooking_time=cooking_time)

if __name__ == '__main__':
    app.run(debug=True)'''
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import os
import groq

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Load API key securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing Groq API Key. Set the GROQ_API_KEY environment variable.")

client = groq.Client(api_key=GROQ_API_KEY)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Page for entering food name and setting a timer
@app.route('/set_timer', methods=['GET', 'POST'])
def set_timer():
    if request.method == 'POST':
        food_name = request.form.get('food_name', 'Unknown Dish')
        cooking_time = request.form.get('cooking_time', '0')
        try:
            cooking_time = int(cooking_time)
        except ValueError:
            return jsonify({"error": "Invalid cooking time"}), 400

        return redirect(url_for('timer', food_name=food_name, cooking_time=cooking_time))
    return render_template('timer_input.html')

# Timer page with an analog timer (JavaScript will handle countdown)
@app.route('/timer')
def timer():
    food_name = request.args.get("food_name", "Unknown Dish")
    cooking_time = request.args.get("cooking_time", "0")
    
    try:
        cooking_time = int(cooking_time)
    except ValueError:
        cooking_time = 0

    return render_template('timer.html', food_name=food_name, cooking_time=cooking_time)

# AI-powered Recipe Fetching (Integrated from groq_test.py)
@app.route("/get_recipe", methods=["POST"])
def get_recipe():
    """Fetches a recipe from Groq AI based on the food name."""
    data = request.json
    dish = data.get("dish")

    if not dish:
        return jsonify({"error": "Dish name is required"}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": f"Give me the recipe for {dish}"},
            ],
            model="llama-3.3-70b-versatile",
        )

        recipe = chat_completion.choices[0].message.content
        return jsonify({"recipe": recipe})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
