from app import app
import os

HOST = '0.0.0.0'
PORT = 8000

# Do some production specific things to the app
if os.environ.get('DEBUG', False):
    app.config['DEBUG'] = True
else:
    app.config['DEBUG'] = False

if __name__ == "__main__":
    port = int(os.environ.get('PORT', PORT))
    app.run(host=HOST, port=port)
