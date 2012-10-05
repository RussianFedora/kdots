#!/bin/bash

ORIGNAME=kdots
VERSION=0.5.1
GIT_REVISION=b93c4e19a1
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://github.com/Ignotus/kdots.git &>/dev/null
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}
