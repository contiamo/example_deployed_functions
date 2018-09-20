FROM rust as builder

RUN echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog 

WORKDIR /rust/src/handler
COPY . .

RUN rustc function/handler.rs -o handler

FROM gcr.io/distroless/cc
#FROM ubuntu
COPY --from=builder /rust/src/handler /
COPY --from=builder /usr/bin/fwatchdog /
ENV fprocess="./handler"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1#

CMD ["./fwatchdog"]
