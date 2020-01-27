import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class libav(mama.BuildTarget):

    workspace = 'build'

    def dependencies(self):
        pass

    def configure(self):
        self.nothing_to_build()

    def package(self):
        if self.config.is_target_arch_x86():
            self.export_include('x86/include')
            self.export_libs('x86/bin', ['.lib','.dll'], src_dir=True)
        elif self.config.is_target_arch_x64():
            self.export_include('x64/include')
            self.export_libs('x64/bin', ['.lib','.dll'], src_dir=True)
        else:
            self.export_syslib('avcodec', 'libav-tools')
            self.export_syslib('avformat', 'libav-tools')
            self.export_syslib('avutil', 'libav-tools')


