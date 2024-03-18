# Simple File Server

This Python script creates a basic file server using the Flask framework, allowing you to serve files over HTTP.

## Usage

1. Clone the repository or save the `file_server.py` script to your local machine.

2. Install Flask if you haven't already:
    ```
    pip install flask
    ```

3. Open a terminal, navigate to the directory containing the `file_server.py` script, and run it:
    ```
    python file_server.py
    ```

4. The server should now be running. You can access files by navigating to `http://localhost:5000/files/<filename>` in your web browser, where `<filename>` is the name of the file you want to download.

## Configuration

- Modify the `UPLOAD_DIRECTORY` variable in the script to specify the directory containing the files you want to serve.

## Notes

- Ensure that the specified directory exists before running the server.
- This script provides a basic file server implementation. Depending on your requirements, you may want to add additional features such as authentication or file listing.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
