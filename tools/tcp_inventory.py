#!/usr/bin/env python3
"""Inventario TCP de bajo impacto para activos autorizados."""
import argparse
import json
import socket
import time
from datetime import datetime, timezone


def parse_ports(value):
    ports = []
    for item in value.split(","):
        if not item.strip():
            continue
        port = int(item.strip())
        if not 1 <= port <= 65535:
            raise argparse.ArgumentTypeError(f"Puerto fuera de rango: {port}")
        if port not in ports:
            ports.append(port)
    if not ports or len(ports) > 128:
        raise argparse.ArgumentTypeError("Indica entre 1 y 128 puertos.")
    return ports


def check_port(host, port, timeout):
    started = time.perf_counter()
    state, error = "sin_respuesta", None
    try:
        with socket.create_connection((host, port), timeout=timeout):
            state = "abierto"
    except ConnectionRefusedError:
        state = "cerrado_o_rechazado"
    except socket.timeout:
        state = "sin_respuesta"
    except OSError as exc:
        state, error = "error", str(exc)
    return {"port": port, "state": state,
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
            "error": error}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host", help="IP o nombre del activo autorizado")
    parser.add_argument("--ports", type=parse_ports, default=parse_ports("22,80,443"))
    parser.add_argument("--timeout", type=float, default=0.5)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    if not 0.1 <= args.timeout <= 3:
        parser.error("--timeout debe estar entre 0.1 y 3 segundos")
    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "target": args.host,
        "method": "TCP connect; no service fingerprinting",
        "results": [check_port(args.host, p, args.timeout) for p in args.ports],
        "limitations": ["Un puerto sin respuesta no demuestra que esté cerrado.",
                        "El resultado depende de firewall, ruta y servicio.",
                        "Usar solo contra activos propios o autorizados."]
    }
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Objetivo: {report['target']} | UTC: {report['timestamp_utc']}")
        for row in report["results"]:
            print(f"{row['port']:>5}/tcp  {row['state']:<22} {row['elapsed_ms']:>8} ms")
        print("La conectividad observada no equivale a identificar una vulnerabilidad.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
