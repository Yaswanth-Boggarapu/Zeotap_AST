import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath("/Users/yash/Zeotap/app/backend")))

from backend.api import app

if __name__ == "__main__":
    app.run(debug=True)
