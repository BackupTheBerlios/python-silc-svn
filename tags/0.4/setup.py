from distutils.core import setup, Extension
from os.path import isfile

try:
    if isfile("MANIFEST"):
        os.unlink("MANIFEST")
except:
    pass

ext_modules = [
    Extension('silc', ['src/pysilc.c'],
              libraries = ['silc', 'silcclient'],
              extra_compile_args = ['-g'],
              include_dirs = ['/usr/include/silc-toolkit',
                              '/usr/local/include/silc'],
              depends = ['src/pysilc_callbacks.c',
                         'src/pysilc_channel.c',
                         'src/pysilc_user.c',
                         'src/pysilc_macros.h',
                         'src/pysilc.h']),
]

setup(name = 'silc',
      version = '0.4',
      description = 'Python Binding for SILC Toolkit',
      author = 'Alastair Tse',
      author_email = 'alastair@tse.id.au',
      url = 'http://www.liquidx.net/pysilc/',
      license = 'BSD',
      ext_package = '',
      ext_modules = ext_modules
)

    
