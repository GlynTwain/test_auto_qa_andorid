# Created by shity at 25.02.2021
Feature: # Работа анимации "меню"
  # Enter feature description here

  Scenario: # Проверить работу карусели Нажатиями
    Given Нажимаю Далее
    Given Нажимаю Далее
    Given Нажимаю Далее

  Scenario: # Проверить работу карусели Свайпами назад
    Then Свайпаем влево
    Then Свайпаем влево
    Then Свайпаем вправо
    Then Свайпаем вправо