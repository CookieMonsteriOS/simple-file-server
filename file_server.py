from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Set the directory you want to serve files from
UPLOAD_DIRECTORY = '/path/to/your/directory'

@app.route('/files/<path:path>')
def download_file(path):
    """Serve a file from the specified directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

if __name__ == '__main__':
    # Make sure the directory exists before running the server
    if not os.path.exists(UPLOAD_DIRECTORY):
        print(f"Error: The specified directory '{UPLOAD_DIRECTORY}' does not exist.")
        exit(1)

    app.run(debug=True)
