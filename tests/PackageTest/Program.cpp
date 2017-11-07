#include <Hypodermic/Hypodermic.h>
#include <iostream>

class Messenger
{
public:
	virtual void TellMeSomething() = 0;
};

class MessengerImpl : public Messenger
{
public:
	void TellMeSomething()
	{
		std::cout << "Hello, Hypodermic!" << std::endl;
	}
};

int main(int argc, char* argv[])
{
	// Arrange
	Hypodermic::ContainerBuilder builder;
	builder.registerType<MessengerImpl>().as<Messenger>();
	auto container = builder.build();

	// Act
	auto inst = container->resolve<Messenger>();
	inst->TellMeSomething();

	// Assert (implicit failure)
	return EXIT_SUCCESS;
}
