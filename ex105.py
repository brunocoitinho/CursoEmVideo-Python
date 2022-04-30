def notas(*nota, sit=False):
    """
    ->Função para analizar as notas e as situação de um aluno
    :param nota: uma ou mais notas de um aluno
    :param sit: (opcional) adciona a situação do aluno no retorno
    :return: dicionario com informações sobre a situação do aluno
    """
    aluno = dict()
    aluno['notas'] = nota
    soma = 0
    aluno['maior'] = nota[0]
    aluno['menor'] = nota[0]

    for c in range(0, len(nota)):
        soma += nota[c]
        if nota[c] > aluno['maior']:
            aluno['maior'] = nota[c]
        if nota[c] < aluno['menor']:
            aluno['menor'] = nota[c]

    aluno['media'] = soma / len(nota)

    if sit:
        if aluno['media'] >= 8:
            aluno['situacao'] = 'BOA'
        elif aluno['media'] >= 6:
            aluno['situacao'] = 'RAZOAVEL'
        else:
            aluno['situacao'] = 'RUIM'

    return aluno


print(notas(9.3, 9, 6, sit=True))
