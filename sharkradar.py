from waitress import serve
from main import app

if __name__ == "__main__":
    print("Starting Shark-Radar Service Registry and Discovery Server on port 16461 for all IP Addresses")
    serve(app, listen="*:16461")
