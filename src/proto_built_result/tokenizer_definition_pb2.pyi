from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TokenizingRequest(_message.Message):
    __slots__ = ["title"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class TokenizingResult(_message.Message):
    __slots__ = ["tokens", "words"]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedScalarFieldContainer[str]
    words: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tokens: _Optional[_Iterable[str]] = ..., words: _Optional[_Iterable[str]] = ...) -> None: ...