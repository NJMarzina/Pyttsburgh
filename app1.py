import os
from flask import Flask, render_template, request

# Get the directory of the current script
base_dir = os.path.abspath(os.path.dirname(__file__))

# Create the Flask application with explicit template folder
app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'))

# Route for the main page with number conversion form
@app.route('/', methods=['GET', 'POST'])
def index():
    binary_result = None
    if request.method == 'POST':
        # Get the number entered by the user
        number = request.form.get('number', type=int)
        if number is not None:
            # Convert to binary
            binary_result = bin(number)[2:]
    
    return render_template('index.html', binary_result=binary_result)

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)