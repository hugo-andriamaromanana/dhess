from typing import TypeAlias
from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable
from icecream import ic  # type: ignore


class Piece(str, Enum):
    """Chess pieces Enum"""
    PAWN = "Pawn"
    BISHOP = "Bishop"
    KNIGHT = "Knight"
    ROOK = "Rook"
    KING = "King"
    QUEEN = "Queen"


class MacroType(str, Enum):
    """Different types of Macro quests"""
    CAPTURE = auto()
    MOVE_CONSTRAINTS = auto()
    PROMOTION = auto()
    OTHER = auto()

def promote_to(piece: Piece) -> str:
    return f"Your first promoted Pawn has to be a {piece.value}"

def capture(piece: Piece) -> str:
    return f"Be the first to capture the {piece.value}"

WithPiece: TypeAlias = Callable[[Piece], str]

QUEST_TYPE_MAP: dict[MacroType, WithPiece] = {
    MacroType.PROMOTION: promote_to,
    MacroType.CAPTURE: capture
}

@dataclass
class MacroQuest:
    title: str
    type: MacroType


def infer_action_from_quest(quest: MacroQuest, value: Piece) -> str:
    return QUEST_TYPE_MAP[quest.type](value)

quest = MacroQuest("Leo", MacroType.CAPTURE)

print(infer_action_from_quest(quest, Piece.KNIGHT))


