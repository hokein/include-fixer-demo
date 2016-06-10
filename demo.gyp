{
  'targets': [
    {
      'target_name': 'include-fixer-demo',
      'type': 'executable',
      'sources': [
        'include/stl.h',
        'include/demo.h',
        'src/main.cpp',
      ],
      'include_dirs': [
        'include'
      ],
    },
  ],
}
