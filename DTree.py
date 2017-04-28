import Settings as st
from flask import Flask

app = Flask(__name__)


@app.route('/decision')
def hello_world():
    return 'Bienvenido estudiante'


if __name__ == '__main__':
    app.run(port = st.port)
