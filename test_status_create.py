from pages.internal_pages import DashboardPage
import pytest


def test_post_create(logged_user, driver):
    input_text = "Great day!"
    dashboard_page = DashboardPage(driver)
    old_posts = dashboard_page.posts
    dashboard_page.create_post(input_text)
    dashboard_page.wait_new_post(len(old_posts))
    new_post = dashboard_page.posts[0]
    assert input_text in new_post.text

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

