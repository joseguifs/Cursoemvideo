from datetime import datetime


def validar_nome(name):
    try:
        namej = ''.join(name.split().strip())
        caracter = [char for char in namej if not char.isalpha()]
        if not any(caracter):
            print("NOME VÁLIDO")
            return True
        else:
            print("NOME INVÁLIDO")
            return False
    except ValueError:
        print("PARÂMETRO PARA A FUNÇÃO INVÁLIDO")


def valida_nascimento(age):
    if datetime.today().year - age < 18:
        print("VOCÊ É MENOR DE IDADE")
        return False
    elif datetime.today().year - age == 18:
        mes = int(input("Digite seu mês de nascimento: "))
        if mes < datetime.today().month:
            print("DATA DE NASCIMENTO VÁLIDA")
            return True
        elif mes == datetime.today().month:
            day = int(input("Digite seu dia de nascimento: "))
            if day <= datetime.today().day:
                print("DATA DE NASCIMENTO VÁLIDA")
                return True
            else:
                print("DATA DE NASCIMENTO INVÁLIDA")
                return False
        else:
            print("DATA DE NASCIEMTNO INVÁLIDA")
            return False
    else:
        print("DATA DE NASCIMENTO VÁLIDA")
        return True


class Banco:
    taxa_juros = 0.1
    contas = list()
    list_investimentos = list()

    def __init__(self, nome, idade):
        self._idade = idade
        self._nome = nome
        self.valido = False
        self._saldo = 0
        Banco.contas.append(
            self)  # Adiciona automaticamente a conta ao criar uma instância, você está adicionando a instância atual da classe à lista de

    # contas Ao adicionar a instância (que representa uma conta) à lista Banco.contas, você está basicamente armazenando um "objeto de conta" nessa lista.
    # adicionando o objeto atual da classe ou a instancial atual da classe (que é o objeto atual) a lista contas

    @classmethod
    def depositar(cls, valor, conta):
        try:
            valor = Banco.validar_valor(valor)
            if valor < 0:
                raise ValueError("NÃO É POSSÍVEL DEPOSITAR VALORES NEGATIVOS")
            if conta not in Banco.contas:
                print("CONTA NÃO ENCOTRADA NO BANCO")
            conta.saldo += valor
            print(f'''VALOR DEPOSITADO PARA {conta.nome}: {valor}
SEU NOVO SALDO É DE {conta.saldo}''')
        except ValueError as e:
            print(f"VALOR NÃO VÁLIDO: {e}")

    @classmethod
    def adicionar_conta(cls, conta):
        cls.contas.append(conta)  # Adiciona a instância da conta
        conta.valido = True

    @classmethod
    def validar(cls, conta):
        if conta not in cls.contas:
            print("CONTA ÍNVALIDA")
        else:
            print("CONTA VÁLIDA")

    @classmethod
    def nova_taxa(cls, nova_taxa):
        cls.taxa_juros = nova_taxa

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_name):
        self.nome = new_name.split()

        try:
            caracters_invalidos = [char for char in ''.join(self.nome) if not char.isalpha()]
            if not any(caracters_invalidos):
                self._nome = new_name
                print(f"seu novo nome é : {self.nome}")
            else:
                raise NameError
        except NameError as e:
            print("NOME INVÁLIDO")

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, new_value):
        try:
            new_value = float(new_value)
            if new_value < 0:
                print("NÃO TEM COMO ADICIONAR VALORES NEGATIVOS A SUA CONTA")
                raise ValueError  # chama o execpt

        except ValueError:
            print("VALOR ÍNVALIDO")
        else:
            self._saldo += new_value
            print(f'''VALOR  ADICIONADO A CONTA DE {self.nome.upper()}: {new_value}
SALDO DE É DE(A) {self._nome.upper()}: {self._saldo}''')

    def sacar(self, value):
        try:
            value = Banco.validar_valor(value)  # Tenta converter o valor para float
            if value < 0:
                raise ValueError("NÃO É POSSÍVEL SACAR VALORES NEGATIVOS")
            if value > self._saldo:
                raise ValueError("ESSE VALOR É MAIOR QUE O SALDO DISPONÍVEL")

            self._saldo -= value  # Realiza o saque
            print(f'''Você sacou {value}
Seu novo saldo é: {self._saldo}''')

        except ValueError as e:
            # se houver uma exceção as parte "as e" armazena essa exceção levantada pelo raise na variavel e
            print(f"VALOR INVÁLIDO: {e}")  # Mensagem de erro detalhada

    def investimento(self, valor, tempo=30):
        try:
            valor = Banco.validar_valor(valor)
            tempo = Banco.validar_valor(tempo)
            if valor < 0:
                raise ValueError("NÃO É POSSIVEL INVESTIR VALOR NEGATIVO")
            if valor > self._saldo:
                raise ValueError("VALOR DE INVESTIMENTO É MAIOR QUE O SALDO DISPONIVEL")
            if tempo < 30:
                raise ValueError("TEMPO DE INVESTIMENTO NÃO PODE SER MENOS QUE 30 DIAS")

        except ValueError as e:
            print(f"VALOR NÃO VÁLIDO: {e}")
        else:
            self._saldo -= valor
            investimentos = {
                'nome': self._nome,
                'valor_investido': valor,
                'tempo_investido': tempo,
                'valor_previsto': valor * Banco.taxa_juros * tempo
            }
            self.list_investimentos.append(investimentos)

    def transeferencia(self, remetente, valor, destinatario):
        """

        :param remetente: A conta que está fazendo a transferência.
        :param valor: O valor a ser transferido
        :param destinatario:  A conta que receberá o valor.

        Raises:
            ValueError: Se o valor for negativo ou maior que o saldo disponível.
        """

        if not destinatario.valido:
            print('ESSA PESSOA NÃO ESTA LISTADA NO NOSSO BANCO DE DADOS')
        else:
            try:
                valor = Banco.validar_valor(valor)
                if valor < 0:
                    raise ValueError("NÃO É POSSIVEL TRASNFERIR VALORES NEGATIVO")
                if valor > self._saldo:
                    raise ValueError("VALOR MAIOR QUE O SALDO DISPONIVEL")
                self._saldo -= valor
                print("REALIZANDO TRASNFERÊNCIA...")
                print(f"TRANSFERÊNCIA DE {valor} REALIZADA COM SUCESSO PARA {destinatario.nome.upper()}")
                destinatario.saldo += valor
                print(f"SALDO ATUAL DE {destinatario.nome.upper()} É DE {destinatario.saldo}")
                print(f"SALDO ATUAL DE {remetente.nome.upper()} É DE: {remetente.saldo}")
            except ValueError as e:
                print(f"VALOR NÃO VÁLIDO: {e}")

    @staticmethod
    def validar_valor(valor):
        try:
            valor = float(valor)
            return valor
        except ValueError:
            raise ValueError("DIGITE UM VALOR VÁLIDO")
        except Exception as e:
            print(f"{e}")


contas_banco = list()
while True:
    name = str(input("Nome do usúario da conta: "))
    age = int(input("Digite seu ano de nascimento: "))
    if valida_nascimento(age) and validar_nome(name):
        print("CONTA CRIADA COM SUCESSO")
        contas_banco.append(Banco(name, age))
    else:
        print("TENTE NOVAMENTE!")
        continue
    while True:
            continuar = str(input("Quer continuar criando contas: [S/N] ")).strip().upper()
            if continuar != 'S' and continuar != 'N':
                print("RESPOSTA INVÁLIDA")
                continue
            if continuar == 'S':
                break
            if continuar.upper() == 'N':
                break
    if continuar == 'S':
        continue
    else:
        print("Saindo...")
        break

print(contas_banco[0].nome)