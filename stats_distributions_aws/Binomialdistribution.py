import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    def __init__(self, p=0.5, n=10):
        self.p = p
        self.n = n
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        self.mean = self.p * self.n
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        self.p = sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        plt.bar(x=['0', '1'], height=[(1-self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of Binomial Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        pnk = math.factorial(k) / (math.factorial(self.n) * math.factorial(self.n - k))
        prob = (self.p ** k) * (1 - self.p) ** (self.n - k)

        return pnk * prob

    def plot_histogram_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
        None

        Returns:
        list: x values for the pdf plot
        list: y values for the pdf plot

        """
        x = []
        y = []

        for k in range(0, self.n + 1):
            x.append(k)
            y.append(self.pdf(k))

        plt.bar(x, y)
        plt.title("Plot of Probability Density \n of Binomial Distribution")
        plt.xlabel("Values")
        plt.ylabel("Probability Density")
        plt.show()

        return x, y

    def __add__(self, other):
        """Function to add together two Binomial stats_distributions_aws with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """
        string = "mean {}, standard deviation {}, p {}, n {}".\
            format(self.mean, self.stdev, self.p, self.n)

        return string
