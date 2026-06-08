from dotenv import load_dotenv
from src.app import create_app
from handlers.product_handler import read_product
import os

load_dotenv()


PORT = os.getenv('PORT', '5000')
app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)