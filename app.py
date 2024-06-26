"""
Application that predicts Carbon emission from vehicles based on the engine size, 
number of cylinders and fuel consumption.
"""
% pip install Flask
import numpy as np
from flask import Flask, request, render_template
import pickle

#Create an app object using the Flask class.
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open(r'C:\Users\berna\ml_fuel_project\models\CO_model.pkl','rb'))

#Define the route to be home
#The decorator below links the relative route of the URL to the function it is decorated
#Here, home function is with '/', our root directory.
#Running the app sends us to index.html
#Note that render_template means it looks for the file in the ttemplates folder

#Use the route() decorator to tell Flask what URL should trigger our function
@app.route('/')
def home():
    return render_template('index.html')
    
#You can use the methods argument of the route() decorator to handle different HTTP
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server
#Add Post method to the decorator to allow for form submission
#Redirect to /predict page with the output
@app.route('/predict', methods=['POST'])
def predict():
    
    int_features = [float(x) for x in request.form.values()] #Convert string inputs into floats
    features = [np.array(int_features)] #Convert to the form [[a,b,c]] for input to predict
    prediction = model.predict(features) #Features must be in the form [[a,b,c]]
    
    output = round(prediction[0],0)
    
    return render_template('index.html', prediction_text='CO2 Emissions is {}'.format(output))

#when the python interpreter reads a source file, it first defines a few special variables
#for now, we care about the __name__ variable
#If we execute our code in the main program, like in our case here, it assigns
#__main__ as the name (__name__)   
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here. 

if __name__ == "__main__":
    app.run()
