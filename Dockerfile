FROM ubuntu:20.04
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y --fix-missing \
    libgtk2.0-dev \
    libglib2.0-0 \
    libgl1-mesa-glx \
    python3-pip\
    && apt-get clean && rm -rf /tmp/* /var/tmp/*
COPY . /root/face_recognition
RUN cd /root/face_recognition && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
CMD cd /root/face_recognition/face_recognition && \
    python3 main_run.py
