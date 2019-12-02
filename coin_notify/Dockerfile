FROM python:3-onbuild

RUN apt-get update && apt-get -y install cron

COPY start.sh /start.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["python manage.py crontab add"]
CMD ["/start.sh"]
