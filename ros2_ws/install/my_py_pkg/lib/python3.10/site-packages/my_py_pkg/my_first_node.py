#!/usr/bin/env python3
import rclpy
from rclpy.node import Node # To make a ROS2 node


class MyNode(Node):
    def __init__(self):
        super().__init__("py_test_OOP")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2 OOP")
        self.create_timer(0.5, self.timer_callback) 
        
    def timer_callback(self): # callback function
        self.counter_ += 1
        self.get_logger().info("Hello Timer" + str(self.counter_))

def main(args=None):
    rclpy.init(args=args) # initialize ROS2 communication

    node = MyNode()
    rclpy.spin(node) # allow Node to continue to be alive 

    rclpy.shutdown() # the last line for program


if __name__ == "__main__":
    main()