from selenium import webdriver


def tjgo(nome):

    driver = webdriver.Chrome()
    driver.get("https://projudi.tjgo.jus.br/BuscaProcessoPublica")
    driver.find_element_by_xpath(
        '//*[@id="NomeParte"]').send_keys("{}".format(nome))
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/form/div/fieldset/div/input[1]").click()
    from time import sleep



