#This file is of abstract syntax tree (AST) node definitions.

from dataclasses import dataclass
from typing import List, Optional, Union

# Base class for all AST nodes ASTNode is the base (parent) class for all other AST node types.
#It doesn’t do anything itself, but helps us group all node types together under one type.

class ASTNode:
    pass

# Root node; body is a list of things in the program like function definitions, statements, etc.
@dataclass
class Program(ASTNode):
    body: List[ASTNode]

# Statements
@dataclass
class FunctionDef(ASTNode):
    name: str
    params: List[str]
    body: List[ASTNode]

@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    then_branch: List[ASTNode]
    elif_branches: List[tuple[ASTNode, List[ASTNode]]]
    else_branch: Optional[List[ASTNode]]

@dataclass
class WhileLoop(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class ForLoop(ASTNode):
    var: str
    iterable: ASTNode
    body: List[ASTNode]

@dataclass
class Return(ASTNode):
    value: Optional[ASTNode]

@dataclass
class Assignment(ASTNode):
    target: str
    value: ASTNode

@dataclass
class ExpressionStatement(ASTNode):
    expression: ASTNode

# Expressions
@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    operator: str
    operand: ASTNode

@dataclass
class Call(ASTNode):
    func: ASTNode
    args: List[ASTNode]

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class Literal(ASTNode):
    value: Union[str, int, float, bool, None]
