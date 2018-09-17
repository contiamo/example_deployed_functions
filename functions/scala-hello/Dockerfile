FROM flangelier/scala 
WORKDIR /home

COPY . .

RUN scalac -d function function/handler.scala

RUN apk --no-cache add curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl --no-cache

RUN chmod u+x function/handler*

RUN adduser jovyan -S

USER jovyan

# hack around classpaths
WORKDIR /home/function

ENV fprocess="scala handler"

HEALTHCHECK --interval=2s CMD [ -e /tmp/.lock ] || exit 1

CMD ["/usr/bin/fwatchdog"]