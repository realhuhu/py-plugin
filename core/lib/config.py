import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-grpc-host")
parse.add_argument("-grpc-port")
parse.add_argument("-redis-host")
parse.add_argument("-redis-port")
parse.add_argument("-redis-password")
config = parse.parse_args()
