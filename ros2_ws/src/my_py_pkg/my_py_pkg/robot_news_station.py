#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station") 
        
        self.robot_name_ = "C3PO"
        self.publisher_ = self.create_publisher(String, "robot_news", 10) # queue size 
        self.timer_ = self.create_timer(0.5, self.publish_news) # publish_news is a callback function
        self.get_logger().info("Robot News Station has been started")
        
        
    def publish_news(self):
        msg = String()
        msg.data = "Hello, this is " + str(self.robot_name_) + " from the robot news station."# ros2 interface show example_interfaces/msg/String
        self.publisher_.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
