#include <QCoreApplication>
#include<iostream>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui/highgui_c.h>
#include<opencv2/imgproc/types_c.h>

using namespace std;
using namespace cv;

//ʹ��opencvʵ��ͼ��ת
int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

        Mat img=imread("../worker.jpg");
        namedWindow("initial img");
        imshow("initial img",img);
        Mat x_img;
        flip(img,x_img,0);    //x��
        namedWindow("x flip img");
        imshow("x flip img",x_img);
        Mat y_img;
        flip(img,y_img,1);    //y��
        namedWindow("y flip img");
        imshow("y flip img",y_img);
        Mat xy_img;
        flip(img,xy_img,-1);    //xyͬʱ��ת
        namedWindow("xy flip img");
        imshow("xy flip img",xy_img);
        waitKey(0);

    return a.exec();
}



