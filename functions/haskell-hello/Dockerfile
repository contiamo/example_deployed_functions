FROM haskell as builder

WORKDIR /home

COPY . .

RUN ghc --make function/handler.hs -o handler

FROM ubuntu
RUN adduser jovyan
WORKDIR /home

RUN apt-get update \
    && apt-get -y install curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog 

COPY --from=builder /home/function/handler    .

RUN chmod u+x handler

USER jovyan

ENV fprocess="./handler"

HEALTHCHECK --interval=2s CMD [ -e /tmp/.lock ] || exit 1

CMD ["/usr/bin/fwatchdog"]