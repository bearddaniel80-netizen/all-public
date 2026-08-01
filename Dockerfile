# syntax=docker/dockerfile:1.7
# ---------- deps ----------
FROM python:3.12-slim AS deps

WORKDIR /build

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install \
    --prefix=/install \
    -r requirements.txt

# ---------- Common Git Stage ----------
FROM deps AS git-base

COPY --from=deps /install /usr/local

RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y git

# ---------- aql-link ----------
FROM git-base AS link

COPY --from=deps /install /usr/local

RUN git clone --depth=1 https://github.com/bearddaniel80-netizen/aegis-link.git

WORKDIR aegis-link/src

RUN python -m build

RUN mv dist/*.whl /tmp/

# ---------- aql ----------
FROM deps AS aql

COPY --from=deps /install /usr/local

COPY src/ .

RUN python -m build

RUN mv dist/*.whl /tmp/

# ---------- runtime ----------
FROM deps AS runtime

COPY --from=deps /install /usr/local

COPY --from=link /tmp/*.whl /tmp

COPY --from=aql /tmp/*.whl /tmp

RUN pip install /tmp/*.whl

WORKDIR /app

COPY data .