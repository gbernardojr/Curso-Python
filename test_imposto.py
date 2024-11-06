import pytest
from calculo_imposto import calcular_imposto

def test_calculo_imposto():
    # Teste com valores normais
    assert calcular_imposto(1000, 0.1) == 100
    assert calcular_imposto(2000, 0.15) == 300

def test_salario_negativo():
    # Teste para garantir que o erro é levantado com salário negativo
    with pytest.raises(ValueError):
        calcular_imposto(-1000, 0.1)

def test_aliquota_invalida():
    # Teste para garantir que o erro é levantado com alíquota fora dos limites
    with pytest.raises(ValueError):
        calcular_imposto(1000, -0.1)
    with pytest.raises(ValueError):
        calcular_imposto(1000, 1.5)

def test_aliquota_zero():
    # Testando caso de alíquota zero
    assert calcular_imposto(1000, 0) == 0
