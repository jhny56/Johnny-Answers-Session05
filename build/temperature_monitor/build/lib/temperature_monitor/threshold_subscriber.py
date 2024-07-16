import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String

class ThresholdSubscriber(Node):
    def __init__(self):
        super().__init__('threshold_subscriber')
        self.subscription = self.create_subscription(Float64, 'temperature', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'alert_trigger', 10)
        self.threshold = 25.0

    def listener_callback(self, msg):
        if msg.data > self.threshold:
            alert_msg = String()
            alert_msg.data = f'Temperature threshold exceeded: {msg.data:.2f}'
            self.publisher_.publish(alert_msg)
            self.get_logger().info(alert_msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ThresholdSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
