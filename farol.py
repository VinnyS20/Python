import time


class farol:
    def __init__(self):
        self.state= "Vermelho"
    
    def trocar_verde(self):
        self.state = "Verde"
        print("Farol verde.Prossiga")
        time.sleep(5)
    
    def trocar_amarelo(self):
        self.state = "Amarelo"
        print("Farol amarelo.desacelere")
        time.sleep(2)

    def trocar_vermelho(self):
        self.state = "Vermelho"
        print("Farol vermelho.Pare")
        time.sleep(5)

    def run(self):
        while True:
            self.trocar_verde()
            self.trocar_amarelo()
            self.trocar_vermelho()

if __name__ == "__main__": 
    farol1 = farol()
    farol1.run()
            