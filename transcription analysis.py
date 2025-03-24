import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Cargar el dataset (asegúrate de que tu DataFrame tiene una columna 'video_id')
df_videos = pd.read_csv("C:\\Users\\Administrator\\Downloads\\ids")

video_ids = df_videos["video_id"].tolist()

# Función para obtener la transcripción de un video
def get_transcription(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])  # Unir todas las líneas en un solo string
    except TranscriptsDisabled:
        return None  # Si el video no tiene transcripción disponible
    except VideoUnavailable:
        return None  # Si el video no está disponible
    except Exception as e:
        return None  # Captura otros errores y continúa

# Usar ThreadPoolExecutor para obtener transcripciones en paralelo
transcriptions = {}
with ThreadPoolExecutor(max_workers=10) as executor:  # Ajusta el número de hilos según necesidad
    future_to_video = {executor.submit(get_transcription, vid): vid for vid in video_ids}

    for future in tqdm(as_completed(future_to_video), total=len(video_ids), desc="Procesando videos"):
        video_id = future_to_video[future]
        transcriptions[video_id] = future.result()  # Guardar la transcripción

# Convertir a DataFrame y guardar en un archivo CSV
df_transcriptions = pd.DataFrame(list(transcriptions.items()), columns=["video_id", "transcription"])
df_transcriptions.to_csv("transcriptions.csv", index=False)

print("\n✅ Proceso completado. Transcripciones guardadas en 'transcriptions.csv'")
