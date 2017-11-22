from conans import ConanFile, CMake, tools

class BuildConan(ConanFile):
	name = "Hypodermic"
	version = "2.4"

	license = "MIT"
	description = "Hypodermic is an IoC container for C++. It provides dependency injection to your existing design."
	url = "https://github.com/ybainier/Hypodermic"

	exports_sources = "*"
	requires = (
		"Boost/1.64.0@conan/stable"
	)

	def package_id(self):
		self.info.header_only()

	def configure(self):
		self.options["Boost"].header_only = True

	def source(self):
		self.run("git clone https://github.com/ybainier/Hypodermic")
		self.run("cd Hypodermic && git checkout v2.4")

	def package(self):
		self.copy("*.h", dst="include/Hypodermic", src="Hypodermic/Hypodermic")
