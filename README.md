# opus-binaries

## Windows

Open mingw64

pacman -Syy (update pacman package list)

pacman -S mingw-w64-x86_64-libssp (required by opus to support building with fortified functions)

mkdir build

mkdir install

cd build

Run ../script/configure-mingw64.sh

make

make install

Move files outside of /install and fix prefix of opus.pc to where the files are moved.