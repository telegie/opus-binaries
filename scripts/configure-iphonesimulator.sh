#!/usr/bin/env bash

# reference: https://github.com/chrisballinger/Opus-iOS

../opus/autogen.sh

EXTRA_CFLAGS="-arch arm64 -miphonesimulator-version-min=14.0 -isysroot $(xcrun --sdk iphonesimulator --show-sdk-path)"

../opus/configure \
  --disable-shared \
  --disable-doc \
  --disable-extra-programs \
  --host=arm-apple-darwin \
  --prefix="$(dirname $(pwd))/e4d4b74/arm64-iphonesimulator" \
  CFLAGS="$EXTRA_CFLAGS"
