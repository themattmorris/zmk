"""Base classes."""

import abc
import enum
from typing import ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field, model_serializer


class FrozenModel(BaseModel):
    """BaseModel that is immutable."""

    model_config = ConfigDict(frozen=True, validate_default=True)


class CustomDefinedBehavior(FrozenModel):
    """A ZMK [custom defined behavior](https://zmk.dev/docs/keymaps/behaviors)."""

    compatible: ClassVar[str] = NotImplemented
    exclude: ClassVar[set[str] | None] = None

    name: str

    @property
    @abc.abstractmethod
    def bindings(self) -> str:
        """Bindings definition."""

    @property
    def identifier(self) -> str:
        """Full identifying name."""
        return "_".join([self.name, type(self).__name__.lower()])

    @property
    def as_zmk(self) -> str:
        """The ZMK representation of the behavior."""
        result = f"\n{' ' * 4}{self.identifier} {{"

        data = self.model_dump(
            by_alias=True,
            exclude_none=True,
            exclude={*(self.exclude or ()), "name"},
        ) | {"bindings": self.bindings}

        for k, v in data.items():
            value = " ".join([str(x) for x in v]) if isinstance(v, list) else v
            result += f"\n{' ' * 8}{k.replace('_', '-')} = <{value}>;"

        return f"{result}\n}};"


class KeyPosition(FrozenModel):
    """A MoErgo Glove80 [key position](
    https://docs.moergo.com/layout-editor-guide/advanced-usage-custom-defined-behaviors/#key-positions)
    based on row and column.
    """

    half: Literal["left", "right"]
    """Which half of the glove80 the key is on."""

    row: int = Field(ge=1, le=6)
    """Row of the key starting from the top."""

    column: int = Field(ge=1, le=8)
    """Column of the key starting from the left."""

    @model_serializer
    def position(self) -> int:
        """The actual integer representation of the key position."""
        # TODO
        return 0


class StrEnum(enum.StrEnum):
    """A string enumeration."""

    @staticmethod
    def _generate_next_value_(
        name: str,
        start: int,  # noqa: ARG004
        count: int,  # noqa: ARG004
        last_values: list[str],  # noqa: ARG004
    ) -> str:
        """Return the member name."""
        return name


@enum.unique
class KeyCode(StrEnum):
    """A [key code](https://zmk.dev/docs/keymaps/list-of-keycodes)."""

    # https://zmk.dev/docs/keymaps/list-of-keycodes#letters
    A = enum.auto()
    B = enum.auto()
    C = enum.auto()
    D = enum.auto()
    E = enum.auto()
    F = enum.auto()
    G = enum.auto()
    H = enum.auto()
    I = enum.auto()
    J = enum.auto()
    K = enum.auto()
    L = enum.auto()
    M = enum.auto()
    N = enum.auto()
    O = enum.auto()
    P = enum.auto()
    Q = enum.auto()
    R = enum.auto()
    S = enum.auto()
    T = enum.auto()
    U = enum.auto()
    V = enum.auto()
    W = enum.auto()
    X = enum.auto()
    Y = enum.auto()
    Z = enum.auto()

    # https://zmk.dev/docs/keymaps/list-of-keycodes#numbers
    NUMBER_1 = enum.auto()
    NUMBER_2 = enum.auto()
    NUMBER_3 = enum.auto()
    NUMBER_4 = enum.auto()
    NUMBER_5 = enum.auto()
    NUMBER_6 = enum.auto()
    NUMBER_7 = enum.auto()
    NUMBER_8 = enum.auto()
    NUMBER_9 = enum.auto()
    NUMBER_0 = enum.auto()

    # https://zmk.dev/docs/keymaps/list-of-keycodes#symbols--punctuation
    EXCLAMATION = enum.auto()
    AT_SIGN = enum.auto()
    HASH = enum.auto()
    DOLLAR = enum.auto()
    PERCENT = enum.auto()
    CARET = enum.auto()
    AMPERSAND = enum.auto()
    ASTERISK = enum.auto()
    LEFT_PARENTHESIS = enum.auto()
    RIGHT_PARENTHESIS = enum.auto()
    EQUAL = enum.auto()
    PLUS = enum.auto()
    MINUS = enum.auto()
    UNDERSCORE = enum.auto()
    SLASH = enum.auto()
    QUESTION = enum.auto()
    BACKSLASH = enum.auto()
    PIPE = enum.auto()
    SEMICOLON = enum.auto()
    COLON = enum.auto()
    SINGLE_QUOTE = enum.auto()
    DOUBLE_QUOTES = enum.auto()
    COMMA = enum.auto()
    LESS_THAN = enum.auto()
    PERIOD = enum.auto()
    GREATER_THAN = enum.auto()
    LEFT_BRACKET = enum.auto()
    LEFT_BRACE = enum.auto()
    RIGHT_BRACKET = enum.auto()
    RIGHT_BRACE = enum.auto()
    GRAVE = enum.auto()
    TILDE = enum.auto()

    # https://zmk.dev/docs/keymaps/list-of-keycodes#control--whitespace
    ESCAPE = enum.auto()
    RETURN = enum.auto()
    SPACE = enum.auto()
    TAB = enum.auto()
    BACKSPACE = enum.auto()
    DELETE = enum.auto()
    INSERT = enum.auto()

    # https://zmk.dev/docs/keymaps/list-of-keycodes#navigation
    HOME = enum.auto()
    END = enum.auto()
    PAGE_UP = enum.auto()
    PAGE_DOWN = enum.auto()
    UP_ARROW = enum.auto()
    DOWN_ARROW = enum.auto()
    LEFT_ARROW = enum.auto()
    RIGHT_ARROW = enum.auto()

    # https://zmk.dev/docs/keymaps/list-of-keycodes#locks
    CAPSLOCK = enum.auto()
    LOCKING_CAPS = enum.auto()
    SCROLLLOCK = enum.auto()
    LOCKING_SCROLL = enum.auto()
    LOCKING_NUM = enum.auto()

    # https://zmk.dev/docs/keymaps/list-of-keycodes#f-keys
    F1 = enum.auto()
    F2 = enum.auto()
    F3 = enum.auto()
    F4 = enum.auto()
    F5 = enum.auto()
    F6 = enum.auto()
    F7 = enum.auto()
    F8 = enum.auto()
    F9 = enum.auto()
    F10 = enum.auto()
    F11 = enum.auto()
    F12 = enum.auto()
    F13 = enum.auto()
    F14 = enum.auto()
    F15 = enum.auto()
    F16 = enum.auto()
    F17 = enum.auto()
    F18 = enum.auto()
    F19 = enum.auto()
    F20 = enum.auto()
    F21 = enum.auto()
    F22 = enum.auto()
    F23 = enum.auto()
    F24 = enum.auto()

    # https://zmk.dev/docs/keymaps/list-of-keycodes#miscellaneous
    PRINTSCREEN = enum.auto()
    PAUSE_BREAK = enum.auto()
    ALT_ERASE = enum.auto()
    SYSREQ = enum.auto()
    KCANCEL = enum.auto()
    CLEAR = enum.auto()
    CLEAR_AGAIN = enum.auto()
    CRSEL = enum.auto()
    PRIOR = enum.auto()
    SEPARATOR = enum.auto()
    OUT = enum.auto()
    OPER = enum.auto()
    EXSEL = enum.auto()
    K_EDIT = enum.auto()


@enum.unique
class Modifier(StrEnum):
    """A [modifier](https://zmk.dev/docs/keymaps/list-of-keycodes#modifiers) to a key
    press.
    """

    LEFT_SHIFT = "LS"
    LEFT_CONTROL = "LC"
    LEFT_ALT = "LA"
    LEFT_GUI = "LG"
    RIGHT_SHIFT = "RS"
    RIGHT_CONTROL = "RC"
    RIGHT_ALT = "RA"
    RIGHT_GUI = "RG"


class KeyPress(FrozenModel):
    """A key press definition."""

    code: KeyCode
    modifier: Modifier | None = None

    @property
    def as_zmk(self) -> str:
        """ZMK representation."""
        code = self.code.value
        return f"{modifier}({code})" if (modifier := self.modifier) else str(code)
