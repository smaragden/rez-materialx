CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(materialx_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_materialx materialx/MaterialX-${materialx_version}.tar.gz
    https://github.com/materialx/MaterialX/archive/v${materialx_version}.tar.gz
)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    materialx
    URL ${url_materialx}
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} -DMATERIALX_BUILD_PYTHON=ON
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 0
)

rez_install_files(
    cmake/materialx.cmake
    DESTINATION .
)
