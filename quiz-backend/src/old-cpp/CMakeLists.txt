# Path definitions.
set(src_dir ${CMAKE_CURRENT_SOURCE_DIR})

# Specify Clang-Tidy linter.
set(CMAKE_CXX_CLANG_TIDY 
    "clang-tidy"
    "-checks=-*,bugprone-*,cppcoreguidelines-*,-llvm*"
    "-header-filter=/.*"  # Only include project headers
)

# Add overall src library.
file(GLOB_RECURSE src_sources CONFIGURE_DEPENDS ${src_dir}/*.cpp)
add_library(src ${src_sources})
target_include_directories(src PUBLIC ${src_dir})
target_link_libraries(src PRIVATE)
