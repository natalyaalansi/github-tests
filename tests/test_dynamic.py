import allure
from allure_commons.types import Severity
from selene import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Неавторизованный пользователь может просматривать задачи в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с наименованием "С Новым Годом (2022)"'):
        s(by.partial_text('С Новым Годом (2022)')).should(be.visible)
