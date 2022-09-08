d = {'s' : 1} # Dicionário

match d:
    case{'f': _} | {'d' :_}: # Executa quando temos a chave f ou d
        print('Contém F ou D')
    case {'a' : _, 'b' : _}: # Executa quando temos as chaves a e b
        print('Contém A e B')
    case {'a' : _}: # Executa quando temos a chave a
        print('contém A')
    case {'s' : _, **kwargs}: # Executa quando temos a chave s
        print(kwargs)