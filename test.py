import requests
import threading
import time

def make_request(text):
    payload = {"text": text}
    response = requests.post("http://localhost:8000/generate_text", json=payload)
    print(f"Generated text: {response.json()['generated_text']}")

# Stress testing the server
def stress_test():
    start_time = time.time()
    num_requests = 100

    for i in range(num_requests):
        thread = threading.Thread(target=make_request, args=(f"Request {i+1}",))
        thread.start()

    elapsed_time = time.time() - start_time
    print(f"Stress test completed in {elapsed_time} seconds")

if __name__ == "__main__":
    # Single request
    make_request("Hello, model!")

    # Stress test
    stress_test()
