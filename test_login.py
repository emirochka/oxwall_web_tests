from pages.internal_pages import MainPage


def test_login(driver):
    user = "admin"
    password = "pass"

    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    sign_in_page.fill_form(user, password)
    dashboard_page = sign_in_page.submit()
    assert dashboard_page.is_this_page()
