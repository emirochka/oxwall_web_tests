from conftest import PROJECT_DIR
from pages.internal_pages import DashboardPage
import pytest
import json
from data.random_string import random_string
import os.path

filename = os.path.join(PROJECT_DIR, "data", "posts.json")


with open(filename, encoding="utf8") as f:
    post_text_list = json.load(f)

for _ in range(3):
    post_text_list.append(random_string(maxlen=1000, spaces=True, whitespases=True))


@pytest.mark.nondestructive
@pytest.mark.parametrize("input_text", post_text_list)
def test_post_create(logged_user, driver, input_text, db):
    dashboard_page = DashboardPage(driver)
    old_posts = dashboard_page.posts
    dashboard_page.create_post(input_text)
    dashboard_page.wait_new_post(len(old_posts))
    assert db.get_last_text_post() == input_text
    new_post = dashboard_page.posts[0]
    assert new_post.text == input_text
    assert new_post.time == "within 1 minute"
    assert new_post.user == logged_user

    # old_posts = app.get_posts()
    # app.create_post("Great day!!!")
    # app.wait_new_post(len(old_posts))
    # new_post = app.get_posts()[0]
    # assert new_post.text == "Great day!!!"
    # assert new_post.author == logged_user
    # assert new_post.time == "within 1 min"


# def test_set_like_to_post(logged_user, app):
#     post = app.get_posts()[0]
#     likes_before = post.get_likes()
#     post.set_like()
#     assert post.get_likes() == likes_before + 1

