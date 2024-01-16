import grpc
import logging
from concurrent import futures
import signal

from src.grpc_services import restaurant_service_pb2
from src.grpc_services import restaurant_service_pb2_grpc

class RestaurantService(restaurant_service_pb2_grpc.RestaurantServiceServicer):
    def CreateRestaurant(self, request, context):
        # Implement your logic here
        return restaurant_service_pb2.RestaurantResponse(message="Restaurant Created")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_service_pb2_grpc.add_RestaurantServiceServicer_to_server(RestaurantService(), server)
    server.add_insecure_port("[::]:50051")

    def handle_sigterm(*_):
        logging.info("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        logging.info("Shut down gracefully")

    signal.signal(signal.SIGTERM, handle_sigterm)
    signal.signal(signal.SIGINT, handle_sigterm)

    server.start()
    logging.info("gRPC server started on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
