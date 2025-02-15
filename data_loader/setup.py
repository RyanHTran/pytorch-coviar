from distutils.core import setup, Extension
import numpy as np

coviar_h264 = Extension('coviar_h264',
		sources = ['coviar_data_loader_h264.c'],
		include_dirs=[np.get_include(), './ffmpeg/include/'],
		extra_compile_args=['-DNDEBUG', '-O3'],
		extra_link_args=['-lavutil', '-lavcodec', '-lavformat', '-lswscale', '-L./ffmpeg/lib/']
)

coviar = Extension('coviar',
		sources = ['coviar_data_loader.c'],
		include_dirs=[np.get_include(), './ffmpeg/include/'],
		extra_compile_args=['-DNDEBUG', '-O3'],
		extra_link_args=['-lavutil', '-lavcodec', '-lavformat', '-lswscale', '-L./ffmpeg/lib/']
)

setup ( name = 'coviar_utils',
	version = '0.1',
	description = 'Utils for coviar training.',
	ext_modules = [ coviar, coviar_h264 ]
)
