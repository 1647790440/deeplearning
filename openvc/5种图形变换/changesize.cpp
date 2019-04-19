#include <QCoreApplication>
#include<iostream>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<opencv2/imgproc/types_c.h>

using namespace std;
using namespace cv;

//使用opencv实现图像大小变换

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

        Mat img=imread("../worker.jpg");
        namedWindow("initial img");
        imshow("initial img",img);
        Mat big_img;
        Mat small_img;
        resize(img,big_img,Size(),2,2);      //resize函数
        resize(img,small_img,Size(),0.5,0.5);
        namedWindow("big img");
        imshow("big img",big_img);
        namedWindow("small img");
        imshow("small img",small_img);
        waitKey(0);
    return a.exec();
}



