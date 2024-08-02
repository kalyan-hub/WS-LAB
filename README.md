# WS-LAB
EXPERIMENT 9 :

If you're interested in understanding and experimenting with the Same-Origin Policy (SOP) from scratch on Kali Linux, you can simulate and explore how it works using basic web servers and web applications. This involves setting up a simple server and experimenting with cross-origin requests.

Here’s a step-by-step guide to create a basic environment to test and understand SOP:

### Setting Up the Environment

1. *Install Necessary Tools*

   Ensure you have a web server and basic tools installed on Kali Linux. For this example, we'll use Python's built-in HTTP server.

   bash
   sudo apt-get update
   
   sudo apt-get install python3
   

3. *Create a Simple Web Server*

   We’ll create two basic HTML files to simulate cross-origin requests.

   *Create the first web server (e.g., server1):*

   bash
   
   mkdir server1
   
   cd server1
   

   Create an index.html file:


                   

   Start the HTTP server:

   bash
   
   python3 -m http.server 8000
   

   *Create the second web server (e.g., server2):*

   Open a new terminal, and create another directory:

   bash
   
   mkdir server2
   
   cd server2
   

   Create a data.html file:

   
   

   Start the HTTP server:

   bash
   
   python3 -m http.server 8001
   

5. *Testing Cross-Origin Requests*

   Open a web browser and navigate to http://localhost:8000. Click the button to fetch data from Server 2. 

   *Expected Behavior:*

   - If SOP is enforced, the browser will block the request from Server 1 to Server 2 due to CORS restrictions.
   - You will see an error in the browser's console.

   To observe the same-origin policy in action, try to fetch resources from different ports or domains.

### Configuring CORS Headers to Allow Cross-Origin Requests

To allow cross-origin requests, you need to modify the server responses to include CORS headers. Here’s how you can do it in Python with Flask for Server 2:

1. *Install Flask and Flask-CORS:*

   bash
   pip install flask flask-cors
   

2. *Create a CORS-Enabled Flask Server (Server 2):*

   Create a server2.py file:

  
  

   Start the Flask server:

   bash
   python3 server2.py
   

### Summary

By following these steps, you’ve set up a basic environment to explore the Same-Origin Policy and CORS:

- *Server 1* serves an HTML page that attempts to fetch data from another origin.
- *Server 2* serves the data and, with CORS configured, allows cross-origin requests.

This setup helps you understand how SOP works and how CORS can be configured to allow or restrict cross-origin interactions. If you have specific questions or need further assistance, feel free to ask!
