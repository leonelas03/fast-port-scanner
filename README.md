# Fast Multithreaded Port Scanner 🌐

A blazing fast, lightweight TCP port scanner written in Python. This reconnaissance tool leverages multithreading to rapidly scan a target IP address for open ports, identifying potential entry points or exposed services.

## 🚀 Features
* **Multithreading:** Uses `concurrent.futures` to scan multiple ports simultaneously, reducing scan time from minutes to milliseconds.
* **Socket Programming:** Built using low-level Python sockets for raw network communication and TCP handshakes.
* **Customizable:** Easily adjustable thread counts and port ranges (defaults to the 1024 well-known ports).

## 🛠️ How it Works
The script attempts to establish a TCP connection with the target IP on a specified range of ports. Instead of iterating sequentially, it deploys a pool of worker threads to test dozens of ports concurrently. If the socket connects successfully (returns 0), the port is flagged as open.

## 💻 How to Run

1. Clone this repository or download `scanner.py`.
2. Ensure you have Python 3 installed on your system.
3. Run the script in your terminal:

   **For Linux / macOS:**
   ```bash
   python3 scanner.py
  **For windows:**
   ```bash
  'python scanner.py' or 'py scanner.py' depending on your installation
  ```

## 🎓 About
Project developed to demonstrate understanding of computer networks, TCP/IP protocols, socket programming, and concurrency in Python.

## 👥 Authors
Guilherme Escórci - [escorcio05](https://github.com/escorcio05)<br>
Leonardo Silva - [leonelas03](https://github.com/leonelas03)
 
   
