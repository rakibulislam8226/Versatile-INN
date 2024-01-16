import grpc
import logging
import signal
from concurrent import futures

from . import restaurant_service_pb2
from . import restaurant_service_pb2_grpc


class RestaurantService(restaurant_service_pb2_grpc.RestaurantServiceServicer):
    def CreateRestaurant(self, request, context):
        # Here, add your business logic to create a restaurant
        try:
            # If successful:
            return restaurant_service_pb2.RestaurantResponse(
                message="Restaurant Created"
            )
        except Exception as e:
            logging.error(f"Failed to create restaurant: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Failed to create restaurant")
            return restaurant_service_pb2.RestaurantResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_service_pb2_grpc.add_RestaurantServiceServicer_to_server(
        RestaurantService(), server
    )
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
