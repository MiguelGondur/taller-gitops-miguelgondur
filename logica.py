def calcular_estadisticas_notas(notas):
    """
    Calcula estadísticas básicas sobre una lista de calificaciones numéricas.

    Args:
        notas: lista de números (int o float), por ejemplo [3.5, 4.0, 2.0, 5.0, 1.5].

    Returns:
        dict con las claves: total, promedio, aprobados, reprobados,
        nota_maxima y nota_minima.

        - Lista vacía: todos los valores en cero.
        - Con notas: total (cantidad), promedio (redondeado a 2 decimales),
          aprobados (nota >= 3.0), reprobados (nota < 3.0), nota_maxima y
          nota_minima.
    """
    if not notas:
        return {
            "total": 0,
            "promedio": 0.0,
            "aprobados": 0,
            "reprobados": 0,
            "nota_maxima": 0.0,
            "nota_minima": 0.0,
        }

    total = 0
    suma = 0
    aprobados = 0
    reprobados = 0
    nota_maxima = notas[0]
    nota_minima = notas[0]

    for nota in notas:
        total += 1
        suma += nota

        if nota >= 3.0:
            aprobados += 1
        else:
            reprobados += 1

        if nota > nota_maxima:
            nota_maxima = nota
        if nota < nota_minima:
            nota_minima = nota

    return {
        "total": total,
        "promedio": round(suma / total, 2),
        "aprobados": aprobados,
        "reprobados": reprobados,
        "nota_maxima": nota_maxima,
        "nota_minima": nota_minima,
    }
