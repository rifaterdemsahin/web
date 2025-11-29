# Running the Project in a GitHub Codespace on macOS

This guide explains how to set up and run this static website project within a GitHub Codespace on a macOS machine.

## Prerequisites

*   A GitHub account.
*   Access to GitHub Codespaces.
*   A web browser.

## Steps

### 1. Open the Project in a Codespace

1.  Navigate to the project's repository on GitHub.
2.  Click the **"Code"** button.
3.  Select the **"Codespaces"** tab.
4.  Click **"Create codespace on main"** to create and launch a new Codespace.

### 2. Set Up and Run the Web Server

This project is a static website, so you'll need a simple web server to view it. We'll use Python's built-in `http.server`, which is available in the default Codespace environment.

1.  **Open a Terminal:** Once your Codespace is running, open a new terminal by going to the menu and selecting **Terminal > New Terminal**.

2.  **Start the Web Server:** In the terminal, run the following command to start a web server on port 8080:

    ```bash
    python3 -m http.server 8080
    ```

3.  **Access the Website:**
    *   When you start the server, GitHub Codespaces will automatically detect that you've started a web server and will show a pop-up notification.
    *   Click the **"Open in Browser"** button in the notification to open a new tab with your website running.
    *   If you don't see the pop-up, you can go to the **"Ports"** tab in the terminal pane, and you will see the running port (8080). Click the **"Open in Browser"** icon (a globe) next to the port number.

### 3. Viewing Your Website

Your website will be available at a URL similar to this:

```
https://<your-codespace-name>-8080.app.github.dev/
```

You can now navigate through the different pages of the website. The `index.html` file in the root directory will automatically redirect to `pages/index.html`.

### 4. Stopping the Web Server

To stop the web server, go back to the terminal where it's running and press `Ctrl + C`.
