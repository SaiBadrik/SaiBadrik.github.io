from flask import *
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('form.html')

@app.route('/submitform', methods=['POST'])
def checkDetails():
  name = request.form['name']
  age = request.form['age']
  gender = request.form['gender']
  details = {
    "name": name,
    "age": age,
    "gender": gender
  }
  return render_template('formOUT.html', details=details)

@app.route('/base')
def base():
  return render_template('base.html')

@app.route('/home')
def homePage():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(debug=True)