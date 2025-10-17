# Gazebo Open Container Initiative Images

[Open Container Initiative](https://opencontainers.org/) images for [Gazebo](https://gazebosim.org)!


Are you looking for **Docker images**?
You're in the right spot!
OCI images are Docker images.
[Here's how Docker and OCI relate](https://www.docker.com/blog/demystifying-open-container-initiative-oci-specifications/).

> [!NOTE]  
> This repository is mostly a fork of the work done by @slorezt in https://github.com/sloretz/ros_oci_images
> adapted to Gazebo. All credit goes to Shane.

## Quick Start

New to containers? Start with [Docker](https://docs.docker.com/get-docker/). It has the most documentation and tutorials.

```
docker run --rm=true -ti ghcr.io/j-rivero/gazebo:jetty gz sim --help
```

## About the images

All images are updated once per week at midnight GMT on Sunday.
Additionally each Gazebo release's images are updated automatically after a sync.

The Gazebo releases provide different variants based on the included libraries.
All images are based on Ubuntu.

| Image           | amd64 | arm64 v8 | Full Image Name                                |
|-----------------|-------|----------|-----------------------------------------------|
| **[Gazebo Jetty (LTS)](https://gazebosim.org/docs/jetty)** | | | |
| core            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:jetty-core`           |
| full            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:jetty-full`           |
| **[Gazebo Ionic](https://gazebosim.org/docs/ionic)** | | | |
| core            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:ionic-core`           |
| full            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:ionic-full`           |
| **[Gazebo Harmonic (LTS)](https://gazebosim.org/docs/harmonic)** | | | |
| core            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:harmonic-core`        |
| full            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:harmonic-full`        |
| **[Gazebo Fortress (LTS)](https://gazebosim.org/docs/fortress)** | | | |
| core            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:fortress-core`        |
| full            | ✅     | ✅        | `ghcr.io/j-rivero/gazebo:fortress-full`        |

## Using with other OCI compatible tools

Used containers for a while?
Other tools might be better fit your use case.

[Apptainer](https://apptainer.org/)

```bash
apptainer run docker://ghcr.io/j-rivero/gazebo:jetty-full gz sim --help
```

[Distrobox](https://github.com/89luca89/distrobox) (Requires Docker or Podman to be installed)

```bash
distrobox create --image ghcr.io/j-rivero/gazebo:jetty-full --name jetty-full
distrobox enter jetty-full
gz sim --help
```

[nerdctl](https://github.com/containerd/nerdctl) using [rootless mode](https://github.com/containerd/nerdctl?tab=readme-ov-file#rootless-mode).

```bash
nerdctl run --rm=true -ti ghcr.io/j-rivero/gazebo:jetty-full gz sim --help
```

[Podman](https://podman.io/)

```bash
podman run --rm=true -ti ghcr.io/j-rivero/gazebo:jetty-full gz sim --help
```

[Rocker](https://github.com/osrf/rocker) (requires Docker to be installed)

```bash
rocker ghcr.io/j-rivero/gazebo:jetty-full gz sim -- --help
```

[Sarus](https://sarus.readthedocs.io/en/stable/#)

```bash
sarus pull ghcr.io/j-rivero/gazebo:jetty-full
sarus run -t ghcr.io/j-rivero/gazebo:jetty-full gz sim --help
```

[SingularityCE](https://sylabs.io/singularity/)

```bash
singularity run docker://ghcr.io/j-rivero/gazebo:jetty-full gz sim --help
```

[Toolbox](https://containertoolbx.org/) (Requires Podman to be installed)

```bash
toolbox create --image ghcr.io/j-rivero/gazebo:jetty-full jetty-full
toolbox enter jetty-full
gz sim --help
```

[x11docker](https://github.com/mviereck/x11docker) (Requires Podman, Docker, or nerdctl to be installed)

```bash
# Option 1: using podman
podman pull ghcr.io/j-rivero/gazebo:jetty-full
# Option 2: using docker
docker pull ghcr.io/j-rivero/gazebo:jetty-full
# Option 3: using nerdctl
nerdctl pull ghcr.io/j-rivero/gazebo:jetty-full

# After pulling, run this to use RViz with gpu acceleration
x11docker --gpu ghcr.io/j-rivero/gazebo:jetty-full gz sim
```

## Comparison to osrf/docker_images

This repo is a spiritual fork of [the official OSRF docker images](https://github.com/osrf/docker_images).
The image definitions here were copied and modified from them.
