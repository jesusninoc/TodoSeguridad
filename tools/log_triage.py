#!/usr/bin/env python3
"""Triage heurístico de registros de autenticación local."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
FAIL_RE = re.compile(r"failed password|authentication failure|login failed|invalid user", re.I)
SUCCESS_RE = re.compile(r"accepted password|accepted publickey|login successful", re.I)
DENIED_RE = re.compile(r"permission denied|access denied|account locked", re.I)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--threshold", type=int, default=5)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    if not 2 <= args.threshold <= 10000:
        parser.error("--threshold debe estar entre 2 y 10000")
    try:
        lines = args.file.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        parser.error(f"No se puede leer el fichero: {exc}")
    failures, successes, denied = Counter(), 0, 0
    matches = []
    for number, line in enumerate(lines, 1):
        match = IP_RE.search(line)
        ip = match.group(0) if match else "sin_ip"
        if FAIL_RE.search(line):
            failures[ip] += 1
            matches.append({"line": number, "type": "auth_failure", "ip": ip})
        successes += bool(SUCCESS_RE.search(line))
        denied += bool(DENIED_RE.search(line))
    report = {
        "file": args.file.name, "total_lines": len(lines),
        "authentication_failures": sum(failures.values()),
        "successful_authentication_markers": successes, "access_denied_markers": denied,
        "sources_over_threshold": [{"ip": ip, "failures": n} for ip, n in failures.most_common()
                                   if n >= args.threshold],
        "top_failure_sources": [{"ip": ip, "failures": n} for ip, n in failures.most_common(10)],
        "matched_lines": matches[:100],
        "limitations": ["Las reglas dependen del formato del log.",
                        "Una IP puede ser proxy, NAT o equipo compartido.",
                        "No concluye que exista un ataque; requiere correlación humana."]
    }
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Fichero: {report['file']} ({report['total_lines']} líneas)")
        print(f"Fallos de autenticación: {report['authentication_failures']}")
        print(f"Marcadores de éxito: {successes}; denegaciones: {denied}")
        for item in report["sources_over_threshold"]:
            print(f"Revisar {item['ip']}: {item['failures']} fallos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
