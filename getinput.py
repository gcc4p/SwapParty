from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/Gulce")
def gulce():
    return render_template("gulce.html")

@app.route('/postData', methods=['POST'])
def postData():
    if request.method == 'POST':
        # Get data from the POST request
        input_text = request.form.get('input_text')  # Replace 'key' with the actual key/name of the data in the form
        height = request.form.get('height')  # Replace 'key' with the actual key/name of the data in the form

        # Process the data (you can do whatever you want with the data here)


        # Return a response
        print(input_text)
        print(height)

        # read a json file in the same directory
        # append the new data in the json file
        # save the json file back
        return 'Data received successfully!', 200  # 200 OK status code indicates a successful request
    else:
        # Handle other HTTP methods (GET, PUT, DELETE, etc.)
        return 'Method not allowed', 405  # 405 Method Not Allowed status code indicates that the method is not allowed for the requested URL

#after form is sent
person1_approved = False
person2_approved = False

@app.route('/approve') # somehow has to work for second person as well?
def approve_swap():
    global person1_approved
    person1_approved = True

if __name__ == "__main__":
    app.run(debug=True)
