#!/usr/bin/env bash

# reference: https://github.com/chrisballinger/Opus-iOS

../opus/autogen.sh

EXTRA_CFLAGS="-arch arm64 -mios-version-min=14.0 -isysroot $(xcrun --sdk iphoneos --show-sdk-path)"

../opus/configure \
  --disable-shared \
  --disable-doc \
  --disable-extra-programs \
  --host=arm-apple-darwin \
  --prefix="/Users/hanseuljun/repos/telegie/deps/ffmpeg-binaries/opus-binaries/e4d4b74/arm64-ios" \
  CFLAGS="$EXTRA_CFLAGS"
