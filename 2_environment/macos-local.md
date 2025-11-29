# Running the Project Locally on macOS

This guide explains how to set up and run this static website project on your local macOS machine.

## Prerequisites

*   **Python 3:** macOS usually comes with Python pre-installed. You can check your version by opening Terminal and typing `python3 --version`.
*   **Node.js (Optional, for `http-server` alternative):** If you prefer using a Node.js-based server, you'll need Node.js and npm installed. You can download it from [nodejs.org](https://nodejs.org/).
*   A modern web browser (e.g., Safari, Chrome, Firefox).

---

## Option 1: Using Python's Built-in Web Server (Recommended for simplicity)

This is the quickest way to get the site up and running as Python is typically available on macOS.

### 1. Open Terminal

1.  Open the **Terminal** application (you can find it in `Applications/Utilities` or by searching with Spotlight `⌘ + Space`).

### 2. Navigate to the Project Directory

1.  Use the `cd` command to navigate to the root directory of your project. For example, if your project is in `/Users/yourusername/projects/web`:

    ```bash
    cd /Users/yourusername/projects/web
    ```

### 3. Start the Web Server

1.  In the Terminal, run the following command to start a simple HTTP server on port 8000:

    ```bash
    python3 -m http.server 8000
    ```
    *   If port 8000 is already in use, you can choose another port (e.g., `python3 -m http.server 8080`).

### 4. Access the Website

1.  Open your web browser (Safari, Chrome, etc.).
2.  Navigate to `http://localhost:8000` (or the port you specified).

Your website should now be running locally. The `index.html` file in the root directory will automatically redirect to `pages/index.html`.

### 5. Stopping the Web Server

To stop the web server, go back to the Terminal where it's running and press `Ctrl + C`.

---

## Option 2: Using Node.js `http-server` (Alternative)

If you have Node.js and npm installed, `http-server` is another great option.

### 1. Install `http-server` (if not already installed)

1.  Open Terminal.
2.  Install `http-server` globally using npm:

    ```bash
    npm install -g http-server
    ```

### 2. Navigate to the Project Directory

1.  Use the `cd` command to navigate to the root directory of your project:

    ```bash
    cd /Users/yourusername/projects/web
    ```

### 3. Start the Web Server

1.  In the Terminal, run the following command:

    ```bash
    http-server
    ```

2.  The server will usually start on port 8080 or 8081 and provide URLs like `http://127.0.0.1:8080` and `http://192.168.x.x:8080`.

### 4. Access the Website

1.  Open your web browser.
2.  Navigate to one of the URLs provided by `http-server` (e.g., `http://localhost:8080`).

### 5. Stopping the Web Server

To stop the web server, go back to the Terminal where it's running and press `Ctrl + C`.
