# opus-binaries

## Windows

Open mingw64

pacman -Syy (update pacman package list)

pacman -S mingw-w64-x86_64-libssp (required by opus to support building with fortified functions)

pacman -Sy mingw-w64-x86_64-cmake

mkdir build

mkdir install

cd build

cmake ../opus -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=../e4d4b74/x86_64-w64-mingw32

make

make install


Note: Using ./configure leaves dll files that does not work well with MSVC.