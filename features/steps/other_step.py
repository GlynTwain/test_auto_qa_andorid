from behave import given, when, then, step

@given("Свайпаем влево")
def swipe_right(context):
    context.app.main_screen.swipe()
