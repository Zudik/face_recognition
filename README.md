docker run --interactive --device=/dev/video0:/dev/video0 --tty --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix/:/tmp/.X11-unix/ zudik/face_recognition

