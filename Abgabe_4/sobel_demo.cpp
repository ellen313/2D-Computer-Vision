#include<pybind11/pybind11.h>
#include<pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <Eigen/Core>

namespace py = pybind11;


Eigen::MatrixXd sobel(Eigen::MatrixXd gray_img, Eigen::MatrixXd filter) {
    int rows = gray_img.rows();
    int cols = gray_img.cols();

    Eigen::MatrixXd filtered_img(rows - 2, cols - 2);

    for (int u = 1; u < rows - 1; ++u) {
        for (int v = 1; v < cols - 1; ++v) {
            double sum = 0.0;

            for (int i = -1; i <= 1; ++i) {
                for (int j = -1; j <= 1; ++j) {
                    sum += gray_img(u + i, v + j) * filter(i + 1, j + 1);
                }
            }

            filtered_img(u - 1, v - 1) = sum;
        }
    }

    double min_val = filtered_img.minCoeff();  // kleinsten Wert in der Matrix
    double max_val = filtered_img.maxCoeff();  // größten Wert in der Matrix
    double range = max_val - min_val;

    if (range != 0) {
        filtered_img = (filtered_img.array() - min_val) / range * 255.0;
    } else {
        filtered_img.setZero();  // Bild hat keine Variation
    }

    return filtered_img;
}

PYBIND11_MODULE(sobel_demo, m) {
    m.doc() = "sobel operator using numpy!";
    m.def("sobel", &sobel);
}