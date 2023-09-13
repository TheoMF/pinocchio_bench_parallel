#!/usr/bin/env sh

sudo apt install assimp-utils robotpkg-example-robot-data robotpkg-hpp-fcl+doc robotpkg-py38-eigenpy robotpkg-py38-hpp-fcl libgomp1
cd ..
git clone --recursive git@gitlab.inria.fr:jucarpen/pinocchio.git
cd pinocchio && mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=<to determine> -DBUILD_WITH_COLLISION_SUPPORT=ON -DBUILD_BENCHMARK=ON -DBUILD_WITH_OPENMP_SUPPORT=ON -DOpenMP_CXX_LIBRARY=/usr/lib/gcc/x86_64-linux-gnu/9/libgomp.so -DOpenMP_CXX_INCLUDE_DIR=/usr/lib/gcc/x86_64-linux-gnu/9/include
make -j4
make install
