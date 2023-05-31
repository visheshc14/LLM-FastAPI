# client.py
import grpc
import text_generator_pb2
import text_generator_pb2_grpc

def generate_text():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = text_generator_pb2_grpc.TextGeneratorStub(channel)
        request = text_generator_pb2.TextRequest(text="Hello, model!")
        response = stub.GenerateText(request)
        print(f"Generated text: {response.generated_text}")

if __name__ == "__main__":
    generate_text()
