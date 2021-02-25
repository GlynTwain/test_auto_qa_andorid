from behave import given, when, then, step


@then("Свайпаем {direction}")
def swipe_right(context, direction):
    direction.lower()

    if direction == "влево":
        context.app.next_screen.swipe(x1=977, y1=803, x2=136, y2=800)
    elif direction == "вправо":
        context.app.next_screen.swipe(x1=136, y1=800, x2=977, y2=803)
    else:
        assert 'Нет заданного направления'
    # context.app.next_screen.swipe(direction)
