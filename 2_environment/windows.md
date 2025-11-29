# Running the Project on Windows

This guide explains how to set up and run this static website project on a Windows machine.

## Prerequisites

*   A code editor like [Visual Studio Code](https://code.visualstudio.com/).
*   A web browser.

---

## Option 1: Using the Live Server Extension in VS Code (Recommended)

This is the easiest method if you have VS Code installed.

### 1. Install the Live Server Extension

1.  Open Visual Studio Code.
2.  Go to the **Extensions** view by clicking the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
3.  Search for **"Live Server"** by Ritwick Dey.
4.  Click **"Install"**.

### 2. Open the Project in VS Code

1.  Open your project folder in VS Code.
2.  In the Explorer panel on the left, right-click on the `index.html` file (or any other HTML file).
3.  Select **"Open with Live Server"**.

This will automatically open a new browser tab with your website running, and it will auto-reload whenever you save a file.

---

## Option 2: Using Node.js and `http-server`

This method requires you to have [Node.js](https://nodejs.org/) installed.

### 1. Install Node.js

If you don't have Node.js installed, download and install it from the official website: [https://nodejs.org/](https://nodejs.org/)

### 2. Install `http-server`

1.  Open a new Command Prompt or PowerShell terminal.
2.  Install the `http-server` package globally by running the following command:

    ```bash
    npm install -g http-server
    ```

### 3. Run the Web Server

1.  In your terminal, navigate to the root directory of your project.
2.  Start the web server by running the following command:

    ```bash
    http-server
    ```

3.  The server will start, and it will show you one or more URLs where your website is accessible (usually `http://127.0.0.1:8080`).

4.  Open your web browser and go to one of these URLs to view your website.

### 4. Stopping the Web Server

To stop the web server, go back to the terminal where it's running and press `Ctrl + C`.
