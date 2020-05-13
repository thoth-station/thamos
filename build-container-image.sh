#!/bin/bash -xe
# Thamos
# Copyright(C) 2019 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# if we are not running as root, let's do it!
[ -z "$SUDO_COMMAND" ] && exec sudo $0

if ! type buildah; then
    dnf install -y --setopt=tsflags=nodocs buildah
fi

# update the local copy...
buildah pull "docker://registry.fedoraproject.org/fedora:30"

ctr=$(buildah from "registry.fedoraproject.org/fedora:30")
mnt=$(buildah mount $ctr)

buildah run $ctr -- pip3 install thamos

# Cleanup
buildah run $ctr -- dnf update -y --setopt=tsflags=nodocs
buildah run $ctr -- dnf clean all
buildah run $ctr -- rm -Rf /root/.cache
rm -rf $mnt/usr/share/man $mnt/usr/share/info

# Setup user environment
buildah run $ctr -- useradd -m user
mkdir -p $mnt/opt/redhat/thoth/thamos/workdir
buildah run $ctr -- chown user:user -R /opt/redhat/thoth/thamos

## Include some buildtime annotations
buildah config --annotation "ninja.thoth-station.build.host=$(uname -n)" $ctr
buildah config --author goern+thoth@redhat.com $ctr
buildah config --cmd "/bin/bash" $ctr
buildah config --workingdir /opt/redhat/thoth/thamos/workdir $ctr
buildah config --user user $ctr

## Commit this container to an image name
buildah umount $ctr
cid=`buildah commit $ctr thoth-ops`
buildah tag $cid localhost/thamos:latest
buildah rm $ctr
