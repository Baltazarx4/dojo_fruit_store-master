from flask import Flask, render_template, request, redirect
app = Flask(__name__)  


@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    form_data = request.form
    return render_template("checkout.html", form_data=form_data)

@app.route('/fruits')         
def fruits():
    frutas =['apple.png','raspberry.png','strawberry','blackberry.png']
    return render_template("fruits.html", frutas=frutas)

if __name__=="__main__":   
    app.run(debug=True)    