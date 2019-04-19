#include <QCoreApplication>
#include<iostream>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<opencv2/imgproc/types_c.h>

using namespace std;
using namespace cv;

Mat Laplace(Mat &img);
//使用opencv锐化图像，用拉普拉斯算子实现
int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

        Mat img=imread("../worker.jpg");
        namedWindow("initial img");
        imshow("initial img",img);
        namedWindow("sharped img");
        imshow("sharped img",Laplace(img));
        waitKey(0);

    return a.exec();
}

Mat Laplace(Mat &img){
    Mat lap_img(img.size(),img.type());
    Mat kern = (Mat_<char>(3,3) << 0, 1 ,0,
                                   1, -4, 1,
                                   0, 1, 0);
    filter2D(img,lap_img,img.depth(),kern);
    return lap_img;
}


