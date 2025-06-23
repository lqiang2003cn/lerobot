# /home/lq/lqtech/ros2_workspaces/ws_moveit2/src/moveit2/moveit_ros/moveit_servo/lerobot_data/wx250s/data/chunk_000/episode_000003.parquet

import time

from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from lerobot.common.datasets.utils import hw_to_dataset_features
from lerobot.common.robots.lekiwi.config_lekiwi import LeKiwiClientConfig
from lerobot.common.robots.lekiwi.lekiwi_client import LeKiwiClient
from lerobot.common.teleoperators.keyboard import KeyboardTeleop, KeyboardTeleopConfig
from lerobot.common.teleoperators.so100_leader import SO100Leader, SO100LeaderConfig

# data.axes[6], # 末端向左向右直线移动:x+,x- 左边下面的十字按键：向左为1，向右为-1 axes[6] D_PAD_X:left_right
# data.axes[7], # 末端向前向后直线移动:y+,y- 左边下面的十字按键：向上为1，向下为-1 axes[7] D_PAD_Y:forward_backward
# data.axes[2], # 末端向上直线移动：z+ 左边前面下边的按钮：默认为1，向下按为-1 axes[2] LEFT_TRIGGER:up
# data.axes[5], # 末端向下直线移动:z- 右边前面下边的按钮：默认为1，向下按为-1 axes[5] RIGHT_TRIGGER:down
# data.buttons[2], # x轴正方向旋转 右边上面的X键 buttons[2] X:x_righthand_rotate
# data.buttons[1], # x轴反方向旋转 右边上面的B键 buttons[1] B:x_counter_righthand_rotate
# data.buttons[3], # y轴正方形旋转 右边上面的Y键 buttons[3] Y:y_righthand_rotate
# data.buttons[0], # y轴反方形旋转 右边上面的A键 buttons[0] A:y_counter_righthand_rotate
# data.buttons[4], # z轴正方向旋转 左边前面上边的按钮 buttons[4] LEFT_BUMPER:z_righthand_rotate
# data.buttons[5], # z轴反方向旋转 右边前面上边的按钮 buttons[5] RIGHT_BUMPER:z_counter_righthand_rotate
# data.buttons[6], # 打开gripper 左边上边右两个小长方形的按键  buttons[6] CHANGE_VIEW:open_gripper
# data.buttons[7], # 关闭gripper 右边上边有三条直线的按键 buttons[7] MENU:close_gripper

action_features_dict = dict.fromkeys(
    (
        "left_right",
        "forward_backward",
        "up",
        "down",
        "x_righthand_rotate",
        "x_counter_righthand_rotate",
        "y_righthand_rotate",
        "y_counter_righthand_rotate",
        "z_righthand_rotate",
        "z_counter_righthand_rotate",
        "open_gripper",
        "close_gripper",
    ),
    float,
)

observation_features_dict = dict.fromkeys(
    (
        "waist.pos",
        "sholder.pos",
        "elbow.pos",
        "forearm_roll.pos",
        "wrist_angle.pos",
        "wrist_rotate.pos",
        "left_finger_joint.pos",
        "right_finger_joint.pos",
    ),
    float,
)

action_features = hw_to_dataset_features(action_features_dict, "action")
obs_features = hw_to_dataset_features(observation_features_dict, "observation")
dataset_features = {**action_features, **obs_features}

dataset = LeRobotDataset.create(
    repo_id="lingqi-tech/wx250s_put_red_cube_on_blue_cube",
    fps=50,
    features=dataset_features,
    robot_type="wx250s",
)

# read frames from collected data in Ros2
# /home/lq/lqtech/ros2_workspaces/ws_moveit2/src/moveit2/moveit_ros/moveit_servo/lerobot_data/wx250s/data/chunk_000/episode_000003.parquet


print(dataset)