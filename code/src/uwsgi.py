# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv

if not os.getenv("ENV", False):
    load_dotenv()

from src import create_app

application = create_app()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=int(os.environ["PORT"]))
