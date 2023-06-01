#include "rclcpp/rclcpp.hpp"

class MyNode: public rclcpp::Node
{
    public:
    MyNode(): Node("cpp_test"), counter_(0) // constructor -> node name, initialize counter to zero
    {
        RCLCPP_INFO(this->get_logger(), "Hello CPP Node Timer! ");
        timer_ = this->create_wall_timer(std::chrono::seconds(1), //duration
                            std::bind(&MyNode::timerCallback, this)); //callback function

    }

    private:
    void timerCallback()
    {
        counter_++;
        RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);


    }

    rclcpp::TimerBase::SharedPtr timer_;
    int counter_;
    
};




int main (int argc, char **argv)
{
    rclcpp::init(argc, argv); //initialize
    auto node = std::make_shared<MyNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    
    return 0;


}

