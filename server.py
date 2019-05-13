import sys
import os
import similarity_pb2 as sample_pb2
import similarity_pb2_grpc as sample_pb2_grpc
from concurrent import futures
from google.protobuf import empty_pb2
import time
import grpc
from similarity import Similarity as score

class SampleServer(sample_pb2_grpc.SampleServerServicer):
    def __init__(self):
        pass
    
    def Similarity(self,request,context):
        sc = score()
        img1,img2 = request.rgb1,request.rgb2
        response = sample_pb2.Similarity_Factor()
        response.score = sc.cosine_similarity(img1,img2)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_SampleServerServicer_to_server(
        SampleServer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("server is running")
    try:
        while True:
            time.sleep(100000)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()