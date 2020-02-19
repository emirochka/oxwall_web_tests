from pages.locators import PostLocator
from value_object.user import User


class PostBlock:
    def __init__(self, element):
        self.element = element

    @property
    def text(self):
        return self.element.find_element(*PostLocator.POST_TEXT).text

    @property
    def time(self):
        return self.element.find_element(*PostLocator.POST_TIME).text

    @property
    def user(self):
        user_element = self.element.find_element(*PostLocator.POST_USER)
        real_name = user_element.text
        username = user_element.get_attribute("href").split("/")[-1]
        return User(username=username, real_name=real_name)

    # TODO
    def add_like(self):
        pass

    @property
    def likes_count(self):
        pass
