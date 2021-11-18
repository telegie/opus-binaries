#!/bin/bash

#reference: https://github.com/msys2/MINGW-packages/issues/5868
#reference: https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-opus/PKGBUILD

../opus/autogen.sh

export LDFLAGS="-lssp"  # for _FORTIFY_SOURCE

../opus/configure \
  --host=x86_64-w64-mingw32 \
  --prefix=/c/Users/hanseul/repos/telegie/deps/ffmpeg-binaries/opus-binaries/install
