# opus-binaries

## How to Build

- git submodule update --init --recursive
- python3 build.py

## For Windows

Open mingw64

pacman -Syy (update pacman package list)

pacman -Sy mingw-w64-x86_64-cmake

mkdir build

cd build

cmake ../opus -G "Unix Makefiles" -DOPUS_FORTIFY_SOURCE=OFF -DOPUS_STACK_PROTECTOR=OFF -DCMAKE_INSTALL_PREFIX=../e4d4b74/x64-windows

make

make install

Note: Using ./configure leaves dll files that does not work well with MSVC.
