from flask import Flask, session
app = Flask(__name__)
app.secret_key="im a secret"
DATABASE = "dojo_and_ninjas_schema"