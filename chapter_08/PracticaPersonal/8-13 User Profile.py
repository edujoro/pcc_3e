def build_profile(nombre, apellido, **otrosDatos):
    otrosDatos.update({'nombre':nombre})
    otrosDatos.update({'apellido':apellido})
    return otrosDatos

print(build_profile('eduardo','cabrera',edad = 36, estado_civil = 'soltero'))