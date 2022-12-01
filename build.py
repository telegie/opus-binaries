#!/usr/bin/env python3
import os
import platform
import subprocess
from pathlib import Path


def run_in_mingw(extra_args, check=False):
    args = ["c:/tools/msys64/usr/bin/env",
            "MSYSTEM=MINGW64"]
    args = args + extra_args
    subprocess.run(args,
                   check=check)


def run_autogen_windows():
    here = Path(__file__).parent.resolve()
    run_in_mingw(["/bin/bash",
                  "-l",
                  f"{here}/opus/autogen.sh"],
                  check=True)


def run_autogen():
    here = Path(__file__).parent.resolve()
    subprocess.run([f"{here}/opus/autogen.sh"],
                   check=True)


def build_x64_windows_binaries():
    here = Path(__file__).parent.resolve()

    build_path = f"{here}/build/x64-windows"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run(["cmake",
                    "-S", f"{here}/opus",
                    "-B", build_path,
                    "-D", "OPUS_FORTIFY_SOURCE=OFF",
                    "-D", "OPUS_STACK_PROTECTOR=OFF",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-windows"],
                    check=True)
    subprocess.run(["msbuild",
                    f"{build_path}/INSTALL.vcxproj",
                    "/p:Configuration=RelWithDebInfo"],
                    check=True)


def build_arm64_mac_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/arm64-mac"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/opus/configure",
                    "--disable-shared",
                    "--disable-doc",
                    "--disable-extra-programs",
                    "--host=arm-apple-darwin",
                    f"--prefix={here}/install/arm64-mac",
                    "CFLAGS=-arch arm64 -O2"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_x64_mac_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/x64-mac"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/opus/configure",
                    "--disable-shared",
                    "--disable-doc",
                    "--disable-extra-programs",
                    "--host=x86_64-apple-darwin",
                    f"--prefix={here}/install/x64-mac",
                    "CFLAGS=-arch x86_64 -O2"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_arm64_ios_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/arm64-ios"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    xcrun_output = subprocess.run(["xcrun",
                                   "--sdk", "iphoneos",
                                   "--show-sdk-path"],
                                  capture_output=True,
                                  check=True)
    iphone_sdk_path = xcrun_output.stdout.decode("utf-8").strip()
    cflags=f"-arch arm64 -mios-version-min=14.0 -isysroot {iphone_sdk_path} -O2"

    subprocess.run([f"{here}/opus/configure",
                    "--disable-shared",
                    "--disable-doc",
                    "--disable-extra-programs",
                    "--host=arm-apple-darwin",
                    f"--prefix={here}/install/arm64-ios",
                    f"CFLAGS={cflags}"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_arm64_iphonesimulator_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/arm64-iphonesimulator"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    xcrun_output = subprocess.run(["xcrun",
                                   "--sdk", "iphonesimulator",
                                   "--show-sdk-path"],
                                  capture_output=True,
                                  check=True)

    iphonesimulator_sdk_path = xcrun_output.stdout.decode("utf-8").strip()
    cflags=f"-arch arm64 -miphonesimulator-version-min=14.0 -isysroot {iphonesimulator_sdk_path} -O2"

    subprocess.run([f"{here}/opus/configure",
                    "--disable-shared",
                    "--disable-doc",
                    "--disable-extra-programs",
                    "--host=arm-apple-darwin",
                    f"--prefix={here}/install/arm64-iphonesimulator",
                    f"CFLAGS={cflags}"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_x64_linux_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/x64-linux"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/opus/configure",
                    "--disable-shared",
                    "--disable-doc",
                    "--disable-extra-programs",
                    f"--prefix={here}/install/x64-linux",
                    "CFLAGS=-fPIC -O2"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_wasm32_emcsripten_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/wasm32-emscripten"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/opus/configure",
                    "--disable-shared",
                    "--disable-asm",
                    "--disable-intrinsics",
                    "--disable-doc",
                    "--disable-extra-programs",
                    f"--prefix={here}/install/wasm32-emscripten",
                    "CFLAGS=-O2"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def main():
    if platform.system() == "Windows":
        run_autogen_windows()
    else:
        run_autogen()

    if platform.system() == "Windows":
        build_x64_windows_binaries()
        return
    elif platform.system() == "Darwin":
        build_arm64_mac_binaries()
        build_x64_mac_binaries()
        build_arm64_ios_binaries()
        build_arm64_iphonesimulator_binaries()
        build_wasm32_emcsripten_binaries()
        return
    elif platform.system() == "Linux":
        build_x64_linux_binaries()
        build_wasm32_emcsripten_binaries()
        return

    raise Exception(f"opus build not supported.")


if __name__ == "__main__":
	main()
