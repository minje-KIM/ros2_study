#!/usr/bin/env python3
import rclpy
from rclpy.node import Node # To make a ROS2 node


def main(args=None):
    rclpy.init(args=args) # initialize ROS2 communication

    node = Node("py_test") # name of the Node
    node.get_logger().info("Hello ROS2")
    rclpy.spin(node) # allow Node to continue to be alive 

    rclpy.shutdown() # the last line for program


if __name__ == "__main__":
    main()