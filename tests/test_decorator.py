import allure
from allure_commons.types import Severity
from selene import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'alansinatalya')
@allure.feature('Задачи в репозитории')
@allure.story('Неавторизованный пользователь может просматривать задачи в репозитории')
@allure.link('https://github.com', name='Testing')

def test_decorator_steps():
    open_main_page()
    search_for_repositry('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_name('С Новым Годом (2022)')

@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Ищем репозиторий {repo}')
def search_for_repositry(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()

@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Открываем таб Issues')
def open_issue_tab():
    s('#issues-tab').click()

@allure.step('Проверяем наличие Issue с наименованием {name}')
def should_see_issue_with_name(name):
    s(by.partial_text(name)).should(be.visible)