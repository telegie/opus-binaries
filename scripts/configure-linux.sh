#!/usr/bin/env bash

../opus/autogen.sh

../opus/configure \
  --disable-shared \
  --disable-doc \
  --disable-extra-programs \
  --prefix="$(dirname $(pwd))/e4d4b74/x64-linux" \