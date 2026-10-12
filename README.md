# Kabarak University — Layered Client-Server Application

A Python-based client-server application developed for Distributed Systems coursework at Kabarak University. The project demonstrates TCP socket communication over localhost, JSON-based request-response handling, and a layered architecture for retrieving product information.

## 🏛️ System Architecture

### Server-Side Layers

1. **Data Access Layer (DAL):** Maintains an in-memory product database using a Python dictionary and retrieves product details based on the supplied product ID.
2. **Business Logic Layer (BLL):** Processes product requests, checks whether the requested product exists, and generates appropriate success or error responses.
3. **Presentation / Network Layer:** Creates and manages the TCP server socket, listens for client connections, receives product IDs, and sends JSON-encoded responses.

### Client-Side Layer

1. **Presentation / Client Layer:** Provides a command-line interface, accepts product IDs from the user, establishes a TCP connection with the server, and displays the returned product information in a readable format.

## 🔄 Communication Process

The application follows a request-response communication model:

1. The client accepts a product ID from the user.
2. The client establishes a TCP connection with the server at `127.0.0.1:65432`.
3. The product ID is transmitted to the server as UTF-8 encoded text.
4. The server retrieves the product information through the data access layer.
5. The business logic layer generates a JSON response indicating success or failure.
6. The server sends the response to the client and closes the connection.
7. The client decodes the JSON response and displays the result.

## 🛠️ Technologies Used

- **Programming language:** Python
- **Networking:** TCP sockets
- **Data exchange:** JSON
- **Network address:** `127.0.0.1` (localhost)
- **Port:** `65432`
- **Data storage:** In-memory Python dictionary

## 📁 Project Structure

```text
kabarak-distributed-systems/
├── client.py
├── server.py
└── README.md
```

## 🚀 How to Run

### Prerequisites

- Python 3 installed on your computer.
- Both `client.py` and `server.py` saved in the same project directory.

### Step 1: Start the server

Open a terminal in the project directory and run:

```bash
python server.py
```

The server will start listening for client connections.

### Step 2: Start the client

Open a second terminal in the same directory and run:

```bash
python client.py
```

### Step 3: Test the application

Enter one of the available product IDs when prompted:

- `101` — Laptop
- `102` — Smartphone
- `103` — Headphones

Enter `999` to test how the application handles a product that does not exist. Enter `exit` to close the client.

## 🧪 Expected Results

- **Successful request:** The client displays the product name, price, and available stock.
- **Unsuccessful request:** The client displays an error message when the product ID is not found.
- **Server monitoring:** The server terminal displays incoming requests and response statuses.

## 🎯 Learning Objectives

This project demonstrates:

- Client-server communication using TCP sockets.
- Request-response interaction between separate program components.
- JSON serialization and deserialization.
- Separation of responsibilities through layered architecture.
- Basic error handling and resource management.
- Local network communication using Python.

## ⚠️ Project Scope

This is an educational demonstration. The product database is stored in memory and is not connected to a persistent database or Kabarak University's actual inventory system. The server processes client connections sequentially.

## 👨‍🎓 Academic Context

Developed as a practical exercise in Distributed Systems to demonstrate the design, implementation, and testing of a simple layered client-server application on a localhost environment.