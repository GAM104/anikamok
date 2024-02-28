from flask import Flask

from helper import pets

app = Flask(__name__)


# Function to display the home page
@app.route('/')
def index():
  return '''
  <h1> Adopt a pet <h1/> 
  <p>Browse through the links below to 
   find your new furry friend:<p/> 
 <ul>
 <li><a href='/animals/dogs'>Dogs</a
 </li> 
 <li><a href='/animals/cats'>Cats </a> </li> 
 <li><a href='/animals/rabbits'>Rabbits</a></li> 
 </ul>
  '''


# Function to display a list of animals based on the pet type
@app.route('/animals/<pet_type>')
def animals(pet_type):  
  html = f'<h1> List of {pet_type} <h1/>'
  html += '<ul>'
  for pet in pets[pet_type]:
    html += f'<li> {pet["name"]}</li>'
  html += '</ul>'
  return html


# Function to display details of a specific pet
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet_list = pets[pet_type]
  pet = pet_list[pet_id]
  return f'''
  <h1>{pet["name"]}</h1>
  <img src={pet["url"]} />
  <p>{pet["description"]}</p>
  <ul>
    <li>{pet["breed"]}</li>
    <li>{pet["age"]}</li>
  </ul>
  '''

# Important: This line of code should always be placed at the bottom of the file.
# This is to ensure the correct startup of the server.
app.run(debug=True, host="0.0.0.0")