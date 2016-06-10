#Include-fixer-Demo

The demo repository demonstrates core features of [#clang-include-fixer][1], a tool
that automatically adds missing headers for unidentified symbols in cpp files.

![screenshot](/screenshot/include-fixer.gif)

Enjoy the tool. :heavy_plus_sign::hash:

## Setup Include-Fixer

Currently, there is no prebuilt binary provided. You have to check out clang
project and build the tool for yourself.

```
// check out llvm repository
git clone http://llvm.org/git/llvm.git llvm
cd llvm
// check out clang repository
git clone http://llvm.org/git/clang.git clang
cd clang
// check out extral clang tools for include-fixer
git clone http://llvm.org/git/clang-tools-extra.git extra
cd ../
mkdir build
cd build
cmake -G Ninja ../
ninja clang-include-fixer
ninja find-all-symbols
```

The [upstream document][1] is a good reference material.

## Projects using Cmake

```
cd path/to/include-fixer-demo
mkdir build
cmake -G Ninja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ../
/path/to/run-find-all-symbols.py -b path/to/find-all-symbols
cd build
ln -sf $PWD/compile_commands.json ../
ln -sf $PWD/find_all_symbols.yaml ../
```

## Projects using gyp

```
cd path/to/include-fixer-demo
gyp demo.gyp -f ninja --depth=.
// Generates compilation json database.
ninja -C out/Default -t compdb cc cxx objc objcxx > compile_commands.json
/path/to/run-find-all-symbols.py -b path/to/find-all-symbols
```

## Other projects

For other non-cmake and non-gyp projects, there is a tool called [Bear](https://github.com/rizsotto/Bear)
to generate JSON compilation database (`compile_commands.json`).

[1]: http://clang.llvm.org/extra/include-fixer.html
