# Start with a small image
FROM python:3-alpine
# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN apk --no-cache add curl ${ADDITIONAL_PACKAGE} \ 
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.9.4/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apk del curl --no-cache
# Add non root user
WORKDIR /home/app/
# Copy the contents of the function folder to the image.
COPY  . . 
# Install required modules.
RUN pip install -r requirements.txt
# Switch to non-root user.
USER guest
# Watchdog configuration
ENV fprocess="python3 index.py"
EXPOSE 8080  
HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1
# Run the watchdog
CMD ["fwatchdog"]