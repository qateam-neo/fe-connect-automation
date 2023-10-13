from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy

class SwipeHelper:
    def __init__(self, driver):
        self.driver = driver
        # Get the size of the screen
        self.screen_size = self.driver.get_window_size()
         # set how long the swipe animation should last in milliseconds.
        self.duration = 800


    def swipe_from_bottom_to_top(self,scale=0.8):
        scale = min(scale, 0.8)
        scale = max(scale, 0.2)

        # Calculate the starting and ending coordinates for the swipe
        # start_x = self.screen_size['width'] // 2
        start_x = self.screen_size['width'] * 0.05
        start_y = self.screen_size['height'] * 0.2
        # end_x = self.screen_size['width'] // 2
        end_x = self.screen_size['width'] * 0.05
        end_y = self.screen_size['height'] * scale

        # Swipe from the starting to the ending coordinates
        self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)

    def swipe_from_top_to_bottom(self,scale=0.4):
        scale = min(scale, 0.8)

        # Calculate the starting and ending coordinates for the swipe
        # start_x = self.screen_size['width'] // 2
        start_x = self.screen_size['width'] * 0.05

        start_y = self.screen_size['height'] * 0.8 
        # end_x = self.screen_size['width'] // 2
        end_x = self.screen_size['width'] * 0.05
        end_y = self.screen_size['height'] * scale

        # Swipe from the starting to the ending coordinates
        self.driver.swipe(start_x, start_y, end_x, end_y, self.duration)

    def scroll_down_to_middle(self):
        # Get screen size
        window_size = self.driver.get_window_size()
        screen_width = window_size['width']
        screen_height = window_size['height']
        
        # Calculate start and end coordinates
        start_x = int(screen_width / 2)
        start_y = int(screen_height / 4)
        end_x = int(screen_width / 2)
        end_y = int(screen_height * 3 / 4)
        # Perform swipe gesture
        self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

        
    def scroll_vertically_to_element(self, element):
        # Get the coordinates of the top and bottom of the screen
        
        screen_top = self.driver.find_element(by=MobileBy.XPATH, value="//android.view.View[1]").location['y']
        screen_bottom = self.driver.find_element(by=MobileBy.XPATH, value="//android.view.View[last()]").location['y'] + self.driver.find_element(by=MobileBy.XPATH, value="//android.view.View[last()]").size['height']

        # Get the location and size of the combo box
        combo_location = element.location['y']
        combo_height = element.size['height']
        # Calculate the distance to scroll
        # scroll_distance = combo_location + combo_height - screen_bottom
        scroll_distance = combo_location  - screen_bottom
        # Perform the scroll
        actions = TouchAction(self.driver)
        actions.press(element).move_to(x=0, y=-scroll_distance).wait(500).release().perform()