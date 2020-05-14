FROM centos:latest

WORKDIR /workspace

ENV MAIL=somemail

RUN yum install python3 -y && pip3 install ansible

COPY . .

CMD ["/bin/bash" , "script.sh" ]