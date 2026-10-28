
from pathlib import Path
from ollama import Client, ResponseError
import httpx


# 1. Leer el archivo de contexto
def leer_contexto(ruta_archivo):
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return archivo.read()

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        return ""

    except UnicodeError:
        print("Error: No se pudo leer el archivo con codificación UTF-8.")
        return ""

    except OSError as error:
        print(f"Error al abrir el archivo: {error}")
        return ""


# 2. Consultar el modelo local mediante Ollama
def consultar_ollama(system_prompt, user_prompt, contexto, modelo, temperatura):

    mensajes = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": (
                f"{user_prompt}\n\n"
                f"CONTEXTO PROPORCIONADO:\n{contexto}"
            ) if contexto else user_prompt
        }
    ]

    client = Client(host="http://localhost:11434")

    respuesta = client.chat(
        model=modelo,
        messages=mensajes,
        options={
            "temperature": temperatura,
            "num_ctx": 8192
        }
    )

    return respuesta.message.content


# 3. Menú principal
def main():

    config = {
        "modelo": "ibm/granite3.3:2b-instruct-q4_K_M",
        "temperatura": 0.2,
        "system_prompt": (
            "Eres un asistente especializado en programación e "
            "inteligencia artificial. Responde en español de forma "
            "clara, precisa y estructurada. Si se proporciona un "
            "documento, utilízalo como fuente de información. "
            "No inventes información que no esté en el documento "
            "cuando la pregunta dependa de su contenido."
        ),
        "user_prompt": "Identifica las aplicaciones prácticas del programa.",
        "contexto": ""
    }

    while True:

        print("\n--- MENÚ ASISTENTE LOCAL ---")
        print("1. Cargar archivo de contexto")
        print("2. Enviar consulta al LLM")
        print("3. Modificar configuración")
        print("4. Ver configuración actual")
        print("0. Salir")

        opcion = input("\nSelecciona una opción: ").strip()

        match opcion:

            case "1":
                ruta = input("Ruta del archivo .txt: ").strip().strip('"')

                contexto = leer_contexto(ruta)

                if contexto.strip():
                    config["contexto"] = contexto
                    print("Archivo cargado correctamente.")
                    print(f"Caracteres cargados: {len(contexto)}")
                else:
                    print("No se ha cargado contenido nuevo.")

            case "2":
                pregunta = input(
                    "\nEscribe tu consulta (Enter para usar la predeterminada): "
                ).strip()

                if pregunta:
                    config["user_prompt"] = pregunta

                print("\nProcesando consulta...")

                try:
                    resultado = consultar_ollama(
                        config["system_prompt"],
                        config["user_prompt"],
                        config["contexto"],
                        config["modelo"],
                        config["temperatura"]
                    )

                    print("\n--- RESPUESTA DEL MODELO ---")
                    print(resultado)

                    # EVALUACIÓN DE LA PRUEBA:
# Pregunta: Crea una función saludar en Python
# La respuesta es satisfactoria si el modelo crea la función sin añadir información incorrecta.

                except httpx.ConnectError:
                    print("Error: No se puede conectar con Ollama.")
                    print("Comprueba que Ollama esté ejecutándose.")

                except ResponseError as error:
                    print(f"Error de Ollama: {error}")

                except Exception as error:
                    print(f"Error inesperado: {error}")

            case "3":
                print("\n--- CONFIGURACIÓN ---")

                nuevo_system = input(
                    "Nuevo System Prompt (Enter para conservar): "
                ).strip()

                if nuevo_system:
                    config["system_prompt"] = nuevo_system

                nuevo_user = input(
                    "Nuevo User Prompt (Enter para conservar): "
                ).strip()

                if nuevo_user:
                    config["user_prompt"] = nuevo_user

                nueva_temp = input(
                    "Nueva temperatura de 0 a 1 (Enter para conservar): "
                ).strip()

                if nueva_temp:
                    try:
                        valor = float(nueva_temp)

                        if 0 <= valor <= 1:
                            config["temperatura"] = valor
                        else:
                            print("La temperatura debe estar entre 0 y 1.")

                    except ValueError:
                        print("Debes introducir un número válido.")

                print("Configuración actualizada.")

            case "4":
                print("\n--- CONFIGURACIÓN ACTUAL ---")
                print(f"Modelo: {config['modelo']}")
                print(f"Temperatura: {config['temperatura']}")
                print(f"System Prompt: {config['system_prompt']}")
                print(f"User Prompt: {config['user_prompt']}")
                print(f"Contexto cargado: {bool(config['contexto'])}")

            case "0":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida.")


if __name__ == "__main__":
    main()
