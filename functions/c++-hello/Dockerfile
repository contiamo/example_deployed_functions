FROM ubuntu as builder
# install gcc
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home
COPY . .

RUN g++ -g function/handler.cpp -o function/handler
#
FROM ubuntu
RUN apt-get update \
    && apt-get -y install curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog 

RUN adduser jovyan
WORKDIR /home

COPY --from=builder /home/function/handler    .

RUN chmod u+x handler

USER jovyan

ENV fprocess="./handler"

HEALTHCHECK --interval=2s CMD [ -e /tmp/.lock ] || exit 1

#CMD ["./fwatchdog"]