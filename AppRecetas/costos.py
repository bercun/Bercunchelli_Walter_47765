"""Utilidades para costo estimado manteniendo ingredientes como texto libre.

Formato sugerido: "2 kg harina, 3 unidad huevo, 200 ml leche" (coma o salto de línea).
El parser es tolerante: si no hay cantidad/unidad, cantidad=1 unidad='unidad'.
"""
import re
import unicodedata
from decimal import Decimal, InvalidOperation

# unidad ingresada -> (unidad_base, factor). Ej: 1 kg = 1000 g.
CONVERSIONES = {
    "g": ("g", Decimal("1")),
    "gr": ("g", Decimal("1")),
    "gramo": ("g", Decimal("1")),
    "gramos": ("g", Decimal("1")),
    "kg": ("g", Decimal("1000")),
    "kilo": ("g", Decimal("1000")),
    "kilos": ("g", Decimal("1000")),
    "ml": ("ml", Decimal("1")),
    "mililitro": ("ml", Decimal("1")),
    "mililitros": ("ml", Decimal("1")),
    "l": ("ml", Decimal("1000")),
    "lt": ("ml", Decimal("1000")),
    "litro": ("ml", Decimal("1000")),
    "litros": ("ml", Decimal("1000")),
    "unidad": ("unidad", Decimal("1")),
    "unidades": ("unidad", Decimal("1")),
    "u": ("unidad", Decimal("1")),
    "taza": ("ml", Decimal("200")),
    "tazas": ("ml", Decimal("200")),
    "cda": ("ml", Decimal("15")),
    "cucharada": ("ml", Decimal("15")),
    "cucharadas": ("ml", Decimal("15")),
    "cdta": ("ml", Decimal("5")),
    "cucharadita": ("ml", Decimal("5")),
    "cucharaditas": ("ml", Decimal("5")),
    "pizca": ("pizca", Decimal("1")),
    "pizcas": ("pizca", Decimal("1")),
}

# (desde_base, hacia_base) -> factor multiplicador
CONVERSION_BASE = {
    ("g", "g"): Decimal("1"),
    ("g", "kg"): Decimal("0.001"),
    ("kg", "g"): Decimal("1000"),
    ("kg", "kg"): Decimal("1"),
    ("ml", "ml"): Decimal("1"),
    ("ml", "l"): Decimal("0.001"),
    ("l", "ml"): Decimal("1000"),
    ("l", "l"): Decimal("1"),
    ("unidad", "unidad"): Decimal("1"),
    ("taza", "ml"): Decimal("200"),
    ("cda", "ml"): Decimal("15"),
    ("cdta", "ml"): Decimal("5"),
    ("pizca", "pizca"): Decimal("1"),
}

_RE_CANT = re.compile(
    r"^\s*(?P<cant>\d+(?:[.,]\d+)?)?\s*(?P<uni>[a-zA-Záéíóúñ]+)?\s*(?:de\s+)?(?P<nombre>.*)$"
)


def normalizar(texto):
    if not texto:
        return ""
    texto = texto.strip().lower()
    texto = "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", texto)


def parse_ingredientes_texto(texto):
    """Devuelve lista de dicts {cantidad: Decimal, unidad: str, nombre: str, nombre_norm: str}."""
    if not texto:
        return []
    fragmentos = re.split(r"[,\n;]+", texto)
    items = []
    for frag in fragmentos:
        frag = frag.strip(" .-")
        if not frag:
            continue
        m = _RE_CANT.match(frag)
        cant_raw = (m.group("cant") or "").replace(",", ".")
        try:
            cantidad = Decimal(cant_raw) if cant_raw else Decimal("1")
        except InvalidOperation:
            cantidad = Decimal("1")
        uni_raw = normalizar(m.group("uni") or "unidad")
        nombre = (m.group("nombre") or frag).strip(" .-")
        if not nombre:
            continue
        # Si la "unidad" no es conocida y no había cantidad, era parte del nombre.
        if uni_raw not in CONVERSIONES and cant_raw == "":
            nombre = f"{m.group('uni')} {nombre}".strip()
            uni_raw = "unidad"
        if uni_raw not in CONVERSIONES:
            # ej "50-60 g de ..." -> el nombre conserva el resto; unidad por defecto
            uni_raw = "unidad"
        unidad_base, factor = CONVERSIONES[uni_raw]
        items.append({
            "cantidad": cantidad,
            "unidad": uni_raw,
            "cantidad_base": cantidad * factor,
            "unidad_base": unidad_base,
            "nombre": nombre.strip(),
            "nombre_norm": normalizar(nombre),
        })
    return items


def convertir(cantidad, desde, hacia):
    if desde == hacia:
        return cantidad
    factor = CONVERSION_BASE.get((desde, hacia))
    if factor is None:
        return None
    return cantidad * factor


def calcular_costo(items, precios):
    """precios: iterable de IngredientePrecio. Match por nombre exacto normalizado, si no icontains.

    Devuelve {"total": Decimal, "detalle": [...], "faltantes": [...]}.
    """
    mapa = {normalizar(p.nombre): p for p in precios}
    total = Decimal("0")
    detalle, faltantes = [], []
    for it in items:
        p = mapa.get(it["nombre_norm"])
        if p is None:
            # fallback: contiene / contenido en (para "queso parmesano" vs "parmesano")
            for key, cand in mapa.items():
                if key and (key in it["nombre_norm"] or it["nombre_norm"] in key):
                    p = cand
                    break
        if p is None:
            faltantes.append(it["nombre"])
            continue
        cant = convertir(it["cantidad_base"], it["unidad_base"], p.unidad_base)
        if cant is None:
            # Sin conversión (ej receta en g y precio en unidad): se informa como faltante de unidad
            faltantes.append(f"{it['nombre']} (sin conversión {it['unidad_base']}->{p.unidad_base})")
            continue
        subtotal = cant * p.precio_estimado
        total += subtotal
        detalle.append({
            "nombre": it["nombre"],
            "cantidad": it["cantidad"],
            "unidad": it["unidad"],
            "precio_unit": p.precio_estimado,
            "unidad_precio": p.unidad_base,
            "subtotal": subtotal,
        })
    return {"total": total, "detalle": detalle, "faltantes": faltantes}
