from conans import ConanFile

class HelloConan(ConanFile):
    name = "Hello"
    version = "1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Timer here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "compiler_args"

    def source(self):
        self.run("git clone https://github.com/xingao0803/demo-cross-build.git")

    def build(self):
        self.run("g++ -c demo-cross-build/src/* @conanbuildinfo.args")
        self.run("ar cr libhello.a hello.o")

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
