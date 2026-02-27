from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OAuthClient:
    """
    Minimal OAuth client scaffold.

    Purpose:
    - Encapsulate token exchange / refresh lifecycle for external APIs.
    - Keep auth concerns isolated from ingestion + signal logic.
    """

    client_id: str

    def refresh_token(self) -> str:
        """
        Refresh an access token.

        Note: Implementation intentionally omitted to avoid exposing secrets.
        """
        raise NotImplementedError(
            "Token refresh logic intentionally omitted in public repo."
        )
