from flask import Flask

app = Flask (__name__)

@app.route('/')
def index ():
  return '''
  <h1> Adopt a pet <h1/> 
  <p>Browse through the links below to find your new furry     
  friend <p/> 
  <ul> 
  <li> dog <li/>
  <li> cat <li/>
  <li> rabbits <li/>
  <ul/>

  
  '''

@app.route('animals')
def animals (pet_type):
  html = '<h1> list of animals <h1/>'
  return html



  
  



# Viktigt: Denna kodrad ska alltid placeras längst ner i filen.
# Detta för att säkerställa en korrekt uppstart av servern.
app.run(debug=True, host="0.0.0.0")

