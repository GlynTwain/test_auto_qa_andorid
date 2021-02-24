# Created by shity at 24.02.2021
Feature: # Работа главной функции приложения - ОсвЕщения воды
  # Enter feature description here

  Scenario: # Необходимо проследовать через меню к освЕщению воды
    Given Нажимаю Далее
    Given Нажимаю Далее
    Given Нажимаю Далее
    Given Нажимаю Начать
    When Озарит воду впышка свещенного света
    #Given На экране предупреждения нажимаю Начать
    Then Выспышка света освящает воду, теперь {context.result}
    Given Закрываем, Вода освещена


    """com.xaxtix.team.waterillunimation:id/exo_subtitles"""