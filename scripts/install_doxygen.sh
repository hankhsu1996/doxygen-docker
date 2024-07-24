#!/bin/sh
VERSION=$1
wget https://www.doxygen.nl/files/doxygen-${VERSION}.linux.bin.tar.gz
tar -xzf doxygen-${VERSION}.linux.bin.tar.gz
mv doxygen-${VERSION}/bin/* /usr/local/bin/
rm -rf doxygen-${VERSION}*
