import time

from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from lerobot.common.datasets.utils import hw_to_dataset_features
from lerobot.common.robots.lekiwi.config_lekiwi import LeKiwiClientConfig
from lerobot.common.robots.lekiwi.lekiwi_client import LeKiwiClient
from lerobot.common.teleoperators.keyboard import KeyboardTeleop, KeyboardTeleopConfig
from lerobot.common.teleoperators.so100_leader import SO100Leader, SO100LeaderConfig

NB_CYCLES_CLIENT_CONNECTION = 250

leader_arm_config = SO100LeaderConfig(port="/dev/tty.usbmodem58760431551")
leader_arm = SO100Leader(leader_arm_config)

keyboard_config = KeyboardTeleopConfig()
keyboard = KeyboardTeleop(keyboard_config)

robot_config = LeKiwiClientConfig(remote_ip="172.18.134.136", id="lekiwi")
lekiwi_client = LeKiwiClient(robot_config)

action_features = hw_to_dataset_features(lekiwi_client.action_features, "action")
obs_features = hw_to_dataset_features(lekiwi_client.observation_features, "observation")
dataset_features = {**action_features, **obs_features}

dataset = LeRobotDataset.create(
    repo_id="pepijn223/lekiwi" + str(int(time.time())),
    fps=10,
    features=dataset_features,
    robot_type=lekiwi_client.name,
)

leader_arm.connect()
keyboard.connect()
lekiwi_client.connect()

if not lekiwi_client.is_connected or not leader_arm.is_connected or not keyboard.is_connected:
    exit()

print("Starting LeKiwi recording")
i = 0
while i < NB_CYCLES_CLIENT_CONNECTION:
    arm_action = leader_arm.get_action()
    arm_action = {f"arm_{k}": v for k, v in arm_action.items()}

    keyboard_keys = keyboard.get_action()

    base_action = lekiwi_client._from_keyboard_to_base_action(keyboard_keys)

    action = {**arm_action, **base_action} if len(base_action) > 0 else arm_action

    action_sent = lekiwi_client.send_action(action)
    # action_sent is formatted as:
    # {
    #     "action":{
    #         "arm_shoulder_pan.pos":1,
    #         "arm_shoulder_lift.pos":2,
    #         "arm_elbow_flex.pos":2,
    #         "arm_wrist_flex.pos":2,
    #         "arm_wrist_roll.pos":2,
    #         "arm_gripper.pos":2,
    #         "x.vel":2,
    #         "y.vel":2,
    #         "theta.vel":2,
    #     }
    # }

    # the client pull messages from the zmq socket
    observation = lekiwi_client.get_observation()
    # observation = {
        #   "observation.state" : np.array(9),
        #   "observation.images.front":np.array(h,w,3),  # maybe np.array(3,h,w)?
        #   "observation.images.wrist":np.array(h,w,3)
    # }

    frame = {**action_sent, **observation}
    # frame = {
    #     "action":{
    #         "arm_shoulder_pan.pos":1,
    #         "arm_shoulder_lift.pos":2,
    #         "arm_elbow_flex.pos":2,
    #         "arm_wrist_flex.pos":2,
    #         "arm_wrist_roll.pos":2,
    #         "arm_gripper.pos":2,
    #         "x.vel":2,
    #         "y.vel":2,
    #         "theta.vel":2,
    #     },
    #     "observation.state" : np.array(9),
    #     "observation.images.front":torch.array(h,w,3),  # maybe np.array(3,h,w)?
    #     "observation.images.wrist":torch.array(h,w,3)
    # }


    task = "Dummy Example Task Dataset"

    dataset.add_frame(frame, task)
    i += 1

print("Disconnecting Teleop Devices and LeKiwi Client")
lekiwi_client.disconnect()
leader_arm.disconnect()
keyboard.disconnect()

print("Uploading dataset to the hub")
dataset.save_episode()
dataset.push_to_hub()
