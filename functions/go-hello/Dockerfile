
FROM golang:1.9.7-alpine3.7 as builder

RUN apk --no-cache add curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl --no-cache
# needs to be /go/src/ this is where $GOROOT points.
WORKDIR /go/src/handler 
COPY . .

# Run a gofmt and exclude all vendored code.
#RUN test -z "$(gofmt -l $(find . -type f -name '*.go' -not -path "./vendor/*" -not -path "./function/vendor/*"))" || { echo "Run \"gofmt -s -w\" on your Golang code"; exit 1; }

RUN go build --ldflags "-s -w" -a -installsuffix cgo -o handler . 

FROM gcr.io/distroless/base

COPY --from=builder /go/src/handler/handler /
COPY --from=builder /usr/bin/fwatchdog /

ENV fprocess="./handler"

HEALTHCHECK --interval=2s CMD [ -e /tmp/.lock ] || exit 1#

ENTRYPOINT ["./fwatchdog"]