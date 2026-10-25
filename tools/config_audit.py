#!/usr/bin/env python3
"""Busca patrones de riesgo en ficheros de configuración de texto."""
import argparse
import json
import re
from pathlib import Path

RULES = [
    ("DEBUG_TRUE", re.compile(r"^\s*(DEBUG|APP_DEBUG)\s*=\s*(true|1|yes)\s*$", re.I),
     "media", "Desactiva debug en producción."),
    ("TLS_VERIFY_DISABLED", re.compile(r"^\s*(VERIFY_TLS|SSL_VERIFY|CURL_SSL_VERIFYPEER)\s*=\s*(false|0|no)\s*$", re.I),
     "alta", "Activa la validación TLS salvo excepción documentada."),
    ("BIND_ALL", re.compile(r"^\s*(HOST|BIND_HOST)\s*=\s*0\.0\.0\.0\s*$", re.I),
     "media", "Confirma que la exposición en todas las interfaces es intencionada."),
    ("PLACEHOLDER_SECRET", re.compile(r"^\s*(PASSWORD|API_KEY|SECRET|TOKEN)\s*=\s*(changeme|password|example|test)\s*$", re.I),
     "media", "No uses secretos débiles ni valores de ejemplo fuera de pruebas."),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        lines = args.file.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        parser.error(f"No se puede leer el fichero: {exc}")
    findings = []
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", ";", "//")):
            continue
        for rule_id, pattern, severity, recommendation in RULES:
            if pattern.search(line):
                findings.append({"rule_id": rule_id, "line": number, "severity": severity,
                                 "recommendation": recommendation,
                                 "evidence": line.split("=", 1)[0].strip() + "=<redacted>"})
    print(json.dumps({"file": args.file.name, "findings_count": len(findings),
                      "findings": findings,
                      "limitations": ["Análisis textual: puede producir falsos positivos.",
                                      "No muestra los valores que podrían contener secretos.",
                                      "No interpreta completamente YAML, JSON o variables dinámicas."]},
                     indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
