#!/usr/bin/env python3
import os
import platform
import subprocess
from pathlib import Path


def run_autogen():
    here = Path(__file__).parent.resolve()
    subprocess.run([f"{here}/opus/autogen.sh"],
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
                    f"--prefix={here}/install/arm64-mac"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def main():
    run_autogen()

    if platform.system() == "Darwin":
        build_arm64_mac_binaries()
        return

    raise Exception(f"opus build not supported.")


if __name__ == "__main__":
	main()
