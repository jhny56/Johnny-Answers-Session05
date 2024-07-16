import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertPublisher(Node):
    def __init__(self):
        super().__init__('alert_publisher')
        self.subscription = self.create_subscription(String, 'alert_trigger', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'alert', 10)

    def listener_callback(self, msg):
        alert_msg = String()
        alert_msg.data = f'ALERT: {msg.data}'
        self.publisher_.publish(alert_msg)
        self.get_logger().info(alert_msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = AlertPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
