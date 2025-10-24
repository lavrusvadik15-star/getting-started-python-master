from selene import browser, be, have


browser.open('https://invoice.taxcom.ru/')
browser.element('[id="loginPassTab"]').click()
browser.element('[name="login"]').type('gendalf')
browser.element('[name="password"]').type('gendalf')
browser.element('[class="ui primary button wrappers__StyledButton-sc-k6oskv-0 gfygBj"]').click()




 #should(be.blank).press_enter())

# should(have.text(''))
