Pattern Matching
================

Uma instrução `match` pega uma expressão e a compara a sucessivas
padrões dados como um ou mais blocos `case`. Isso é superficialmente
semelhante a uma instrução `switch` em C, Java ou JavaScript (e muitos
outras línguas), mas muito mais poderoso.

A forma mais simples de Match Case compara um valor de assunto com um ou mais literais:

```py
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something else"
```

Observe o último bloco: o "nome da variável" `_` atua como um *curinga* e
sempre executa quando não for nenhum dos casos.

--------

Você pode combinar vários literais em um único padrão usando `|` ("ou"):

```py
        case 401|403|404:
            return "Not allowed"
```

--------

O que é passado para o case pode ser atribuições de descompactação e podem ser usados para vincular
variáveis:

```py
# The subject is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

Estude isso com atenção! O primeiro padrão tem dois literais e pode
ser pensado como uma extensão do padrão literal mostrado acima. Mas
os próximos dois padrões combinam um literal e uma variável, e o
variável *captura* um valor do assunto (`x` ou `y`). O quarto
padrão captura dois valores, o que o torna conceitualmente semelhante a
a atribuição de descompactação.

--------

Se você estiver usando classes para estruturar seus dados você pode usar o nome da classe seguido por uma lista de argumentos semelhante a um
construtor, mas com a capacidade de capturar variáveis

```py
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def whereis(point):
    match point:
        case Point(0, 0):
            print("Origin")
        case Point(0, y):
            print(f"Y={y}")
        case Point(x, 0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

--------

Podemos adicionar uma cláusula `if` a um padrão, conhecido como "guard". Se o
guard for false, `match` continua para tentar o próximo bloco `case`. Observação
que a captura de valor acontece antes que a guarda seja avaliada:

```py
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

--------

Os padrões podem usar constantes nomeadas. Estes devem ser nomes pontilhados para evitar que sejam interpretados como variável de captura:

  ```py
  from enum import Enum
  class Color(Enum):
      RED = 0
      GREEN = 1
      BLUE = 2

  match color:
      case Color.RED:
          print("I see red!")
      case Color.GREEN:
          print("Grass is green")
      case Color.BLUE:
          print("I'm feeling the blues :(")
  ```
  
  --------
  
- Os literais `None`, `False` e `True` são tratados de forma especial:
  comparações com o assunto são feitas usando `is`.
  
  ```py
  match b:
      case True:
          print("Yes!")
  ```
  is exactly equivalent to this:
  ```py
  if b is True:
      print("Yes!")
  ```

--------

- As classes podem substituir o mapeamento de argumentos posicionais para
  atributos definindo uma variável de classe `__match_args__`.
  
  [PEP](https://www.python.org/dev/peps/pep-0622/#special-attribute-match-args).
