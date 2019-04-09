#include<iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
 
 
using namespace cv;
 
 
int main()
{
	// 读入一张图片
	Mat img=imread("worker.jpg");
	// 创建一个名为 "worker"窗口
	namedWindow("worker");
	// 在窗口中显示游戏原画
	imshow("worker",img);
	// 等待60000 ms后窗口自动关闭
	waitKey(60000);
	return 0;
}

