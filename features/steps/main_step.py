from behave import given, when, then, step

@given('Tap next')
def tap_next(context):
    context.app.main_screen.tap_next()

@given('Tap next1')
def tap_next(context):
    context.app.main_screen.tap_next()

@given('Tap next2')
def tap_next(context):
    context.app.main_screen.tap_next()