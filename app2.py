import os
from flask import Flask, render_template, request

# Get the directory of the current script
base_dir = os.path.abspath(os.path.dirname(__file__))

# Create the Flask application with explicit template folder
app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'))

# Route for the main page with string processing form
@app.route('/', methods=['GET', 'POST'])
def index():
    # Create variables to store the results
    num_letters = None
    num_words = None
    num_sentences = None

    if request.method == 'POST':
        # Get the string entered by the user
        entry = request.form.get('string')
        if entry:
            # Process the string
            num_letters = len(entry)
            num_words = len(entry.split())
            num_sentences = entry.count('.') + entry.count('!') + entry.count('?')

    return render_template('app2.html', 
                           num_letters=num_letters, 
                           num_words=num_words, 
                           num_sentences=num_sentences)

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
