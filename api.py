from flask import Flask
app = Flask("THG_API")


@app.route("/")
def root():
    return 'api thg'


@app.route('/thg/packinfo/nadaconsta')
def nadaconsta():
    return 1
