
import socket
import json

# Kabarak University - Distributed Systems Practical
# Project: Local Product Information Server
# Address: 127.0.0.1 | Port: 65432


# ==========================================
# LAYER 1: DATA ACCESS LAYER (DAL)
# Stores and retrieves product information.
# ==========================================

PRODUCT_DATABASE = {
    "101": {"name": "Laptop", "price": 999.99, "stock": 5},
    "102": {"name": "Smartphone", "price": 499.99, "stock": 12},
    "103": {"name": "Headphones", "price": 79.99, "stock": 25}
}


def get_product_details(product_id):
    """Retrieve product details using the supplied ID."""
    return PRODUCT_DATABASE.get(product_id)


# ==========================================
# LAYER 2: BUSINESS LOGIC LAYER (BLL)
# Processes requests and determines the result.
# ==========================================

def handle_product_request(product_id):
    """Check whether the requested product exists."""
    product = get_product_details(product_id)

    if product is not None:
        return {
            "status": "success",
            "message": "Product found successfully.",
            "data": product
        }

    return {
        "status": "error",
        "message": f"Product ID {product_id} was not found."
    }


# ==========================================
# LAYER 3: PRESENTATION / NETWORK LAYER
# Handles TCP connections and JSON responses.
# ==========================================

def run_server(host="127.0.0.1", port=65432):
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server_socket.bind((host, port))
    server_socket.listen()

    print("=" * 48)
    print("KABARAK UNIVERSITY - DISTRIBUTED SYSTEMS")
    print("Product Information Server")
    print(f"Server address: {host}:{port}")
    print("Status: Waiting for client requests...")
    print("=" * 48)

    try:
        while True:
            connection, client_address = server_socket.accept()

            with connection:
                received_data = connection.recv(1024).decode("utf-8")

                if not received_data:
                    continue

                product_id = received_data.strip()

                print(f"\nClient connected: {client_address}")
                print(f"Request received for product ID: {product_id}")

                # Pass the request to the business logic layer.
                result = handle_product_request(product_id)

                # Convert the result into JSON before sending it.
                response = json.dumps(result).encode("utf-8")
                connection.sendall(response)

                print(f"Response status: {result['status']}")
                print("Response sent successfully.")
                print("-" * 48)

    except KeyboardInterrupt:
        print("\nServer stopped by the user.")

    finally:
        server_socket.close()
        print("Server socket closed.")


if __name__ == "__main__":
    run_server()
