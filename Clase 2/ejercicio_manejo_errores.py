def division_segura():
    print("--- Calculadora de División Segura ---")
    
    # Intentamos ejecutar el código que podría fallar
    try:
        # 1. Pedir entradas
        num1_str = input("Ingresa el numerador (número de arriba): ")
        num2_str = input("Ingresa el denominador (número de abajo): ")

        # 2. Conversión a número (puede causar ValueError si ingresan texto)
        num1 = float(num1_str)
        num2 = float(num2_str)

        # 3. Operación (puede causar ZeroDivisionError si num2 es 0)
        resultado = num1 / num2
        
    # Si ocurre un error, Python busca el 'except' que coincida
    
    except ZeroDivisionError:
        # 4. Maneja el error específico de división por cero
        print("\n¡Error Matemático! No se puede dividir por cero.")
        
    except ValueError:
        # 5. Maneja el error específico de tipo de datos (ej. ingresar 'hola')
        print("\n¡Error de Datos! Solo se aceptan números. Por favor, revisa la entrada.")
        
    except Exception as e:
        # 6. Maneja cualquier otro error inesperado
        print(f"\n¡Ocurrió un error inesperado! Tipo de error: {type(e).__name__}")
        
    else:
        # 7. Si NO hubo NINGÚN error en el bloque 'try'
        print("\n--- Resultado Exitoso ---")
        print(f"{num1} dividido por {num2} es igual a {resultado}")
        
    finally:
        # 8. Se ejecuta SIEMPRE, haya habido error o no
        print("\nPrograma terminado. Gracias por usar la calculadora.")

division_segura()