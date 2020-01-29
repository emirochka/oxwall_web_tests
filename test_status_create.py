def test_status_create(logged_user, app):
    old_posts = app.get_posts()
    app.create_post("Great day!!!")
    app.wait_new_post(len(old_posts))
    new_post = app.get_posts()[0]
    assert new_post.text == "Great day!!!"
    # assert new_post.author == logged_user
    # assert new_post.time == "within 1 min"


# def test_set_like_to_post(logged_user, app):
#     post = app.get_posts()[0]
#     likes_before = post.get_likes()
#     post.set_like()
#     assert post.get_likes() == likes_before + 1

