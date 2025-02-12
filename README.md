# URL Shortener Application

This is a simple URL shortener application built using Python's Tkinter library for the graphical user interface (GUI) and the `pyshorteners` library for URL shortening services. The application allows users to input a URL, select a URL shortening service, and get a shortened URL.

## Features

- User-friendly GUI to input URLs
- Supports multiple URL shortening services (TinyURL and Is.gd)
- Displays the shortened URL and allows users to click and open it in a web browser
- Error handling for invalid inputs and service errors

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `tkinter` (usually included with Python installations)
  - `pyshorteners`
  - `webbrowser` (usually included with Python installations)

## Installation

1. Clone the repository or download the ZIP file and extract it.
2. Install the required Python libraries using pip:

   ```bash
   pip install pyshorteners
   ```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `url_shortener.py` file.
3. Run the application:

   ```bash
   python url_shortener.py
   ```

4. The GUI will open, allowing you to enter a URL and select a URL shortening service.
5. Click the "Shorten URL" button to get the shortened URL.
6. The shortened URL will be displayed, and you can click it to open it in your web browser.

## Code Overview

The application consists of the following key components:

1. **URL Entry**: A text entry widget for the user to input the URL to be shortened.
2. **Shortener Options**: Radio buttons for the user to select the URL shortening service (TinyURL or Is.gd).
3. **Shorten Button**: A button that triggers the URL shortening process.
4. **Result Label**: A label that displays the shortened URL and allows the user to click and open it in a web browser.

Here's a brief description of the main functions:

- `shorten_url()`: This function is triggered when the "Shorten URL" button is clicked. It retrieves the input URL, checks for validity, selects the appropriate shortening service, shortens the URL, and displays the result. It also handles errors and displays appropriate error messages.
