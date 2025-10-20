#!/usr/bin/env python3

# Copyright 2024 Shane Loretz.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import subprocess


# TODO(j-rivero) share implementation with build_images.py
def _full_name(registry, name, tag):
    return f"{registry}/{name}:{tag}"


def _pull(full_name, dry_run):
    cmd = ["docker", "pull", full_name]
    if dry_run:
        print(cmd)
    else:
        subprocess.check_call(cmd)


def _run(full_name, extra_cmd, platform=None, dry_run=False):
    cmd = ["docker", "run", "--rm=true"]
    if platform:
        cmd.append("--platform")
        cmd.append(platform)
    cmd.append(full_name)
    cmd.extend(extra_cmd)
    if dry_run:
        print(cmd)
    else:
        subprocess.check_call(cmd)


def _print_gz_help(full_name, platform=None, dry_run=False, gazebo_release=""):
    if gazebo_release == "fortress":
        cmd = ["ign", "sim", "--help"]
    else:
        cmd = ["gz", "sim", "--help"]
    _run(full_name, cmd, platform, dry_run)


def _print_pkg_version(full_name, pkg, platform=None, dry_run=False):
    cmd = ["apt-cache", "show", pkg]
    _run(full_name, cmd, platform, dry_run)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="localhost", type=str)
    parser.add_argument("--image-name", default="gazebo", type=str)
    parser.add_argument("--release", required=True, type=str)
    parser.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    return args


def main():
    args = parse_arguments()

    gazebo_release = args.release.lower()
    dry_run = args.dry_run

    amd64 = "linux/amd64"
    arm64 = "linux/arm64/v8"

    combos = [
        ("core", amd64),
        ("full", amd64),
        ("core", arm64),
        ("full", arm64),
    ]
    for image, platform in combos:
        tag = f"{gazebo_release}-{image}"
        package = f"gz-{gazebo_release}"
        full_name = _full_name(args.registry, args.image_name, tag)
        _pull(full_name, dry_run)
        _print_pkg_version(full_name, package, platform, args.dry_run)
        _print_gz_help(full_name, platform, dry_run, gazebo_release)


if __name__ == "__main__":
    main()
