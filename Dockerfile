FROM node:16-alpine AS front

WORKDIR ${APP_ROOT}
COPY --chown=${USER} ./pokeml-front .
# remove node_modules and dist folders as esbuild is platform-specific and will cause error during npm run build
RUN rm -rf ${APP_ROOT}/node_modules ${APP_ROOT}/dist

RUN npm install && \
    npm run build

FROM python:3.11-alpine AS api

WORKDIR ${APP_ROOT}
COPY --chown=${USER} ./pokeml-api .
COPY --chown=${USER} --from=front ${APP_ROOT}/dist ./src/resources

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

EXPOSE 5000

CMD ["python", "src/controller.py"]
