FROM haskell as builder

COPY . .

RUN ghc --make /function/handler.sh -o /function/handler
# go test $(go list ./... | grep -v /vendor/) -cover

FROM python:3-alpine
RUN apk --no-cache add curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl --no-cache
RUN apk --no-cache add ca-certificates

# Add non root user
RUN addgroup -S app && adduser -S -g app app
RUN mkdir -p /home/app

WORKDIR /home/app

COPY --from=builder /usr/bin/fwatchdog         .

COPY --from=builder /haskell/src/handler/function/  .
COPY --from=builder /haskell/src/handler/handler    .

RUN chown -R app /home/app

USER app

ENV fprocess="./handler"

HEALTHCHECK --interval=2s CMD [ -e /tmp/.lock ] || exit 1

CMD ["./fwatchdog"]