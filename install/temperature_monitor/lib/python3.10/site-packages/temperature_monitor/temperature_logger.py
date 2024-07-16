import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import os

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(Float64, 'temperature', self.listener_callback, 10)
        self.log_dir = os.path.join(os.path.expanduser('~'), 'Desktop/Session05/Johnny-Answers-Session05/src/temperature_monitor/logging')
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file_path = os.path.join(self.log_dir, 'temperature_log.txt')
        self.get_logger().info(f'Logging temperature data to {self.log_file_path}')
        
    def listener_callback(self, msg):
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(f'{self.get_clock().now().to_msg().sec}, {msg.data:.2f}\n')
        self.get_logger().info(f'Logged temperature: {msg.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
