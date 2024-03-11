cmake_minimum_required(VERSION 3.12)

project(cmakesample
     VERSION 0.1
     DESCRIPTION "CMake-base AuroraOS application"
     LANGUAGES CXX
)

find_package(Qt5 COMPONENTS Core Network Qml Gui Quick REQUIRED)

include(FindPkgConfig)
pkg_search_module(AURORA auroraapp REQUIRED)

set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(${PROJECT_NAME} main.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE
    $<BUILD_INTERFACE:${AURORA_INCLUDE_DIRS}>
)

target_compile_definitions(${PROJECT_NAME} PRIVATE
    $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>
)

target_link_libraries(${PROJECT_NAME}
    Qt5::Quick
    ${AURORA_LDFLAGS}
)

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION bin
)
install(DIRECTORY qml
    DESTINATION share/${PROJECT_NAME}
)
install(DIRECTORY translations
    DESTINATION share/${PROJECT_NAME}
    FILES_MATCHING PATTERN "*.qm"
)
install(FILES ${PROJECT_NAME}.desktop
    DESTINATION share/applications
)
foreach(_size 86x86 108x108 128x128 172x172)
     install(FILES icons/${_size}/${PROJECT_NAME}.png
          DESTINATION share/icons/hicolor/${_size}/apps
     )
endforeach()

# Tell Qt Creator where the application executable(s) would be located on the
# device.
#
# It is not necessary to list other deployables than executables (runtime
# targets) here. The deployment process of Sailfish OS projects is opaque to
# Qt Creator and the information contained in QtCreatorDeployment.txt is only
# used to locate the executable associated with the active run configuration
# on the device in order to run it.
#
# Search the Qt Creator Manual to learn about the QtCreatorDeployment.txt file
# format.
file(WRITE "${CMAKE_BINARY_DIR}/QtCreatorDeployment.txt"
    "${CMAKE_INSTALL_PREFIX}\n${CMAKE_BINARY_DIR}/${PROJECT_NAME}:bin\n")
