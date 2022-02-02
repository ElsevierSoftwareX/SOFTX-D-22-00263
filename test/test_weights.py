import unittest
import numpy as np

from pymcdm import weights


class TestEqualWeights(unittest.TestCase):
    """ Test output method without reference (no needed) """

    def test_output(self):
        matrix = np.array([[1, 2, 3, 5],
                           [2, 3, 4, 8]])

        output = [0.25, 0.25, 0.25, 0.25]
        output_method = list(weights.equal_weights(matrix))

        self.assertListEqual(output, output_method)


class TestEntropyWeights(unittest.TestCase):
    """ Test output method with reference:
    [1] Elsayed, Elsayed A., A. Shaik Dawood, and R. Karthikeyan. "Evaluating alternatives through the application of
    TOPSIS method with entropy weight." Int. J. Eng. Trends Technol 46.2 (2017): 60-66.
    """

    def test_output(self):
        matrix = np.array([[7, 312, 1891, 6613, 163],
                           [72, 88, 728, 941804, 1078],
                           [10, 252, 2594, 3466, 117471],
                           [10, 145, 980, 2371, 86329],
                           [65, 54, 350, 501, 29897],
                           [29, 48, 380, 912, 34051],
                           [7, 476, 3300, 78470, 2212],
                           [70, 87, 650, 733, 819000],
                           [4, 86, 591, 3015, 103],
                           [12, 79, 579, 3240, 96098],
                           [21, 45, 261, 1253, 453],
                           [1, 72, 530, 4333, 0.104800]])

        output = [0.104991, 0.069124, 0.071373, 0.449937, 0.304575]
        output_method = [round(weight, 6) for weight in weights.entropy_weights(matrix)]

        self.assertListEqual(output, output_method)


class TestSTDWeights(unittest.TestCase):
    """ Test output method with reference:
    [1] Jahan, A., & Edwards, K. L. (2013). Weighting of dependent and target-based criteria for optimal decision-making
     in materials selection process: Biomedical applications. Materials & Design, 49, 1000-1008.
    """

    def test_output(self):
        matrix = np.array([[0, 0, 0],
                           [0.39, 0.3, 0.77],
                           [0.17, 0.36, 0.8],
                           [0.35, 0.29, 0.93],
                           [0.3, 0.4, 0.94],
                           [0.84, 0.71, 1],
                           [1, 1, 0.99]])

        output = [0.35, 0.31, 0.34]
        output_method = [round(weight, 2) for weight in weights.standard_deviation_weights(matrix)]

        self.assertListEqual(output, output_method)


class TestMERECWeights(unittest.TestCase):
    """ Test output method with reference:
    [1] Keshavarz-Ghorabaee, M., Amiri, M., Zavadskas, E. K., Turskis, Z., & Antucheviciene, J. (2021). Determination of
    Objective Weights Using a New Method Based on the Removal Effects of Criteria (MEREC). Symmetry, 13(4), 525.
    """

    def test_output(self):
        matrix = np.array([[450, 8000, 54, 145],
                           [10, 9100, 2, 160],
                           [100, 8200, 31, 153],
                           [220, 9300, 1, 162],
                           [5, 8400, 23, 158]])

        types = np.array([1, 1, -1, -1])

        output = [0.5752, 0.0141, 0.4016, 0.0091]
        output_method = [round(weight, 4) for weight in weights.merec_weights(matrix, types)]

        self.assertListEqual(output, output_method)
