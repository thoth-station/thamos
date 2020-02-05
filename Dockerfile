FROM registry.fedoraproject.org/fedora:30
LABEL maintainer=thoth@redhat.com

RUN dnf update -y --setopt=tsflags=nodocs && \
    dnf clean all && \
    rm -Rf /root/.cache && \
    rm -rf /usr/share/man /usr/share/info && \
    useradd -m user && \
    mkdir -p /opt/redhat/thoth/thamos/workdir && \
    chown user:user -R /opt/redhat/thoth/thamos

COPY ./ /tmp/thamos-install 
RUN pushd /tmp/thamos-install && python3 setup.py install && rm -rf /tmp/thamos-install

CMD ["/bin/bash"]
WORKDIR /opt/redhat/thoth/thamos/workdir
USER user
