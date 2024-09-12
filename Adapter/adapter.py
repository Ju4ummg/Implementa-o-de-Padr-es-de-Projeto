class Target:
    def request(self):
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


# Uso do Adapter
def client_code(target: Target):
    print(target.request())


# O cliente trabalha com a interface Target.
print("Client: I can work just fine with the Target objects:")
target = Target()
client_code(target)

print("\nClient: The Adaptee has a weird interface. See, I don't understand it:")
adaptee = Adaptee()
print(f"Adaptee: {adaptee.specific_request()}")

print("\nClient: But I can work with it via the Adapter:")
adapter = Adapter(adaptee)
client_code(adapter)