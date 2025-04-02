### Què són els tests unitaris?

Els **tests unitaris** serveixen per verificar les unitats individuals de codi en el desenvolupament de programari, com ara funcions, mètodes o classes, de manera aïllada per assegurar-se que funcionen correctament. Una "unitat" és la peça més petita de codi que es pot provar de manera independent.

#### Objectius dels tests unitaris:

- **Detectar errors aviat**: Identifiquen problemes en el codi abans que es converteixin en errors més grans.
- **Facilitar el manteniment**: Quan es fan canvis al codi, els tests unitaris ajuden a assegurar que les funcionalitats existents no es trenquin.
- **Documentació viva**: Els tests poden servir com a documentació per entendre com hauria de funcionar una funció o mètode.
- **Millorar la confiança**: Proporcionen confiança que el codi funciona com s'espera.

#### Exemple d'un test unitari en Python amb `unittest`:

```python
import unittest
from calculadora import suma

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        resultat = suma(2, 3)
        self.assertEqual(resultat, 5)

if __name__ == '__main__':
    unittest.main()
```

#### Característiques clau:

- **Aïllament**: Cada test unitari prova una sola funcionalitat.
- **Automatització**: Es poden executar automàticament amb eines com `unittest`, `pytest` (Python), `JUnit` (Java), etc.
- **Repetibilitat**: Els tests es poden executar tantes vegades com sigui necessari.
### Com funciona la biblioteca `unittest` de Python?

La biblioteca `unittest` és una de les eines integrades a Python per escriure i executar tests unitaris. Proporciona una estructura basada en classes per definir i organitzar els tests.

#### Passos bàsics per utilitzar `unittest`:

1. **Importar la biblioteca**: Importa el mòdul `unittest`.
2. **Crear una classe de test**: Defineix una classe que hereti de `unittest.TestCase`.
3. **Escriure mètodes de test**: Cada mètode que comença amb `test_` es considera un test.
4. **Utilitzar assertions**: Fes servir mètodes com `assertEqual`, `assertTrue`, etc., per verificar els resultats esperats.
5. **Executar els tests**: Utilitza `unittest.main()` per executar els tests.

#### Exemple senzill:

```python
import unittest

# Funció a provar
def multiplica(a, b):
    return a * b

# Classe de test
class TestMultiplica(unittest.TestCase):
    def test_multiplica_positius(self):
        self.assertEqual(multiplica(2, 3), 6)

    def test_multiplica_negatius(self):
        self.assertEqual(multiplica(-2, -3), 6)

    def test_multiplica_zero(self):
        self.assertEqual(multiplica(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
```

#### Mètodes comuns d'assertions:

- `assertEqual(a, b)`: Verifica que `a == b`.
- `assertNotEqual(a, b)`: Verifica que `a != b`.
- `assertTrue(x)`: Verifica que `x` és cert.
- `assertFalse(x)`: Verifica que `x` és fals.
- `assertRaises(exception, callable, *args, **kwargs)`: Verifica que es llança una excepció.

#### Avantatges de `unittest`:
- És una biblioteca estàndard, no cal instal·lar res addicional.
- Suporta configuració i neteja amb els mètodes `setUp` i `tearDown`.
- Compatible amb altres eines i frameworks de testing.

Amb aquests conceptes, pots començar a escriure tests unitaris robustos per al teu codi en Python.