from flask import Flask, render_template_string, request
import password_game as password_sol
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def password_game():
    message = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        # if password_sol.check_length(password):
        #     message = 'Success! Your password meets the requirement. (Frankie, wrote this function, lol)'
        if password_sol.check_length(password) == False and password_sol.check_length(password) != None:
            message = 'Error: Password must be atleast 8 characters long.'
        elif password_sol.check_digit(password) == False and password_sol.check_digit(password) != None:
            message = 'Error: Password must contain a digit'
        elif password_sol.check_uppercase(password) == False and password_sol.check_uppercase(password)!= None:
            message = 'Error: Does not contain an upperclase letter'
        elif password_sol.check_even_numbers(password) == False and password_sol.check_even_numbers(password) != None:
            message = "Error: Does not contain an even number"
        elif password_sol.check_sum(password) == False and password_sol.check_sum(password) != None:
            message = "Error: All the digits do not add up to 25"
        elif password_sol.check_day_of_week(password) == False and password_sol.check_day_of_week(password) != None:
            message = "Error: Does not contain day of week"
        else:
            message = "The password meets all the criteria!!"

    return render_template_string('''
    <!doctype html>
    <html>
    <head>
        <title>The Password Game</title>
        <style>
            body {
                background-color: #f0f2f5;
                font-family: Arial, sans-serif;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background-color: #fff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            h1 {
                margin-bottom: 20px;
            }
            ul {
                list-style-type: none;
                padding: 0;
                margin-bottom: 20px;
            }
            ul li {
                margin: 10px 0;
            }
            form input[type="password"] {
                padding: 10px;
                width: 80%;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            form input[type="submit"] {
                padding: 10px 20px;
                background-color: #007BFF;
                border: none;
                color: #fff;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            form input[type="submit"]:hover {
                background-color: #0056b3;
            }
            .message {
                margin-top: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>The Password Game</h1>
            <p>Enter a password that meets the following requirement:</p>
            <ul>
                <li>Password length must be exactly 8 characters.</li>
            </ul>
            <form method="post">
                <input type="password" name="password" required><br>
                <input type="submit" value="Submit">
            </form>
            {% if message %}
            <p class="message">{{ message }}</p>
            {% endif %}
        </div>
    </body>
    </html>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)
