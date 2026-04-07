"""
Custom exceptions used by the library.
"""


class PicasoError(RuntimeError):
    """Something went wrong while processing the command."""


class CommunicationError(RuntimeError):
    """Communication with device failed (e.g. a serial read / write timeout)."""
