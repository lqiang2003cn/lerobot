
FROM runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04

RUN mkdir -p ~/miniconda3

RUN apt-get update

RUN apt-get install -y wget 

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_25.3.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

RUN bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

ARG conda_env=lerobot

ENV PATH=~/miniconda3/bin:$PATH

RUN conda create -y -n $conda_env python=3.10

ENV PATH=~/miniconda3/envs/$conda_env/bin:$PATH

RUN /bin/bash -c "source activate lerobot"

RUN apt-get install cmake build-essential python3-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev pkg-config -y

RUN conda install ffmpeg=7.1.1 -c conda-forge

RUN git clone https://github.com/huggingface/lerobot ~/lerobot

RUN cd ~/lerobot && pip install -e ".[aloha, pusht, xarm]"

CMD ["/start.sh"] 

# ENV PATH=~/miniconda3/bin:$PATH



# FROM ubuntu:22.04
# # update apt and get miniconda
# RUN apt-get update \
#     && apt-get install -y wget \
#     && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh


# # install miniconda
# ENV PATH="/root/miniconda3/bin:$PATH"
# RUN mkdir /root/.conda && bash Miniconda3-latest-Linux-x86_64.sh -b



# # create conda environment
# RUN conda init bash \
#     && . ~/.bashrc \
#     && conda create --name lerobot python=3.10 \
#     && conda activate lerobot

# RUN conda install ffmpeg=7.1.1 -c conda-forge

# RUN mkdir ~/lerobot_ws && cd ~/lerobot_ws && git clone https://github.com/huggingface/lerobot.git && cd lerobot

# RUN pip install -e ".[aloha, pusht, xarm]"




# ENV PATH="~/miniconda3/bin:$PATH"



# RUN conda init && bash ~/.bashrc && . ~/.bashrc

# RUN conda create -y -n lerobot python=3.10

# RUN conda init

# RUN conda activate lerobot

# RUN pip install pandas 



# RUN ~/miniconda3/bin/conda create --name lerobot python=3.10

# RUN ~/miniconda3/bin/conda init && bash ~/.bashrc && . ~/.bashrc

# ENV conda=~/miniconda3/bin/conda

# ENV bashrc=~/.bashrc

# RUN $conda init && . $bashrc && conda activate lerobot && pip install pandas 

# RUN source activate base 

# RUN conda activate lerobot

# RUN pip install pandas

# RUN bash Miniconda3-py310_25.3.1-1-Linux-x86_64.sh

# RUN conda init bash \
#     && . ~/.bashrc \
#     && conda create --name lerobot python=3.10 \
#     && conda activate lerobot

# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_25.3.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

# RUN bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

# RUN rm ~/miniconda3/miniconda.sh

# SHELL ["/bin/bash", "--login", "-c"]

# RUN ~/miniconda3/bin/conda create -y -n lerobot python=3.10

# RUN ~/miniconda3/bin/conda init bash

# RUN echo "conda activate myenv" > ~/.bashrc

# RUN mkdir ~/lerobot_ws && cd ~/lerobot_ws && git clone https://github.com/huggingface/lerobot.git



