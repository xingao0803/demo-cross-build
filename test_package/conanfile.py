import os

from conans import ConanFile, tools


class HelloTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "compiler_args"
    requires = "Hello/1.0@jfrog/stable"

    def build(self):
        if self.settings.arch == "x86_64":
            self.run("g++ ../../example.cpp @conanbuildinfo.args -o example")
        else :
            self.run("g++ ../../example.cpp -m32 @conanbuildinfo.args -o example")

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')
        self.copy('*.a', dst='bin', src='lib')

    def test(self)
        os.chdir("bin")
        self.run("..%sexample" % os.sep)
        self.run("file ..%sexample" % os.sep)
