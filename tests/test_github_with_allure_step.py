import allure
from allure_commons.types import Severity, AttachmentType
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Vados61')
@allure.feature('Проверка наличия задачи в репозитории')
@allure.story('Тест с помощью шагов в контекстном менеджере')
@allure.link('https://github.com', name='Testing')
def test_issue_name():
    with allure.step('Открываем главную страницу'):
        browser.open("https://github.com")

    with allure.step('Ищем репозиторий'):
        s("button[aria-label='Toggle navigation'] .Button-content").click()
        s('.header-search-input').click().send_keys("eroshenkoam/allure-example")
        s('.header-search-input').press_enter()

    with allure.step('Выбираем первый в списке'):
        ss('.repo-list>li a').first().click()

    with allure.step('Переходим в раздел Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие issue с нужным описанием'):
        s(by.partial_text('С Новым Годом (2022)')).should(be.visible)

    with allure.step('Делаем скриншот результата'):
        allure.attach(browser.driver.get_screenshot_as_png(), name='Screen', attachment_type=AttachmentType.PNG)
