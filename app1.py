import os
from flask import Flask, render_template, request

# Get the directory of the current script
base_dir = os.path.abspath(os.path.dirname(__file__))

# We know this works because with base=8 it matches octal
def custom_baseConverter(number, base=8):
    # Validate base
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    
    # Handle 0 as a special case
    if number == 0:
        return '0'
    
    # Define digits to use
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Initialize the result
    result = ''
    
    # Absolute value to handle negative numbers
    is_negative = number < 0
    number = abs(number)
    
    # Convert to custom base
    while number > 0:
        # Get the remainder
        remainder = number % base
        # Add the corresponding digit
        result = digits[remainder] + result
        # Integer division to reduce the number
        number = number // base
    
    # Add negative sign if needed
    return ('-' + result) if is_negative else result

# Create the Flask application with explicit template folder
app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'))

# Route for the main page with number conversion form
@app.route('/', methods=['GET', 'POST'])
def index():
    # Create variables to store the results
    binary_result = None
    octal_result = None
    hexadecimal_result = None
    custom_base_result = None
    
    if request.method == 'POST':
        # Get the number entered by the user
        number = request.form.get('number', type=int)
        if number is not None:
            # Convert to binary
            binary_result = bin(number)[2:]
            # Convert to octal
            octal_result = oct(number)[2:]
            # Convert to hexadecimal
            hexadecimal_result = hex(number)[2:]
            # Convert to custom base
            custom_base_result = custom_baseConverter(number)
    
    return render_template('app1.html', 
                           binary_result=binary_result, 
                           octal_result=octal_result, 
                           hexadecimal_result=hexadecimal_result, 
                           custom_base_result=custom_base_result)

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)