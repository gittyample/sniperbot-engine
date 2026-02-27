from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable


@dataclass
class IngestionPipeline:
    """
    Data ingestion scaffold.

    Responsibilities:
    - Receive raw JSON payloads from an API client
    - Validate/normalize fields into a consistent schema
    - Output structured records for downstream evaluation
    """

    source: str

    def normalize(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize a single payload into a stable internal schema.
        """
        raise NotImplementedError(
            "Normalization logic intentionally omitted in public repo."
        )

    def normalize_batch(self, payloads: Iterable[Dict[str, Any]]) -> list[Dict[str, Any]]:
        return [self.normalize(p) for p in payloads]
