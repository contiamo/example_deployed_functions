FROM haskell as builder
# get function watchdog
RUN apt-get update \
    && apt-get -y install curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog 

WORKDIR /src/handler

COPY . .

RUN ghc --make function/handler.hs -o handler

#FROM gcr.io/distroless/java
FROM ubuntu
COPY --from=builder /src/handler /
COPY --from=builder /usr/bin/fwatchdog /
ENV fprocess="./handler"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

ENTRYPOINT ["./fwatchdog"]