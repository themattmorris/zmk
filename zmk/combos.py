"""[Key combinations](https://zmk.dev/docs/keymaps/combos)."""

from typing import ClassVar

from .base import CustomDefinedBehavior, KeyPosition, KeyPress
from .macros import Macro


class Combo(CustomDefinedBehavior):
    """Key combination definition."""

    compatible: ClassVar[str] = "combos"
    exclude: ClassVar[set[str] | None] = {"macro"}

    timeout_ms: int = 50
    key_positions: list[int | KeyPosition]
    macro: list[KeyPress]
    layers: list[int] = [0]  # noqa: RUF012

    @property
    def macro_behavior(self) -> Macro:
        """Macro representation of macro."""
        return Macro(name=self.name, keys=self.macro)

    @property
    def bindings(self) -> str:
        """Macro binding."""
        return f"&{self.macro_behavior.identifier}"
