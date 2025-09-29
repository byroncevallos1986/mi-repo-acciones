# script.py
from datetime import datetime, timezone, timedelta

try:
    # Python 3.9+: zoneinfo
    from zoneinfo import ZoneInfo
    ec_tz = ZoneInfo("America/Guayaquil")
    now_ec = datetime.now(ec_tz)
    now_utc = now_ec.astimezone(timezone.utc)
except Exception:
    # Fallback sencillo si zoneinfo no está disponible
    now_utc = datetime.now(timezone.utc)
    now_ec = now_utc - timedelta(hours=5)

print("Hora UTC:", now_utc.isoformat())
print("Hora Ecuador (America/Guayaquil):", now_ec.isoformat())

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"UTC: {now_utc.isoformat()}\nEcuador: {now_ec.isoformat()}\n")
