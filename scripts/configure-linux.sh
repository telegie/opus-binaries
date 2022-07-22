#!/usr/bin/env bash

../opus/autogen.sh

../opus/configure \
  --disable-shared \
  --disable-doc \
  --disable-extra-programs \
  --prefix="/Users/hanseuljun/repos/telegie/deps/ffmpeg-binaries/opus-binaries/e4d4b74/x64-linux" \
