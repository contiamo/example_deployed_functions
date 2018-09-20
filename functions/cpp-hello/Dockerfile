FROM ubuntu as builder
# get watchdog 
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get -y install curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

# install gcc
RUN apt-get -y install gcc mono-mcs 

WORKDIR /cpp/src/handler
COPY . .

RUN g++ -g function/handler.cpp -o handler

FROM gcr.io/distroless/cc
COPY --from=builder /cpp/src/handler /
COPY --from=builder /usr/bin/fwatchdog /
ENV fprocess="./handler"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["./fwatchdog"]