import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main(args=None):
    rclpy.init('test_point')
    print("test is only test")
    rclpy.shutdown()

if __name__ == '__main__':
    main()