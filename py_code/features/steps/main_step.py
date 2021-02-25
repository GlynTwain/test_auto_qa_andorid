from behave import given, when, then, step


@then('открывается экран с текстом, нажимаем далее')
@given('появляется надпись с пердупреждением и нажимаем начать')
@given('Нажимаю Далее')
def tap_next(context):
    context.app.main_screen.tap_next()


@then('нажимаем Осветить')
def tap_next(context):
    context.app.main_screen.tap_go()


@then("Выспышка света освящает воду, теперь {result}")
def anim_flash(context, result):
    result = context.app.main_screen.get()
    print(result)


@when("Вспышка освещает воду, ждём {wait_time} секунд")
def wait_animations(context,wait_time):
    context.app.main_screen.wait(time=wait_time)


@then('Закрываем, Вода освещена')
def tap_close(context):
    context.app.main_screen.tap_close()
