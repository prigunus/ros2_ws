import sys
import rclpy
from rclpy.node import Node

#from std_msgs.msg import String
from example_interfaces.srv import AddTwoInts

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli_wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
    

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(int(sys.argv[1], int(sys.argv[2])))
    minimal_client.get_logger().info(
        f'Result of add two inst : {int(sys.argv[1])} + {int(sys.argv[2])}, {response.sum}'
    )
    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

