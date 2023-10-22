from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/postData', methods=['POST'])
def postData():
    if request.method == 'POST':
        # Get data from the POST request
        email_addie = request.form.get('input-3')  # Replace 'key' with the actual key/name of the data in the form
       
        # Process the data (you can do whatever you want with the data here)
        with open('swapPartyUsers.json', 'r') as file:
            data = json.load(file)
            data[email_addie] = "some new data"
            with open('swapPartyUsers.json', 'w') as file:
                json.dump(data, file, ident=4)




        # Return a response
        print(email_addie)


        # read a json file in the same directory
        # append the new data in the json file
        # save the json file back
        return 'Data received successfully!', 200  # 200 OK status code indicates a successful request
    else:
        # Handle other HTTP methods (GET, PUT, DELETE, etc.)
        return 'Method not allowed', 405  # 405 Method Not Allowed status code indicates that the method is not allowed for the requested URL

if __name__ == "__main__":
    app.run(debug=True)
