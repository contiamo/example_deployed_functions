FROM alpine:edge
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories \
    && apk update \
    && apk add wget ghc ca-certificates musl-dev shadow linux-headers zlib-dev \
    && update-ca-certificates
# get function watchdog
RUN apk update \
    && apk add curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl

WORKDIR /src/handler

COPY . .

RUN ghc --make function/handler.hs -o handler

ENV fprocess="./handler"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

ENTRYPOINT ["./fwatchdog"]

