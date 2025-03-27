from flask import Flask, render_template, request, redirect, url_for
# Create an instance of the Flask class.
app = Flask(__name__)

# Main route to enter the app number
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the number entered by the user
        number = request.form.get('app_number', type=int)
        if number is not None:
            # Redirect to the corresponding app
            return redirect(url_for('redirect_to_app', number=number))
    
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>App Selector</title>
    </head>
    <body>
        <h1>Select an App</h1>
        <form method="POST">
            <label for="app_number">Enter an app number:</label>
            <input type="number" id="app_number" name="app_number" required>
            <input type="submit" value="Go to App">
        </form>
    </body>
    </html>
    '''

# Route that accepts a number and redirects based on that number
@app.route('/redirect/<int:number>')
def redirect_to_app(number):
    # Depending on the number entered, redirect to different URLs
    if number == 1:
        return redirect('http://localhost:5001/')
    elif number == 2:
        return redirect('http://localhost:5002/')
    elif number == 3:
        return redirect('http://localhost:5003/')
    else:
        return f"App {number} not found!", 404

if __name__ == '__main__':
    # Run the app on localhost:4449
    app.run(host='localhost', port=4449, debug=True)