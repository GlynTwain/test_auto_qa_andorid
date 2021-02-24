from behave import given, when, then, step


@given('Нажимаю Далее')
@given('Нажимаю Начать')
def tap_next(context):
    context.app.main_screen.tap_next()


@given('Начинаем Освещение')
def tap_next(context):
    context.app.main_screen.tap_go()


@then("Выспышка света освящает воду, теперь {result}")
def anim_flash(context, result):
    result = context.app.main_screen.get()
    print(result)


@when("Да Озарит воду, впышка свещенного света")
def wait_animations(context):
    context.app.main_screen.wait()


@given('Закрываем, Вода освещена')
def tap_close(context):
    context.app.main_screen.tap_close()
