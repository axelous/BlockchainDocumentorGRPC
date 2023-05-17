import grpc
import text_pb2
import text_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = text_pb2_grpc.TextServiceStub(channel)
        response = stub.sendText1(text_pb2.TextRequest1(text="76ea00c4811a504a7a174473e0d0daca"))
    print(response.text)

if __name__ == '__main__':
    run()

