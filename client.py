
import socket
import json

# Kabarak University - Distributed Systems Practical
# Project: Local Product Information Client
# Communicates with server.py through a TCP connection.


def get_product_from_server(product_id, host="127.0.0.1", port=65432):
    """Send a product ID to the server and display its response."""

    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:
        # Establish a TCP connection with the local server.
        client_socket.connect((host, port))

        # Send the requested product ID.
        client_socket.sendall(product_id.encode("utf-8"))

        # Receive the server response and decode its JSON data.
        response = client_socket.recv(1024).decode("utf-8")
        result = json.loads(response)

        print("\n--- Kabarak Product Lookup Result ---")

        if result["status"] == "success":
            product = result["data"]

            print(f"Product name : {product['name']}")
            print(f"Price        : ${product['price']}")
            print(f"Stock        : {product['stock']} units")

        else:
            print(f"Request failed: {result['message']}")

    except ConnectionRefusedError:
        print(
            "Connection failed. Start server.py before "
            "running the client."
        )

    except (json.JSONDecodeError, KeyError, OSError) as error:
        print(f"Communication error: {error}")

    finally:
        # Release the client socket after the request.
        client_socket.close()


if __name__ == "__main__":
    print("=" * 43)
    print("KABARAK UNIVERSITY")
    print("DISTRIBUTED SYSTEMS - CLIENT APPLICATION")
    print("=" * 43)

    while True:
        product_id = input(
            "\nEnter product ID (101, 102, 103) or 'exit': "
        ).strip()

        if product_id.lower() == "exit":
            print("Client application closed.")
            break

        if product_id:
            get_product_from_server(product_id)
