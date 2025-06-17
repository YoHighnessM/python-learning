# the code under doesn't work
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if front_is_clear():
#         move()

#         if not front_is_clear() and not is_facing_north() and not right_is_clear():
#             turn_left()

#             if not front_is_clear and not right_is_clear():
#                 turn_left()
#                 move()

#                 if not front_is_clear() and not right_is_clear():
#                     turn_left()

#                 if (
#                     not front_is_clear()
#                     and not is_facing_north()
#                     and not right_is_clear()
#                 ):
#                     turn_left()
#                     move()
#                 else:
#                     move()
#             elif right_is_clear() and front_is_clear:
#                 turn_right()
#                 move()
#                 turn_right()
#                 move()

#         elif right_is_clear() and front_is_clear:
#             turn_right()
#             move()
#             turn_right()
#             move()
#     elif not front_is_clear() and not is_facing_north() and not right_is_clear():
#         turn_left()
#         move()


# this code works
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_cycle():
    turn_left()

    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()

    turn_left()


while not at_goal():
    if wall_in_front():
        one_cycle()
    else:
        move()
