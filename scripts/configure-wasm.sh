#!/bin/bash

# from: https://github.com/brion/ogv.js/blob/master/buildscripts/compileOpusWasm.sh

../opus/autogen.sh

emconfigure ../opus/configure \
  --disable-asm \
  --disable-intrinsics \
  --disable-doc \
  --disable-extra-programs \
  --prefix="/Users/hanseuljun/repos/telegie/deps/ffmpeg-binaries/opus-binaries/e4d4b74/wasm32-emscripten" \
  --disable-shared \
  CFLAGS="-O3"
