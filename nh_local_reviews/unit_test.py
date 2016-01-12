from selenium import webdriver
import unittest


class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8084/')

    def tearDown(self):
        self.browser.close()

    def testHeaderContent(self):
        self.assertIn('Northampton Local Guide', self.browser.title)
        body = self.browser.find_element_by_tag_name('body')
        mainheader = body.find_element_by_id('mainheader')
        mainheader_content = mainheader.text
        self.assertEqual("Welcome to your best guide to Northampton, MA", mainheader_content)

    # Goal of test:
    #  click on +1 RIGHT counter increases
    #  click on -1 RIGHT counter decreases
    #       el = find.element_by_...
    #       el.click()
    #
    #    find the counters
    #    record their values
    #    find the +1 button and counter
    #        verify the counter increases
    #
    #    find the -1 button and counter
    #        verify the counter decreases
    def testLikeDislike(self):
        """ Let's setup a dictionary to hold our review likes """
        review_likes = {}
        num_clicks = 20

        reviews = self.browser.find_elements_by_class_name('review')
        for review in reviews:
            """ let's fill our dictionary with the review name and initial like count """
            header = review.find_element_by_tag_name('header')
            like_count = review.find_element_by_class_name('like_count')
            review_likes[header.text] = like_count.text

            """ let's test our +1 button """
            like_button = review.find_element_by_class_name('likebutton')
            for num in range(0, num_clicks):
                like_button.click()
            self.assertEqual(int(review_likes[header.text]) + num_clicks, int(like_count.text))

            """ let's test our -1 button """
            dislike_button = review.find_element_by_class_name('dislikebutton')
            for num in range(0, num_clicks):
                dislike_button.click()
            self.assertEqual(int(review_likes[header.text]), int(like_count.text))

    def testSortReviews(self):
        """ how about setting up what we expect our sort order to be """
        expected_order = [15,15,25,45]
        reverse_expected_order = list(expected_order)
        reverse_expected_order.reverse()

        """ let's do a sort """
        btn_sort = self.browser.find_element_by_id('btn_sort')
        btn_sort.click()

        """ now test our sort """
        review_likes = []
        reviews = self.browser.find_elements_by_class_name('review')
        for review in reviews:
            like_count = review.find_element_by_class_name('like_count')
            review_likes.append(int(like_count.text))
        self.assertEqual(review_likes, expected_order)

        """ let's do a reverse order sort """
        chk_sorted_order_reverse = self.browser.find_element_by_id('chk_sorted_order_reverse')
        chk_sorted_order_reverse.click()
        btn_sort = self.browser.find_element_by_id('btn_sort')
        btn_sort.click()

        """ now test our reverse order sort """
        review_likes = []
        reviews = self.browser.find_elements_by_class_name('review')
        for review in reviews:
            like_count = review.find_element_by_class_name('like_count')
            review_likes.append(int(like_count.text))
        self.assertEqual(review_likes, reverse_expected_order)


if __name__ == "__main__":
    unittest.main()
