FROM ubuntu:latest



RUN apt-get update && apt-get install -y \
    macchanger \
    net-tools \
    iproute2 \
    network-manager  


COPY ./notes.txt /notes.txt

CMD ["/bin/bash"]
