# Face recognition in real-time.
Python3 + OpenCV + SQLite3
## Getting ready to work
### Create folders:
 - /data/faces
 - /data/trainer
### Pyvenv:
 - pip3 install -r requirements.txt
### Docker:
 - docker build -t docker_hub_name/face_recognition .
 - docker run --interactive --device=/dev/video0:/dev/video0 --tty --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix/:/tmp/.X11-unix/ docker_hub_name/face_recognition


