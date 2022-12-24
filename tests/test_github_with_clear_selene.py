import allure
from allure_commons.types import Severity, AttachmentType
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Vados61')
@allure.feature('Проверка наличия задачи в репозитории')
@allure.story('Тест с помощью только Selene')
@allure.link('https://github.com', name='Testing')
def test_issue_name():
    browser.open('https://github.com')

    s("button[aria-label='Toggle navigation'] .Button-content").click()
    s('.header-search-input').click().send_keys('eroshenkoam/allure-example')
    s('.header-search-input').press_enter()
    ss('.repo-list>li a').first().click()
    s('#issues-tab').click()

    s(by.partial_text('С Новым Годом (2022)')).should(be.visible)
    allure.attach(browser.driver.get_screenshot_as_png(), name='Screen', attachment_type=AttachmentType.PNG)
