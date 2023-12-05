from flask import Flask, redirect, render_template, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'

#THIS WILL MOVE LOCATIONS LATER -- (controller file)
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def start():
    # print(session.get('visits'))
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 0
    print(session)
    return render_template('index.html')  # Return the string 'Hello World!' as a response
#*******************************
# @app.route('/count')
# def count():
#     print(session)
#     return render_template('index.html', session=session)  # Return the string 'Hello World!' as a response



@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
#This is always at the bottom!
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
#*******************************
