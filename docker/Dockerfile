FROM alpine:3.11.3 as base

RUN addgroup --system ci
RUN adduser --system -G ci ci
USER ci
RUN mkdir /home/ci/workdir
WORKDIR /home/ci/workdir

USER root
RUN apk add python3
USER ci

COPY --chown=ci:ci env_util env_util
ENTRYPOINT ["python3", "env_util/with_env.py"]

FROM base as bash-5.0.0

USER root
RUN apk add bash
USER ci

COPY --chown=ci:ci runners/bash/run.bash .
CMD ["bash", "run.bash"]

FROM base as python-dotenv-0.9.1

USER root
RUN apk add python3
USER ci

RUN pip3 install --user python-dotenv==0.9.1
COPY --chown=ci:ci runners/python-dotenv/run.py .

CMD ["python3", "run.py"]

FROM base as python-dotenv-0.10.1

USER root
RUN apk add python3
USER ci

RUN pip3 install --user python-dotenv==0.10.1
COPY --chown=ci:ci runners/python-dotenv/run.py .

CMD ["python3", "run.py"]

FROM base as python-dotenv-0.12.0

USER root
RUN apk add python3
USER ci

RUN pip3 install --user python-dotenv==0.12.0
COPY --chown=ci:ci runners/python-dotenv/run.py .

CMD ["python3", "run.py"]

FROM base as ruby-dotenv-2.6.0

USER root
RUN apk add ruby
RUN gem install dotenv:2.6.0
USER ci

COPY --chown=ci:ci runners/ruby-dotenv/run.rb .

CMD ["ruby", "run.rb"]

FROM base as js-dotenv-6.2.0

USER root
RUN apk add nodejs npm
USER ci

RUN npm install dotenv@6.2.0
COPY --chown=ci:ci runners/js-dotenv/run.js .

CMD ["node", "run.js"]
