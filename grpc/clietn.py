import grpc
import text_pb2
import text_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = text_pb2_grpc.TextServiceStub(channel)
        response = stub.sendText2(text_pb2.TextRequest2(text="0x568C10Fb7b2eF315A0B20d4D2Bd8C623296577eB"))
    print(response.text)

if __name__ == '__main__':
    run()