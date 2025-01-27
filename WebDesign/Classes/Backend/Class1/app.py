from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
@app.route('/contact/<name>')
def contacts(name="Guest"):
  return render_template('contacts.html', name=name)

@app.route('/name/<name>')
def name(name):
  return f"<h1>Hello, {name}!</h1>"

@app.route('/square/<int:num>')
def square(num):
  pattern = ""
  for i in range(num):
    pattern += "*"*i + "<br>"
  return f"Your number is {num}. Here is your pattern: : <br> {pattern}"

if __name__ == '__main__':
  # debug mode is enabled
  app.run(debug=True, port=1000)