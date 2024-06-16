# Flask-Apps

To run the flask application using cmd in Windows-
in cmd, go to the directory which contains the code, in cmd type set FLASK_APP="filename", then type flask run.

To run using the name of the module-
set these in the code-
app=FLASK(__name__)
if __name__ == '__main__':
    app.run(debug=True)

and in the terminal- 
python filename.py
