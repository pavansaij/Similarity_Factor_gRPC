import sys
import os
import similarity_pb2
import similarity_pb2_grpc
import grpc
from google.protobuf import empty_pb2
from img_to_vec import Img2Vec
from PIL import Image

def run(path1,path2):
    channel = grpc.insecure_channel('localhost:50051')
    stub = similarity_pb2_grpc.SampleServerStub(channel)
    img2vec = Img2Vec()
    Image_In = similarity_pb2.Image(rgb1=img2vec.get_vec(Image.open(path1)),rgb2=img2vec.get_vec(Image.open(path2)))
    response = stub.Similarity(Image_In)
    print(response.score)
    
if __name__ == '__main__':
    path1 = input("Input first image path:")
    path2 = input("Input second image path:")
    run(path1,path2)