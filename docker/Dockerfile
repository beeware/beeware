FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y git python3-dev python3-pip libgirepository1.0-dev libcairo2-dev libpango1.0-dev libwebkitgtk-3.0-0 gir1.2-webkit-3.0
RUN python3 -m pip install MarkupSafe
RUN python3 -m pip install --pre beeware

WORKDIR project
ENTRYPOINT ["briefcase"]
