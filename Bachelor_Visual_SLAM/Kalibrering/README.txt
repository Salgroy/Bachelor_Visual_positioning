# Merk, alle norske ekstrabokstaver er erstattet med o eller a

# For aa kalibrere dataset, ta video av et rutebrett som vedlagt i kalibrering_chessboard_540p.
# Det er VELDIG viktig at kalibreringssettet er 100% flatt på underlaget. Ingen boyninger eller forvrengninger. Dette odelegger testsettet.
# Paase også at videofilen ikke har motion blur og at frames ser "gode" ut.

# Aapne en linux maskin med god lagringsplass og kjor kommandoen "ffmpeg -i ../(Navn_på_video) -vf fps=(Antall_frames_optimalt_for_koden) (Navn_på_dataset_%06d.png)".
# Denne kommandoen deler opp videofilen i mange bilder som kan sendes gjennom koden.
# Gjor det samme med videofilen fra omraadet som skal testes ogsaa.

# Send saa dette datasettet gjennom kalibreringsfunksjonen til MatLab. Denne kan finnes under APPS. Velg datasett og velg riktig kalibreringssett.