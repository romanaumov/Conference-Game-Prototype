from flask import Flask, render_template_string
import csv
from flask import request

app = Flask(__name__)

# Set the get endpoint URL
@app.route('/', methods=['GET'])
def home():
    print('Get the Main page...')
    
    path = './web/index.html'
    
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

# Set the get endpoint URL
@app.route('/page2', methods=['GET'])
def page2():
    print('Get the Second page...')
    
    path = './web/2.html'
    
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

# Set the get endpoint URL
@app.route('/page3', methods=['GET'])
def page3():
    print('Get the Second page...')
    
    path = './web/3.html'
    
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

@app.route('/page4', methods=['POST'])
def page4():
    print('Get the Second page...')
    
    path = './web/4.html'
    PLAYERS_PATH = 'players.csv'
    
    # Process the form data here
    first_player = request.form['first_player']
    second_player = request.form['second_player']
        
    if request.form.get('privacy_policy') is not None:
        # The user has agreed to the game rules
        is_agreed = 1
    else:
        # The user has not agreed to the game rules
        is_agreed = 0
    
    # Save the names into a CSV file
    with open(PLAYERS_PATH, 'a', newline='') as csv_file:
        fieldnames = ['first_player', 'second_player']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if csv_file.tell() == 0:
            # Write the header row if the file is empty
            writer.writeheader()

        # Write the data row
        writer.writerow({'first_player': first_player, 'second_player': second_player})

    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

@app.route('/page5', methods=['POST'])
def page5():
    
    print('Get the Second page...')
    
    path = './web/5.html'
    
    topic = request.form['topic']  # Change 'topic' to the name of the select element
    # ...
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

# # Set the get endpoint URL
# @app.route('/page5', methods=['GET'])
# def page5():
#     print('Get the Second page...')
    
#     path = './web/5.html'
    
#     # Read the contents of the HTML file
#     with open(path, 'r') as html_file:
#         html_contents = html_file.read()
        
#     # Render an HTML template with the HTML contents
#     return render_template_string(html_contents)

# Set the get endpoint URL
@app.route('/page6', methods=['GET'])
def page6():
    print('Get the Second page...')
    
    path = './web/6.html'
    
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

# Set the get endpoint URL
@app.route('/page7', methods=['GET'])
def page7():
    print('Get the Second page...')
    
    path = './web/7.html'
    
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

# Set the get endpoint URL
@app.route('/page8', methods=['GET'])
def page8():
    print('Get the Second page...')
    
    path = './web/8.html'
    
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

# Set the get endpoint URL
@app.route('/page9', methods=['GET'])
def page9():
    print('Get the Second page...')
    
    path = './web/9.html'
    
    # Read the contents of the HTML file
    with open(path, 'r') as html_file:
        html_contents = html_file.read()
        
    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
