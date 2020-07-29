def normalize_path_params(cidade=None, avaliacao_min = 0, avaliacao_max = 5, diaria_min = 0, diaria_max = 10000, limit = 50, offset = 0, **dados):
    if cidade:
        return {'avaliacao_min' : avaliacao_min, 'avaliacao_max' : avaliacao_max, 'diaria_min' : diaria_min, 'diaria_max' : diaria_max, 'cidade' : cidade, 'limit' : limit, 'offset' : offset}
    return{'avaliacao_min' : avaliacao_min, 'avaliacao_max' : avaliacao_max, 'diaria_min' : diaria_min, 'diaria_max' : diaria_max, 'limit' : limit, 'offset' : offset}


consulta_sem_cidade = "SELECT * FROM hoteis WHERE (avaliacao >= ? and avaliacao <= ?) and (diaria >= ? and diaria <= ?) LIMIT ? OFFSET ?"
consulta_com_cidade = "SELECT * FROM hoteis WHERE (avaliacao >= ? and avaliacao <= ?) and (diaria >= ? and diaria <= ?) and cidade = ? LIMIT ? OFFSET ?"