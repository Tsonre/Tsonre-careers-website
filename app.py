from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title':'Data Analyst',
    'location':'Lagos, Nigeria',
    'salary':'NGN. 1,000,000'
    },
  {
    'id':2,
    'title':'Backend Engineer',
    'location':'Ogun, Nigeria',
    'salary':'NGN. 500,000'
  
  },
{
    'id':3,
    'title':'Project manager',
    'location':'Ondo, Nigeria',
    'salary':'NGN. 2,000,000'
  
 },
{
    'id':4,
    'title':'Frontend Engineer',
    'location':'Lagos, Nigeria',
    'salary':'NGN. 250,000'
  
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
  
  