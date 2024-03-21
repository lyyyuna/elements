#!/usr/bin/env bash

cd "$(dirname "$0")"

WORKDIR="$(pwd)"

manimgl ${WORKDIR}/src/elements/${1} Solution --write_file --video_dir ${WORKDIR}/build