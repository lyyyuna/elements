#!/usr/bin/env bash

cd "$(dirname "$0")"

WORKDIR="$(pwd)"

manim -p ${WORKDIR}/src/elements/${1} Solution