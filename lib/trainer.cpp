#include <iostream>
#include <fstream>
#include <string>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
  string line;
  ifstream input_file;
  Mat *inputMat;//(9, 10, CV_32FC1);
  input_file.open("../games/inputs");
  if(input_file.is_open())
    {
      while(getline(input_file, line))
        {
          cout << line << endl;
        }
    }
  input_file.close();

  return 0;
}
