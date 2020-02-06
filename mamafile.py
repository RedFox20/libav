import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class libav(mama.BuildTarget):

    workspace = 'build'

    def dependencies(self):
        self.nothing_to_build()

    def configure(self):
        pass

    def package(self):
        if self.windows:
          if self.config.is_target_arch_x86():
              self.export_include('x86/include')
              self.export_libs('x86/bin', ['.lib','.dll'], src_dir=True)
          elif self.config.is_target_arch_x64():
              self.export_include('x64/include')
              self.export_libs('x64/bin', ['.lib','.dll'], src_dir=True)
        elif self.linux:
            self.export_syslib('libavcodec', 'ffmpeg')
            self.export_syslib('libavformat', 'ffmpeg')
            self.export_syslib('libavutil', 'ffmpeg')


