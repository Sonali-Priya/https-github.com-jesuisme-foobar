from foobar import FoobarClass
import csv
from math import sqrt
import unittest


class ChildClass(FoobarClass):
    """
            Initialize the class
            :param items: It contains the list of card labels
            :param email_list: It contains the list of emails
            :param scores: It contains the list of scores of students
    """
    def __init__(self):
        FoobarClass.__init__(self)
        self.items = []
        self.pop_list = []
        self.email_list = []
        self.scores = []
        self.my_list = []

    def read_data(self):
        # pop_list = []
        """
               The read_data reads from the csv file supplied
        """

        with open('student_responses.csv', 'r') as file:
            read_file = csv.reader(file)
            for row in read_file:
                self.items.append(row)
                # print("Items", self.items)

            for i in range(len(self.items)):
                my_list = self.items[i]


                # if my_list[-1] not in pop_list:
                self.pop_list = my_list.pop()
                # if self.pop_list not in self.email_list:
                self.email_list.append(self.pop_list)
            # print("Email_List+++", self.email_list)
            # print("Card_Labels+++", self.items)

    def compute_score(self):
        """
        To compute score for each card_label
        The output format of the csv file will be:
        <student id>, <score>
        :return:
        """
        scores = []
        for card_label in self.items:
            str_ans = self.transform_card_order_to_string(card_label)
            incorrect_cards = self.levenshtein_score(str_ans)
            correct_cards = len(self.code_map) - incorrect_cards
            score = (correct_cards * 4) - (incorrect_cards * 2)
            scores.append(score)
        self.scores = scores
        # print("scores",scores)

    def write_student_scores(self):
        """
        To write score in CSV file
        :return:
        """
        with open('result.csv', 'w', newline='') as file:
            write_file = csv.writer(file, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            i = 0
            for score in self.scores:
                percent = (score / self.max_score) * 100
                # print("Percentage--", percent)
                write_file.writerow([self.email_list[i]] + [str(score)] + [str(percent)])

                i += 1

    def average(self):

        """Calculates the average of the student raw scores"""

        avg = float(sum(self.scores)) / len(self.scores)
        print("Average", avg)

        self.avg = avg

    def standard_deviation(self):
        """ Calculates the standard deviation of the student raw scores """
        # self.standard_dev = standard_dev
        list = []
        for x in self.scores:
            list.append(x - self.avg)
        # print("List",list)

        sqr = []
        for x in list:
            sqr.append(x * x)
        # print("sqr", sqr)

        Sum_sqr = sum(sqr)
        # print("Sum of squares", Sum_sqr)

        variance = 1 / len(sqr) * Sum_sqr
        # print("Variance", variance)

        standard_dev = sqrt(variance)
        print("Standard deviation ", standard_dev)


class ChildTestClass(unittest.TestCase):
    def test_readdata(self):
        self.assertGreater(len(child_obj.items), 0)

    def test_computescore(self):
        self.assertGreater(len(child_obj.scores), 0)

    '''def test_writestudentscores(self):
        child_obj = ChildClass
        child_obj.read_data()
        child_obj.compute_score()
        child_obj.write_student_scores()
        child_obj.write_file.seek(0)
        content = child_obj.write_file.read()
        self.assertTrue(child_obj.content,"test@test.com,4,14.285714285714285")'''

    '''def test_average(self):
        self.assertEqual(child_obj.avg, 7.6)'''

    '''def test_standarddeviation(self):

        self.assertEqual(child_obj.standard_deviation(),11.757550765359253)


        #self.assertIn(child_obj.standard_deviation(138.23999999999998), 11.757550765359253)'''

    def test_transform_card_order_to_string(self):
        self.assertEqual('a', child_obj.transform_card_order_to_string(['A1']))


if __name__ == '__main__':
    unittest.main()

child_obj = ChildClass()
child_obj.read_data()
child_obj.compute_score()
child_obj.write_student_scores()
child_obj.average()
child_obj.standard_deviation()
