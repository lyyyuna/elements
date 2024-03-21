#!/usr/bin/env bash

cd "$(dirname "$0")"

WORKDIR="$(pwd)"

manimgl ${WORKDIR}/src/elements/${1} Solution