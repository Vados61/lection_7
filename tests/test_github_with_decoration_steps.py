import allure
from allure_commons.types import Severity, AttachmentType
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Vados61')
@allure.feature('Проверка наличия задачи в репозитории')
@allure.story('Тест с помощью задекорированных шагов')
@allure.link('https://github.com', name='Testing')
def test_issue_name():
    open_home_page('https://github.com')
    search_repo('eroshenkoam/allure-example')
    get_first_item()
    go_to_issues()
    check_issue('С Новым Годом (2022)')
    get_screenshot()


@allure.step('Открываем главную страницу')
def open_home_page(url):
    browser.open(url)


@allure.step('Ищем репозиторий - {repo_name}')
def search_repo(repo_name):
    s("button[aria-label='Toggle navigation'] .Button-content").click()
    s('.header-search-input').click().send_keys(repo_name)
    s('.header-search-input').press_enter()


@allure.step('Выбираем первый в списке')
def get_first_item():
    ss('.repo-list>li a').first().click()


@allure.step('Переходим в раздел Issues')
def go_to_issues():
    s('#issues-tab').click()


@allure.step('Проверяем наличие issue с описанием: {text}')
def check_issue(text):
    s(by.partial_text(text)).should(be.visible)


@allure.step('Делаем скриншот результата')
def get_screenshot():
    allure.attach(browser.driver.get_screenshot_as_png(), name='Screen', attachment_type=AttachmentType.PNG)
