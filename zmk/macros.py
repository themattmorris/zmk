"""[Macros](https://zmk.dev/docs/keymaps/behaviors/macros)."""

from typing import ClassVar

from .base import CustomDefinedBehavior, KeyPress


class Macro(CustomDefinedBehavior):
    """Macro definition."""

    compatible: ClassVar[str] = "behavior-macro"
    exclude: ClassVar[set[str] | None] = {"keys"}

    binding_cells: list[int] = [0]  # noqa: RUF012
    keys: list[KeyPress]

    @property
    def bindings(self) -> str:
        """Key press bindings."""
        return " ".join(
            [
                "&macro_tap",
                *[" ".join(["&kp", key_press.as_zmk]) for key_press in self.keys],
            ]
        )
