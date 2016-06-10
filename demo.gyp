{
  'targets': [
    {
      'target_name': 'include-fixer-demo',
      'type': 'executable',
      'sources': [
        'include/bar.h',
        'include/foo.h',
        'include/stl.h',
        'src/main.cpp',
      ],
      'include_dirs': [
        'include'
      ],
    },
  ],
}
