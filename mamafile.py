import mama

##
# Explore Mama docs at https://github.com/RedFox20/Mama
#
class libav(mama.BuildTarget):

    workspace = 'build'

    def dependencies(self):
        pass

    def configure(self):
        pass

    def package(self):
        if self.config.is_target_arch_x86():
            self.export_include('x86/include')
            self.export_lib('x86/lib/libavcodec.a', src_dir=True)
            self.export_lib('x86/lib/libavformat.a', src_dir=True)
            self.export_lib('x86/lib/libavutil.a', src_dir=True)
        elif self.config.is_target_arch_x64():
            self.export_include('x64/include')
            self.export_lib('x64/lib/libavcodec.a', src_dir=True)
            self.export_lib('x64/lib/libavformat.a', src_dir=True)
            self.export_lib('x64/lib/libavutil.a', src_dir=True)
        else:
            self.export_syslib('avcodec', 'libav-tools')
            self.export_syslib('avformat', 'libav-tools')
            self.export_syslib('avutil', 'libav-tools')


