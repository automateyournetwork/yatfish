FROM ubuntu:latest

RUN echo "==> Upgrading apk and installing system utilities..." \
  && apt -y update \
  && apt-get install -y wget \
  && apt-get -y install sudo

RUN echo "==> Installing Python3 and pip..." \
  && apt-get install python3 -y \
  && apt install python3-pip -y \
  && apt install openssh-client -y

RUN echo "==> Adding pyATS..." \
  && pip install pyats[full]

RUN echo "==> Adding Batfish..." \
  && pip install pybatfish

COPY /yatfish /yatfish/
COPY /scripts /scripts/

RUN echo "==> Install dos2unix..." \
  && sudo apt-get install dos2unix -y

RUN echo "==> Convert script..." \
  && dos2unix /scripts/startup.sh

CMD ["/bin/bash", "/scripts/startup.sh"]