from calculo_imposto import calcular_imposto

def main():
    try:
        # Recebe o salário e a alíquota do usuário
        salario = float(input("Digite o salário: "))
        aliquota = float(input("Digite a alíquota (por exemplo, 0.1 para 10%): "))
        
        # Calcula o imposto
        imposto = calcular_imposto(salario, aliquota)
        
        # Exibe o resultado
        print(f"O imposto sobre o salário de R${salario} com uma alíquota de {aliquota*100}% é R${imposto:.2f}.")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

