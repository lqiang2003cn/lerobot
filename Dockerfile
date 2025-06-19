FROM runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04

COPY . /lerobot_ws

CMD ["/start.sh"] 