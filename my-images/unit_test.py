from selenium import webdriver
import unittest


class MainPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('localhost:8080')

    def testDown(self):
        self.browser.close()

    def testHeaderContent(self):
        self.assertIn('Northampton Local Guide', self.brower.title)
        body = self.browser.find_element_by_id('body')
        mainheader = body.find_element_by_id('mainheader')
        mainheader_content = mainheader.text
        self.assertEqual("I expect this, mainheader_content")

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
        counters = self.browser.find_element_by_class_name('reviews')
        
        pass

    def testSortReviews(self):
        pass


if __name__ == "__main__"
    unittest.main()
