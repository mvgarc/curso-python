# Registro completo de un estudiante
estudiante = {
 "nombre": "Ana Martínez",
 "edad": 21,
 "carrera": "Ingeniería Informática",
 "notas": [8.5, 9.2, 7.8, 9.0],
 "activo": True
}
# Acceder a los datos
print(f"Estudiante: {estudiante['nombre']}")
print(f"Promedio de notas: {sum(estudiante['notas']) / len(estudiante['notas']):.2f}")
# Modificar información
estudiante["edad"] = 22
estudiante["notas"].append(9.5)
# Añadir nueva información
estudiante["email"] = "ana.martinez@universidad.es"
print(f"Datos actualizados: {estudiante}")