from project import es_numero_valido, comparar_respuesta, resultado_a_texto

def test_es_numero_valido():
    assert es_numero_valido("1")
    assert es_numero_valido("10")
    assert not es_numero_valido("0")
    assert not es_numero_valido("11")
    assert not es_numero_valido("abc")
    assert not es_numero_valido("")

def test_comparar_respuesta():
    assert comparar_respuesta("peine", "es un peine")
    assert comparar_respuesta("nube", "una NUBE blanca")
    assert comparar_respuesta("esponja", "Creo que es una esponja")
    assert not comparar_respuesta("peine", "cepillo")
    assert not comparar_respuesta("nube", "lluvia")
    assert not comparar_respuesta("esponja", "jabón")

def test_resultado_a_texto():
    assert resultado_a_texto(True) == "correcto"
    assert resultado_a_texto(False) == "incorrecto"
