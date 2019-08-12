from waitress import serve
from main import app

if __name__ == "__main__":
    print("")
    print("Starting Shark-Radar\nService Registry and Discovery Server\non port 16461 for all IP Addresses")
    print("")
    serve(app, listen="*:16461")
