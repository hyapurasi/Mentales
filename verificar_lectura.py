import argparse
from difflib import SequenceMatcher

try:
    import speech_recognition as sr
except ImportError as e:
    raise SystemExit("Debe instalar speech_recognition y sus dependencias: " + str(e))


def reconocer_voz(audio_file=None, timeout=5):
    recognizer = sr.Recognizer()
    if audio_file:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
    else:
        with sr.Microphone() as source:
            print("Hable ahora...")
            audio = recognizer.listen(source, timeout=timeout)
    try:
        return recognizer.recognize_sphinx(audio, language="es-ES")
    except sr.UnknownValueError:
        return ""


def verificar_texto(objetivo, reconocido):
    return SequenceMatcher(None, objetivo.lower(), reconocido.lower()).ratio()


def main():
    parser = argparse.ArgumentParser(description="Verifica si el audio coincide con un texto dado")
    parser.add_argument("texto", help="Palabra o frase a leer")
    parser.add_argument("--audio", help="Ruta opcional a un archivo de audio WAV")
    parser.add_argument("--umbral", type=float, default=0.8, help="Nivel minimo de similitud aceptado")
    args = parser.parse_args()

    reconocido = reconocer_voz(args.audio)
    print("Reconocido:", reconocido)

    similitud = verificar_texto(args.texto, reconocido)
    print("Similitud:", similitud)

    if similitud >= args.umbral:
        print("Lectura correcta")
    else:
        print("La lectura no coincide")


if __name__ == "__main__":
    main()
