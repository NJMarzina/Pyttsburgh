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
    euros = None
    yen = None
    pesos = None

    if request.method == 'POST':
        # Get the string entered by the user
        number = request.form.get('number', type=int)
        if number:
            # Convert
            euros = '${:,.2f}'.format(number*0.92)
            yen= '${:,.2f}'.format(number*150.0)
            pesos = '${:,.2f}'.format(number*20.0)

    return render_template('app3.html', 
                           euros=euros, 
                           yen=yen, 
                           pesos=pesos)

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
