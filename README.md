# opus-binaries

## Windows

Open mingw64

pacman -Syy (update pacman package list)

pacman -S mingw-w64-x86_64-libssp (required by opus to support building with fortified functions)

mkdir build

mkdir install

cd build

Run ../script/configure-wasm.sh

make

make install
