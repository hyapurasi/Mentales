# Mentales
Aplicación web para desarrollar procesos mentales en niños

## Verificación de lectura

El script `verificar_lectura.py` permite comprobar si la voz grabada coincide con una palabra o frase.

### Requisitos

Instalar las dependencias:
```
pip install SpeechRecognition pyaudio pocketsphinx
```

### Uso

Ejecute el script indicando el texto a leer. Opcionalmente puede proporcionar un archivo WAV:
```
python verificar_lectura.py "hola mundo" --audio ejemplo.wav
```
Si no se indica `--audio`, se utilizará el micrófono por defecto.
