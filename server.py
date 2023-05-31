# server.py
from concurrent import futures
import grpc
from minGPT.mingpt.model import GPT

import text_generator_pb2
import text_generator_pb2_grpc

class TextGeneratorServicer(text_generator_pb2_grpc.TextGeneratorServicer):
    def GenerateText(self, request, context):
        # Load the trained model
        model = GPT.load("model_weights")  # Provide the path to your trained model weights

        # Generate text based on the input
        generated_text = model.generate(request.text)

        return text_generator_pb2.TextResponse(generated_text=generated_text)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_generator_pb2_grpc.add_TextGeneratorServicer_to_server(TextGeneratorServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
