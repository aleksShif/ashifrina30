# Shy : Sasha S, Henry B, Yuki F
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go? - to the terminal
    return "No hablo queso!"

app.run()

