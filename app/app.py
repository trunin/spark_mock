import os

from flask import Flask

app = Flask(__name__)

SPARK_MASTER_HOST = os.environ.get("SPARK_MASTER_HOST")


@app.route('/')
def home():
    print(SPARK_MASTER_HOST)
    return str(SPARK_MASTER_HOST)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')