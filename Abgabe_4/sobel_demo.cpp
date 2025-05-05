#include<pybind11/pybind11.h>
#include<pybind11/numpy.h>
#include <pybind11/eigen.h>

namespace py = pybind11;


Eigen::MatrixXd sobel(Eigen::MatrixXd gray_img, Eigen::MatrixXd filter) {
    int rows = gray_img.rows();
    int cols = gray_img.cols();

    Eigen::MatrixXd filtered_img(rows - 2, cols - 2);

    // 1. Faltung anwenden
    for (int i = 1; i < rows - 1; ++i) {
        for (int j = 1; j < cols - 1; ++j) {
            double sum = 0.0;

            for (int fi = -1; fi <= 1; ++fi) {
                for (int fj = -1; fj <= 1; ++fj) {
                    sum += gray_img(i + fi, j + fj) * filter(fi + 1, fj + 1);
                }
            }

            filtered_img(i - 1, j - 1) = sum;
        }
    }

    // 2. Skalieren des Ergebnisses auf 0–255
    double min_val = filtered_img.minCoeff();
    double max_val = filtered_img.maxCoeff();
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