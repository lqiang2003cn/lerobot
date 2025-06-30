# class TeClass:
#     def __init__(self,abc,cba):
#         self.abc=abc
#         self.cba=cba

# b = {
#     "a":TeClass(1,3),
#     "b":TeClass(2,4)
# }

# # d = list(b)
# # print(d)
# # d[0]


# current_pressed = {
#     "a":True,
#     "b":True,
#     "c":False
# }
# action = {key for key, val in current_pressed.items() if val}
# d = dict.fromkeys(action)
# print(d)

def _state_ft() -> dict[str, type]:
    return dict.fromkeys(
        (
            
            "arm_shoulder_lift.pos",
            "arm_elbow_flex.pos",
            "arm_wrist_flex.pos",
            "arm_wrist_roll.pos",
            "arm_gripper.pos",
            "x.vel",
            "y.vel",
            "theta.vel",
            "arm_shoulder_pan.pos",
        ),
        float,
    )
t = tuple(_state_ft().keys())
print(t)