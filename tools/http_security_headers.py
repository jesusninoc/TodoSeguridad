#!/usr/bin/env python3
"""Revisión no intrusiva de cabeceras HTTP de un activo autorizado."""
import argparse
import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from urllib.parse import urlparse

RULES = {
    "Strict-Transport-Security": ("media", "Evalúa HSTS tras revisar subdominios y despliegue."),
    "Content-Security-Policy": ("alta", "Define una CSP adaptada a los recursos legítimos."),
    "X-Content-Type-Options": ("baja", "Considera X-Content-Type-Options: nosniff."),
    "Referrer-Policy": ("baja", "Configura una política de Referer adecuada."),
    "Permissions-Policy": ("baja", "Limita funciones del navegador no necesarias."),
    "X-Frame-Options": ("media", "Revisa CSP frame-ancestors y/o X-Frame-Options."),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()
    parsed = urlparse(args.url)
    if parsed.scheme not in ("https", "http") or not parsed.hostname:
        parser.error("La URL debe comenzar por http:// o https://")
    if not 1 <= args.timeout <= 15:
        parser.error("--timeout debe estar entre 1 y 15 segundos")
    request = urllib.request.Request(args.url, headers={"User-Agent": "PortfolioHeaderReview/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=args.timeout) as response:
            status, headers, final_url = response.status, dict(response.headers.items()), response.geturl()
    except urllib.error.HTTPError as exc:
        status, headers, final_url = exc.code, dict(exc.headers.items()), exc.geturl()
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        print(json.dumps({"url": args.url, "error": str(exc)}, indent=2))
        return 2
    normalized = {key.lower(): value for key, value in headers.items()}
    findings = []
    for header, (severity, recommendation) in RULES.items():
        present = header.lower() in normalized
        findings.append({"header": header, "present": present,
                         "severity_if_missing": None if present else severity,
                         "recommendation": None if present else recommendation})
    print(json.dumps({
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "requested_url": args.url, "final_url": final_url, "http_status": status,
        "headers": headers, "findings": findings,
        "limitations": ["Una cabecera ausente no confirma por sí sola una vulnerabilidad.",
                        "No se analizan cookies, rutas autenticadas ni contenido de la aplicación."]
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
