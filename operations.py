import random, string

class Operation:

    def generator_unipw(data):
        hash(data)

    def generator_pw(self):
        chars = string.ascii_letters + string.digits
        charandom = random.choices(chars, k=23)
        return ''.join(charandom)
        #print("Clave generada", ''.join(charandom))


#if __name__ == "__main__":
#    app = Operation()
#    app.generator_pw()