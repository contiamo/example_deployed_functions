FROM julia

# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.8.10/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog 

# Add non root user
RUN adduser jovyan

WORKDIR /home

COPY handler.jl         .

RUN chown -R jovyan /home

USER jovyan

ENV fprocess="julia handler.jl"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
