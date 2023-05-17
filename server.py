from concurrent import futures

import grpc
from web3 import Web3
from web3.middleware import geth_poa_middleware

import text_pb2
import text_pb2_grpc
from deploy import deploy





from web3 import Web3

# In the video, we forget to install_solc
# from solcx import compile_standard
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from django.views.decorators.csrf import csrf_exempt

import json

import web3
from web3 import Web3

# In the video, we forget to `install_solc`
# from solcx import compile_standard
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
class TextServiceServicer(text_pb2_grpc.TextServiceServicer):
    def sendText1(self, request, context):
        response = text_pb2.TextResponse1()
        text = deploy(request.text)
        response.text = text
        return response

    def sendText2(self, request, context):
        response = text_pb2.TextResponse2()
        var = request.text
        with open("SimpleStorage.sol", "r") as file:
            simple_storage_file = file.read()
        load_dotenv()

        # We add these two lines that we forgot from the video!
        print("Installing...")
        install_solc("0.6.0")

        # Solidity source code
        compiled_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
                "settings": {
                    "outputSelection": {
                        "*": {
                            "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                        }
                    }
                },
            },
            solc_version="0.6.0",
        )

        with open("compiled_code.json", "w") as file:
            json.dump(compiled_sol, file)

        # get bytecode
        bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
            "bytecode"
        ]["object"]

        # get abi
        abi = json.loads(
            compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
        )["output"]["abi"]

        # w3 = Web3(Web3.HTTPProvider(os.getenv("GOERLI_RPC_URL")))
        # chain_id = 4
        #
        # For connecting to ganache
        w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
        chain_id = 1337

        if chain_id == 4:
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            print(w3.clientVersion)
        # Added print statement to ensure connection suceeded as per
        # https://web3py.readthedocs.io/en/stable/middleware.html#geth-style-proof-of-authority

        my_address = "0xFA77658B30f71e338cCb80c3d6fa15457D5741e6"
        private_key = "0xe3fe155ac8bf2ab558eeb1ca787785f624c7d19badd17968e13c8192487b86c3"

        # Create the contract in Python
        SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
        simple_storage = w3.eth.contract(address=var, abi=abi)
        response.text = simple_storage.functions.retrieve().call()
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_pb2_grpc.add_TextServiceServicer_to_server(TextServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()