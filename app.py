from flask import Flask, render_template, request
import pickle
classifier = pickle.load(open('spam_ham_model.pkl', 'rb'))
cv = pickle.load(open('countVect_model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    message = request.form['message']
    data = [message]
    vect = cv.transform(data).toarray()
    prediction = classifier.predict(vect)
    output=prediction[0]
    if output=='spam':
        output="Spam Text Detected" 
    elif output=='ham':
        output= "Not a Spam Text"
    # print(output) 
    return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == '__main__':
	app.run(debug=True)