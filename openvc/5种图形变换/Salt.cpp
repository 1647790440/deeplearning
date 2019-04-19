#include <QCoreApplication>
#include<iostream>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<opencv2/imgproc/types_c.h>
#include<time.h>

using namespace std;
using namespace cv;

Mat SaltNoise(Mat &img);
//使用opencv为图像添加椒盐噪声，随机函数实现
int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

        Mat img=imread("../worker.jpg");
        namedWindow("initial img");
        imshow("initial img",img);
        namedWindow("noised img");
        imshow("noised img",SaltNoise(img));
        waitKey(0);

    return a.exec();
}

Mat SaltNoise(Mat &img){
    int n = 5000; //noise numbers
    Mat Salt_img = img.clone();
    for(int k = 0;k < n;k++){
        int i = rand() % Salt_img.rows;
        int j = rand() % Salt_img.cols;
        if(Salt_img.channels() == 1){
            Salt_img.at<uchar>(i,j) = 255;  //white
        }else{
            Salt_img.at<Vec3b>(i,j)[0] = 255;
            Salt_img.at<Vec3b>(i,j)[1] = 255;
            Salt_img.at<Vec3b>(i,j)[2] = 255;
        }
    }
    for(int k = 0;k < n;k++){
        int i = rand() % Salt_img.rows;
        int j = rand() % Salt_img.cols;
        if(Salt_img.channels() == 1){
            Salt_img.at<uchar>(i,j) = 0;  //black
        }else{
            Salt_img.at<Vec3b>(i,j)[0] = 0;
            Salt_img.at<Vec3b>(i,j)[1] = 0;
            Salt_img.at<Vec3b>(i,j)[2] = 0;
        }
    }
    return Salt_img;
}
