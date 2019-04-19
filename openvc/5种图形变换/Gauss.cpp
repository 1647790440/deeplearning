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
//使用opencv为图像添加高斯噪声
Mat GaussNoise(Mat &img);

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

        Mat img=imread("../worker.jpg");
        namedWindow("initial img");
        imshow("initial img",img);
        namedWindow("noised img");
        imshow("noised img",GaussNoise(img));
        waitKey(0);

    return a.exec();
}

Mat GaussNoise(Mat &img){
    Mat Gauss_img(img.size(),img.type());
    Mat noise(img.size(),img.type());
    RNG rng(time(NULL));
    rng.fill(noise,RNG::NORMAL,20,49);
    cv::add(img,noise,Gauss_img);

    return Gauss_img;
}
