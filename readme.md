#Include-fixer-Demo

The demo repository demonstrates core features of #clang-include-fixer, a tool
that automatically adds missing headers for unidentified symbols in cpp files.

Enjoy the tool.

## Setup Include-Fixer

Follow the [upstream document](http://clang.llvm.org/extra/include-fixer.html).

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
